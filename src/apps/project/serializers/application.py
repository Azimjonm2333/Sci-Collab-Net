from rest_framework import serializers
from src.apps.project.models import Application
from src.apps.accounts.serializers import UserListSerializer


class ApplicationListSerializer(serializers.ModelSerializer):

    user = UserListSerializer()

    class Meta:
        model = Application
        fields = (
            'id',
            'project',
            'user',
            'description',
        )



class ApplicationCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = (
            'project',
            'description',
        )

class ApplicationApproveSerializer(serializers.ModelSerializer):

    applications = serializers.ListField(child=serializers.IntegerField())

    class Meta:
        model = Application
        fields = (
            'applications',
        )

    def validate_applications(self, value):
        """
        Custom validation for the 'applications' field.

        Args:
            value (list): The value of the 'applications' field.

        Returns:
            list: The validated 'applications' value if it passes validation.

        Raises:
            serializers.ValidationError: If validation fails.
        """
        applications = []
        for application_id in value:
            try:
                application = Application.objects.get(pk=application_id)
                applications.append(application)
            except Application.DoesNotExist:
                raise serializers.ValidationError(f"Application with ID {application_id} does not exist.")
        return applications
