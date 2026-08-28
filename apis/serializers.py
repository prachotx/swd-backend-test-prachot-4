from rest_framework import serializers
from .models import School
from .models import ClassRoom

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"
        
class ClassRoomSerializer(serializers.ModelSerializer):
    school = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = ClassRoom
        fields = "__all__"
