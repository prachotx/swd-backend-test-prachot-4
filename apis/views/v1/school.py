from apis.models import School
from apis.serializers import SchoolSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class SchoolViewSet(APIView):
    def get(self, request):
        name = request.query_params.get("name")
        
        if name:
            schools = School.objects.filter(name__icontains=name)
        else:
            schools = School.objects.all()
        
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)