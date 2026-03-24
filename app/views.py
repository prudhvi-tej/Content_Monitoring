from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from .services import run_scan
from django.utils import timezone

@api_view(['POST'])
def add_keyword(request):
    serializer = KeywordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['POST'])
def scan(request):
    run_scan()
    return Response({"msg": "scan done"})


@api_view(['GET'])
def get_flags(request):
    data = Flag.objects.all()
    return Response(FlagSerializer(data, many=True).data)


@api_view(['PATCH'])
def update_flag(request, pk):
    flag = Flag.objects.get(id=pk)
    flag.status = request.data.get('status')
    flag.reviewed_at = timezone.now()
    flag.save()
    return Response({"msg": "updated"})

@api_view(['GET'])
def home(request):
    return Response({"message": "API is running"})