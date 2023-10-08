from rest_framework import serializers
from src.apps.project.models import Project
from src.apps.gallery.serializers import ImageSerializer
from src.apps.handbook.models import Category, Tag
from src.apps.gallery.models import Image
from src.apps.handbook.serializers import CategoryListSerializer, TagListSerializer
from src.apps.accounts.serializers import UserShortSerializer

class ProjectListSerializer(serializers.ModelSerializer):

    images = ImageSerializer(many=True)
    categories = CategoryListSerializer(many=True)
    tags = TagListSerializer(many=True)
    user = UserShortSerializer()

    class Meta:
        model = Project
        fields = (
            'id',
            'user',
            'categories',
            'tags',
            'images',
            'name',
            'slug',
            'description',
            'likes_count',
            'comments_count',
            'views_count',
            'downloads_count',
            'file',
        )



class ProjectDetailSerializer(serializers.ModelSerializer):

    user = UserShortSerializer()
    images = ImageSerializer(many=True)
    categories = CategoryListSerializer(many=True)
    tags = TagListSerializer(many=True)
    members = UserShortSerializer(many=True)

    class Meta:
        model = Project
        fields = (
            'user',
            'categories',
            'tags',
            'members',
            'images',
            'name',
            'description',
            'likes_count',
            'comments_count',
            'views_count',
            'downloads_count',
            'file',
        )
        lookup_field = 'slug'




class ProjectCreateSerializer(serializers.ModelSerializer):

    images = ImageSerializer(many=True, required=False)
    categories = serializers.ListField(child=serializers.IntegerField())
    tags = serializers.ListField(child=serializers.CharField())

    def validate_categories(self, value):
        categories = []
        if value:
            for category in value:
                try:
                    category = Category.objects.get(pk=category)
                except Category.DoesNotExist:
                    raise serializers.ValidationError(f"Category with id {category} does not exist")
                if Category.objects.filter(parent=category):
                    raise serializers.ValidationError("Нужно добавить только те категории у которых нету дочерей")
                categories.append(category)
        return categories

    def create(self, validated_data: dict):
        user = self.context['request'].user
        tags_data = validated_data.pop('tags', [])
        images_data = validated_data.pop('images', [])
        categories = validated_data.pop('categories', [])

        project = Project.objects.create(user=user, **validated_data)
        project.categories.set(categories)

        tags = []
        for tag_name in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tags.append(tag)
        project.tags.set(tags)

        images = []
        for image_data in images_data:
            image = Image.objects.create(**image_data)
            images.append(image)
        project.images.set(images)

        return project
    
    class Meta:
        model = Project
        fields = (
            'categories',
            'tags',
            'images',
            'name',
            'description',
            'file',
        )





class ProjectUpdateSerializer(serializers.ModelSerializer):

    images = ImageSerializer(many=True, required=False)
    categories = serializers.ListField(child=serializers.IntegerField(), required=False)
    tags = serializers.ListField(child=serializers.CharField(), required=False)
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)

    def validate_categories(self, value):
        categories = []
        if value:
            for category in value:
                try:
                    category = Category.objects.get(pk=category)
                except Category.DoesNotExist:
                    raise serializers.ValidationError(f"Category with id {category} does not exist")
                if Category.objects.filter(parent=category):
                    raise serializers.ValidationError("Нужно добавить только те категории у которых нету дочерей")
                categories.append(category)
        return categories

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.file = validated_data.get('file', instance.file)

        categories_data = validated_data.get('categories', [])
        tags_data = validated_data.get('tags', [])
        images_data = validated_data.get('images', [])

        if categories_data:
            instance.categories.clear()
            instance.categories.set(categories_data)

        if tags_data:
            instance.tags.clear()
            for tag_name in tags_data:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                instance.tags.add(tag)

        if images_data:
            instance.images.clear()
            for image_data in images_data:
                image, _ = Image.objects.get_or_create(**image_data)
                instance.images.add(image)
        return instance


    class Meta:
        model = Project
        fields = (
            'categories',
            'tags',
            'images',
            'name',
            'description',
            'file',
        )

