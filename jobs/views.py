from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import JobSerializer, ApplicationSerializer
from .models import Job
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class JobViewSet(ReadOnlyModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_application(request, pk):
    # Messageboard to post to
    job = get_object_or_404(Job, pk=pk)

    serializer = ApplicationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # here you can pass data without validation directly to the save method
    serializer.save(job=job)
    return Response(serializer.data)