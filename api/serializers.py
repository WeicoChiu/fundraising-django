from django.db.models import fields
from rest_framework import serializers
from project.models import Category, Project, ProjectSupport

class ProjectSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSupport
        exclude = ['project']

class ProjectSerializer(serializers.ModelSerializer):
    projectsupport = ProjectSupportSerializer()
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = [
            'projectowner',
            'status',
            'total_donate',
            'count_donate',
        ]

    def create(self, validated_data):
        support_data = validated_data.pop('projectsupport')
        project = Project.objects.create(**validated_data)
        projectsupport = ProjectSupport.objects.create(project=project, **support_data)
        projectsupport.project.status = 'published'
        projectsupport.save()
        return project

class ProjectDetailSerializer(serializers.ModelSerializer):
    projectsupport = ProjectSupportSerializer(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = [
            'projectowner',
            'status',
            'total_donate',
            'count_donate',
        ]

    def update(self, instance, validated_data):
        # support_data = validated_data.pop('projectsupport')
        instance.category = validated_data.get('category', instance.category)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.save()

        # projectsupport = instance.projectsupport
        # projectsupport.name = support_data.get('name', projectsupport.name)
        # projectsupport.description = support_data.get('description', projectsupport.description)
        # projectsupport.price = support_data.get('price', projectsupport.price)
        # projectsupport.save()

        return instance

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class CategoryClassifySerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'