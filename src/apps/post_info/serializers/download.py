from rest_framework import serializers
from src.apps.post_info.models import Download
from src.apps.accounts.serializers import UserUsernameSerializer
from src.apps.project.serializers import ProjectApplicationSerializer


class DownloadListSerializer(serializers.ModelSerializer):
    
    project = ProjectApplicationSerializer()
    user = UserUsernameSerializer()

    class Meta:
        model = Download
        fields = (
            'id',
            'project',
            'user',
        )



class DownloadCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Download
        fields = ('project',)
