from rest_framework import serializers
from src.apps.post_info.models import View
from src.apps.accounts.serializers import UserUsernameSerializer
from src.apps.project.serializers import ProjectApplicationSerializer


class ViewListSerializer(serializers.ModelSerializer):
    
    project = ProjectApplicationSerializer()
    user = UserUsernameSerializer()

    class Meta:
        model = View
        fields = (
            'id',
            'project',
            'user',
        )



class ViewCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = View
        fields = ('project',)
