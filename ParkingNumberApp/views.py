from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ExternalScripts.RefactorViewFunctions import ViewFunctions

from .models import ParkingNumber
from .serializers import ParkingNumberSerializer, ParkingNumberSerializerSet


class ParkingNumberView(generics.ListCreateAPIView):
    queryset = ParkingNumber.objects.all()
    serializer_class = ParkingNumberSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return ViewFunctions().get_function_view(request, ParkingNumber, ParkingNumberSerializer)

    def post(self, request, *args, **kwargs):
        return ViewFunctions().post_function(request, ParkingNumberSerializerSet)


class ParkingNumberViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParkingNumber.objects.all()
    serializer_class = ParkingNumberSerializerSet
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return ViewFunctions().get_function_viewset(request, ParkingNumber, ParkingNumberSerializer, **kwargs)

    def put(self, request, *args, **kwargs):
        return ViewFunctions().put_function(request, ParkingNumber, ParkingNumberSerializer, ParkingNumberSerializerSet, **kwargs)
