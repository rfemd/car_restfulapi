from rest_framework import authentication, filters, permissions, viewsets

from api.authentication import TokenAuthentication

from .filters import CarFilterSet
from .models import Car
from .serializer import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = CarFilterSet
