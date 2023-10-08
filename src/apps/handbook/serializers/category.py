from rest_framework import serializers
from src.apps.handbook.models import Category


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug',)


class CategoryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
            'parent',
            'created_at',
            'updated_at',
        )
        lookup_field = 'slug'



class NestedCategorySerializer(serializers.ModelSerializer):
    """ Nested category serializer """

    childrens = serializers.SerializerMethodField()

    def get_childrens(self, obj):
        children_categories = Category.objects.filter(parent=obj)
        serializer = NestedCategorySerializer(children_categories, many=True)
        return serializer.data

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
            'childrens',
        )


class CategorySlugListSerializer(serializers.Serializer):
    categories = serializers.ListField(child=serializers.CharField())

    def validate_categories(self, value):
        categories = []
        for category_slug in value:
            try:
                category = Category.objects.get(slug=category_slug)
            except Category.DoesNotExist:
                raise serializers.ValidationError(f"Category with slug {category_slug} does not exist")
            categories.append(category)
        return categories
