from dataclasses import field
from typing_extensions import Required
from rest_framework import serializers
from issues.models import *



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')


class ProjectsSerializer(serializers.ModelSerializer):
    user_team = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),many=True,
        allow_null = True, read_only = False, required = False
    )
    class Meta: 
        model = Projects
        fields = ('id','proj_name','wiki','datetime','user_team')


class IssueSerializer(serializers.ModelSerializer):
    composer = serializers.PrimaryKeyRelatedField(read_only=True)
    project = serializers.PrimaryKeyRelatedField(
        queryset = Projects.objects.all(), required = True
    )
    class Meta:
        model = Issues
        fields = ('id','project','heading','description','composer','priority','tags','status','datetime')
        read_only_fields = ('datetime','composer')
