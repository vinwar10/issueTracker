from dataclasses import field
import email
from importlib.metadata import files
from os import read
from typing_extensions import Required
from rest_framework import serializers
from issues.models import *


###
### All Register related
###
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','password')
        extra_kwargs = {'password':{'write_only':True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user




MIN_LENGTH = 8
###
### USER SERIALIZER
###
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')



###
### PROJECT SERIALIZER
###
class ProjectsSerializer(serializers.ModelSerializer):
    user_team = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.all(),many=True,
        allow_null = True, read_only = False, required = False
    )
    class Meta: 
        model = Projects
        fields = ('id','proj_name','wiki','datetime','user_team')
        read_only_fields = ('datetime',)




###
### ISSUE SERIALIZER
###
class IssueSerializer(serializers.ModelSerializer):
    composer = serializers.PrimaryKeyRelatedField(read_only=True)
    project = serializers.PrimaryKeyRelatedField(
        queryset = Projects.objects.all(), required = True
    )
    composer_username = serializers.SerializerMethodField(read_only=True)
    
    def get_composer_username(self, obj):
        return obj.composer.username

    class Meta:
        model = Issues
        fields = ('id','project','heading','description','composer','composer_username','priority','tags','status','datetime')
        read_only_fields = ('datetime','composer')



###
### INVITE SERIALIZER
###
class InviteSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(
        queryset = Projects.objects.all(), required = True
    )
    invitee = serializers.PrimaryKeyRelatedField( 
        queryset = User.objects.all(), required = True
    )
    class Meta:
        model = Invite
        fields = ('id','project','invitee','operation','url')
        read_only_fields = ('url','slug')





