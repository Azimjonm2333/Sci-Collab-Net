from rest_framework import serializers
from src.apps.post_info.models import Like
from src.apps.accounts.serializers import UserUsernameSerializer
from src.apps.project.serializers import ProjectApplicationSerializer


class LikeListSerializer(serializers.ModelSerializer):
    
    project = ProjectApplicationSerializer()
    user = UserUsernameSerializer()

    class Meta:
        model = Like
        fields = (
            'id',
            'project',
            'user',
        )



class LikeCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Like
        fields = ('project',)
