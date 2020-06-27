import django.contrib.auth.password_validation as validators
from django.contrib.auth import get_user_model
from django.core import exceptions

from rest_framework import serializers
from users.models import CustomUser

CustomUser = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    '''Serializes (format into JSON) and deserializes `CustomUser` model.'''
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'created_at',
            'is_staff',
            'is_active',
            'is_superuser',
        ]
        read_only_fields = ['id', 'is_superuser', 'is_staff', 'is_active']


class RegistrationSerializer(serializers.ModelSerializer):
    '''
    Serializes and deserializes `CustomUser` model to create new `user` object.
    Saves either as a `user` or `admin`
    '''
    confirm_password = serializers.CharField(
        max_length=500, 
        required=True, 
        write_only=True,
    )


    class Meta:
        model = CustomUser
        fields = [
            'email',
            'first_name',
            'last_name',
            'password',
            'confirm_password',
            'phone_number',
            'created_at',
            'is_staff',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }
    
    def validate(self, data):
        password = data.get('password')
        errors = dict()

        try:
            validators.validate_password(password)
        except exceptions.ValidationError as err:
            errors['password'] = list(err.messages)
        
        if errors:
            raise serializers.ValidationError(errors)
        return super(RegistrationSerializer, self).validate(data)
    
    def create(self, validated_data):
        if validated_data['is_staff'] == True:
            user = CustomUser.objects.create_superuser(
                email=validated_data['email'].lower(),
                password=validated_data['password'],
                first_name=validated_data['first_name'].title(),
                last_name=validated_data['last_name'].title(),
                phone_number=validated_data['phone_number'],
            )
        else:
            user = CustomUser.objects.create_user(
                    email=validated_data['email'].lower(),
                    password=validated_data['password'],
                    first_name=validated_data['first_name'].title(),
                    last_name=validated_data['last_name'].title(),
                    phone_number=validated_data['phone_number'],
            )
        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    '''Serializes and deserializes password.'''
    new_password = serializers.CharField(
        max_length=500, 
        required=True, 
        write_only=True,
    )
    confirm_password = serializers.CharField(
        max_length=500, 
        required=True, 
        write_only=True,
    )


    class Meta:
        model = CustomUser
        fields = [
            'password', 
            'new_password', 
            'confirm_password',
            ]
        extra_kwargs = {
            'password': {'write_only': True},
        }
    
    def validate(self, data):
        password = data.get('new_password')

        errors = dict()
        try:
            validators.validate_password(password=password)
        except exceptions.ValidationError as err:
            errors['new_password'] = list(err.messages)
        
        if errors:
            raise serializers.ValidationError(errors)
        return super(ChangePasswordSerializer, self).validate(data)

    def update(self, instance, validated_data):
        if 'new_password' in validated_data:
            instance.set_password(validated_data['new_password'])
            instance.save()
            return instance
