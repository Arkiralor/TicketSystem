from rest_framework.serializers import ModelSerializer

from user_app.models import User, UserProfile

class UserGeneralSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

class UserAdminSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "regnal_number",
            "username",
            "email",
            "phone_primary",
            "unsuccessful_login_attempts",
            "blocked_until",
            "slug",
            "is_active",
            "date_joined",
            "date_modified"
        )

class UserOutputSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "regnal_number",
            "username",
            "email",
            "slug",
            "date_joined",
        )


class UserProfileInputSerializer(ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileOutputSerializer(ModelSerializer):
    user = UserOutputSerializer()
    class Meta:
        model = UserProfile
        fields = '__all__'