from rest_framework.views import APIView
from apis.serializers import ClassRoomSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from apis.models import School
from apis.models import ClassRoom

class ClassRoomViewSet(APIView):
    def get(self, request):
        school_id = request.query_params.get("school_id")
        
        if school_id:
            school = get_object_or_404(School, id=school_id)
            class_rooms = ClassRoom.objects.filter(school=school)
        else:
            class_rooms = ClassRoom.objects.all()
        
        serializer = ClassRoomSerializer(class_rooms, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        school_id = request.query_params.get("school_id")
        school = get_object_or_404(School, id=school_id)

        serializer = ClassRoomSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        class_room = serializer.save(school=school)

        return Response(
            ClassRoomSerializer(class_room).data,
            status=status.HTTP_201_CREATED
        )