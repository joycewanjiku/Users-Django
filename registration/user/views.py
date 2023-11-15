from rest_framework import viewsets
from .serializers import UserSerializer, WasteCollectorSerializer, WasteRecyclerSerializer
from .models import User, WasteCollector, WasteRecycler

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class WasteCollectorViewSet(viewsets.ModelViewSet):
    queryset = WasteCollector.objects.all()
    serializer_class = WasteCollectorSerializer

class WasteRecyclerViewSet(viewsets.ModelViewSet):
    queryset = WasteRecycler.objects.all()
    serializer_class = WasteRecyclerSerializer
