from rest_framework import serializers
from .models import Folder, Image

class ImageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'id',
            'get_original_url',
            'get_thumbnail_url',
            'created_at',
            'updated_at',
        )


class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'id',
            'get_original_url',
            'get_thumbnail_url',
        )


class ImageSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = Image
        fields = "__all__"


class FolderSerializer(serializers.ModelSerializer):
    images_count = serializers.SerializerMethodField(read_only=True)

    def get_images_count(self, obj):
        return obj.image_set.count()

    class Meta:
        model = Folder
        fields = (
            'id',
            'name',
            'images_count',
            'created_at',
        )


class FolderDetailSerializer(serializers.ModelSerializer):
    images_count = serializers.SerializerMethodField(read_only=True)

    def get_images_count(self, obj):
        return obj.image_set.count()

    class Meta:
        model = Folder
        fields = (
            'name',
            'images_count',
            'created_at',
            'updated_at',
        )


class FolderImageSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images_count(self, obj):
        return obj.image_set.count()

    def get_images(self, obj):
        instance = obj.image_set.all()
        serializer = ImageListSerializer(instance, many=True)
        return serializer.data

    class Meta:
        model = Folder
        fields = (
            'name',
            'images',
            'created_at',
            'updated_at',
        )
