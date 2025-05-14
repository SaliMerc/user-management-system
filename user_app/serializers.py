from django.contrib.auth import password_validation
from rest_framework import serializers
from .import models
from .models import MyUser

"""For viewing all the users in the system"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MyUser
        fields ='__all__'

"""For adding new users into the system"""
class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = models.MyUser
        fields ='__all__'

    def create(self, validated_data):
        user=MyUser.objects.create_user(**validated_data)
        return user

"""For changing the passwords of the users in the system"""
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, data):
        user = self.context.get('user')
        """checking if the new password is the same as the confirm password"""
        try:
            if data['new_password'] != data['confirm_password']:
                raise serializers.ValidationError({"New-passwords":"New passwords and confirm password need to match"})

            """Checking if the old password is correct"""
            if not user.check_password(data['old_password']):
                raise serializers.ValidationError({"Old password":"Old password is incorrect"})

            """Ensuring that the new password is not the same as the old password"""
            if data['new_password'] == data['old_password']:
                raise serializers.ValidationError({"Password-repeat":"New password cannot be the same as the old password"})

            """If the new passwords match and not the same as the old password, its validated and saved"""
            password_validation.validate_password(data['new_password'], user)
            return data
        except serializers.ValidationError as e:
            return {'error': e}

"""For updating user details in the system"""
class UpdateUserDetails(serializers.ModelSerializer):
    class Meta:
        model = models.MyUser
        fields=['first_name','last_name','display_name','phone_number']
