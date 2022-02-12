from django.db import router
from .api.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register('projects',ProjectViewSet)
router.register('issues',IssueViewSet)
router.register('user',UserViewSet)
router.register('invite',InviteViewSet)