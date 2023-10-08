from rest_framework import serializers
from src.apps.post_info.models import Comment
from src.apps.accounts.serializers import UserUsernameSerializer
from src.apps.project.serializers import ProjectApplicationSerializer



class NestedCommentSerializer(serializers.ModelSerializer):
    """ Nested Comment serializer """
    
    user = UserUsernameSerializer()
    childrens = serializers.SerializerMethodField()

    def get_childrens(self, obj):
        children_categories = Comment.objects.filter(parent=obj)
        serializer = NestedCommentSerializer(children_categories, many=True)
        return serializer.data

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'message',
            'childrens',
        )



class CommentCreateSerializer(serializers.ModelSerializer):
    
    def validate(self, value):
        parent = value.get('parent', False)
        if parent:
            if parent.project != value.get('project'):
                raise serializers.ValidationError("Комментарий не найден")
        return value

    def create(self, validated_data: dict):
        validated_data['user'] = self.context['request'].user
        instance = super().create(validated_data)

        return instance

    class Meta:
        model = Comment
        fields = (
            'project',
            'message',
            'parent'
        )