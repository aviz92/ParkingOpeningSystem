from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ExternalScripts.RefactorViewFunctions import ViewFunctions

from .models import MotorcycleNumber, MotorcycleNumberApartmentOwner
from .serializers import MotorcycleNumberSerializer, MotorcycleNumberSerializerSet, \
    MotorcycleNumberApartmentOwnerSerializer, MotorcycleNumberApartmentOwnerSerializerSet


class MotorcycleNumberView(generics.ListCreateAPIView):
    queryset = MotorcycleNumber.objects.all()
    serializer_class = MotorcycleNumberSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return ViewFunctions().get_function_view(request, MotorcycleNumber, MotorcycleNumberSerializer)

    def post(self, request, *args, **kwargs):
        return ViewFunctions().post_function(request, MotorcycleNumberSerializerSet)


class MotorcycleNumberViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = MotorcycleNumber.objects.all()
    serializer_class = MotorcycleNumberSerializerSet
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return ViewFunctions().get_function_viewset(request, MotorcycleNumber, MotorcycleNumberSerializer, **kwargs)

    def put(self, request, *args, **kwargs):
        return ViewFunctions().put_function(request, MotorcycleNumber, MotorcycleNumberSerializer, MotorcycleNumberSerializerSet, **kwargs)


class MotorcycleNumberApartmentOwnerView(generics.ListCreateAPIView):
    queryset = MotorcycleNumberApartmentOwner.objects.all()
    serializer_class = MotorcycleNumberApartmentOwnerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return ViewFunctions().get_function_view(request, MotorcycleNumberApartmentOwner, MotorcycleNumberApartmentOwnerSerializer)

    def post(self, request, *args, **kwargs):
        return ViewFunctions().post_function(request, MotorcycleNumberApartmentOwnerSerializerSet)


class MotorcycleNumberApartmentOwnerViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = MotorcycleNumberApartmentOwner.objects.all()
    serializer_class = MotorcycleNumberApartmentOwnerSerializerSet
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return ViewFunctions().get_function_viewset(request, MotorcycleNumberApartmentOwner, MotorcycleNumberApartmentOwnerSerializer, **kwargs)

    def put(self, request, *args, **kwargs):
        return ViewFunctions().put_function(request, MotorcycleNumberApartmentOwner, MotorcycleNumberApartmentOwnerSerializer, MotorcycleNumberApartmentOwnerSerializerSet, **kwargs)
