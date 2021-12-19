from django.db.models import query
from rest_framework import parsers
from rest_framework.serializers import Serializer
from project.models import Category, Project, ProjectOwner
from api.serializers import CategoryClassifySerializer, CategorySerializer, ProjectDetailSerializer, ProjectSerializer, ProjectSupportSerializer
from rest_framework import permissions, serializers, status, generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser, MultiPartParser
from .permission import AdminCreateOrModeifyPermission, CreatePermission, ProjectOwnerPermission

class ListCategory(generics.ListCreateAPIView):
    permission_classes = [AdminCreateOrModeifyPermission]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [AdminCreateOrModeifyPermission]
    serializer_class = CategoryClassifySerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Category.objects.filter(pk=pk)

class ListProject(generics.ListCreateAPIView):
    permission_classes = [CreatePermission]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        projectowner = ProjectOwner.objects.get(user = self.request.user)

        serializer.save(
            projectowner=projectowner,
        )

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [ProjectOwnerPermission]
    serializer_class = ProjectDetailSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Project.objects.filter(pk=pk)
