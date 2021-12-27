from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import JobSerializer
from .models import Job

class JobViewSet(ReadOnlyModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()