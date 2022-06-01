from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView

from .models import Party

from .serializers import PartySerializer

from rest_framework.permissions import IsAuthenticated

# Create your views here.


class PartyListView(ListCreateAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    permission_classes = (IsAuthenticated,)  # tuple!!
