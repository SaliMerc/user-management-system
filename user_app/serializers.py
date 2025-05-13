from django.contrib.auth import password_validation
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .import models
from .models import MyUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MyUser
        fields ='__all__'

class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = models.MyUser
        fields ='__all__'

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = MyUser.objects.create_user(password=password, **validated_data)
        user.set_password(password)
        user.save()
        return user

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, data):
        user = self.context.get('user')
        # checking if the new password is the same as the confirm password
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({"New-passwords":"New passwords must be same"})

        # checking if the old password is correct
        if not user.check_password(data['old_password']):
            raise serializers.ValidationError({"Old password":"Old password is incorrect"})

        #ensures that the new password is not the same as the old password
        if data['new_password'] == data['old_password']:
            raise serializers.ValidationError({"Password-repeat":"New password cannot be the same as the old password"})

        # if the new passwords match and not the same as the old password, its validated and saves
        password_validation.validate_password(data['new_password'], user)

        return data

class UpdateUserDetails(serializers.ModelSerializer):
    class Meta:
        model = models.MyUser
        fields=['first_name','last_name','display_name','phone_number']
