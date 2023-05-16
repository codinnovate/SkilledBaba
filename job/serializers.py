from rest_framework import serializers

from .models import *


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('__all__')

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Job
        depth = 1

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Company

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Blog
        depth = 1

class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Scholarship
        depth = 1

