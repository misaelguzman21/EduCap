from django.contrib.auth.models import User
from django.db import models
from rest_framework import fields, serializers
from accounts.models import UserModel, Estudiante


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = [
            'id',
            'email',
            'username',
            'password',
            'first_name',
            'last_name',
        ]

    def create(self, validated_data):
        password = validated_data["password"]
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ['id', 'user', 'edad']

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.user = validated_data["user"]
        instance.save()
        return instance


class getStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'


class getUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['email', 'first_name', 'last_name']
