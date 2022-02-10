from email import message
from urllib import request

from hamcrest import contains
from ..models import *
from .serializer import *
import urllib.request
from rest_framework import viewsets
from rest_framework import generics,permissions
from rest_framework.permissions import IsAdminUser,IsAuthenticated,BasePermission,DjangoModelPermissionsOrAnonReadOnly,DjangoModelPermissions

###
### All user related 
###
class UserViewPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        userid = view.kwargs.get('pk')
        return int(request.user.id) == int(userid)

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [UserViewPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer


###
### All Project related
###

class ProjectUserTeamPermission(BasePermission):
    message = 'Not accessible'
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            a = request.user.projects.all()
            return obj in a 

class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated&ProjectUserTeamPermission]
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


###
### All issue related
### 

class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issues.objects.all()
    serializer_class = IssueSerializer