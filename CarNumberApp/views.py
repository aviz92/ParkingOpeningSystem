from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ExternalScripts.RefactorViewFunctions import ViewFunctions

from .models import CarNumber, CarNumberApartmentOwner
from .serializers import CarNumberSerializer, CarNumberSerializerSet, \
    CarNumberApartmentOwnerSerializer, CarNumberApartmentOwnerSerializerSet


class CarNumberView(generics.ListCreateAPIView):
    queryset = CarNumber.objects.all()
    serializer_class = CarNumberSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return ViewFunctions().get_function_view(request, CarNumber, CarNumberSerializer)

    def post(self, request, *args, **kwargs):
        return ViewFunctions().post_function(request, CarNumberSerializerSet)


class CarNumberViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarNumber.objects.all()
    serializer_class = CarNumberSerializerSet
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return ViewFunctions().get_function_viewset(request, CarNumber, CarNumberSerializer, **kwargs)

    def put(self, request, *args, **kwargs):
        return ViewFunctions().put_function(request, CarNumber, CarNumberSerializer, CarNumberSerializerSet, **kwargs)


class CarNumberApartmentOwnerView(generics.ListCreateAPIView):
    queryset = CarNumberApartmentOwner.objects.all()
    serializer_class = CarNumberApartmentOwnerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return ViewFunctions().get_function_view(request, CarNumberApartmentOwner, CarNumberApartmentOwnerSerializer)

    def post(self, request, *args, **kwargs):
        return ViewFunctions().post_function(request, CarNumberApartmentOwnerSerializerSet)


class CarNumberApartmentOwnerViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarNumberApartmentOwner.objects.all()
    serializer_class = CarNumberApartmentOwnerSerializerSet
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return ViewFunctions().get_function_viewset(request, CarNumberApartmentOwner, CarNumberApartmentOwnerSerializer, **kwargs)

    def put(self, request, *args, **kwargs):
        return ViewFunctions().put_function(request, CarNumberApartmentOwner, CarNumberApartmentOwnerSerializer, CarNumberApartmentOwnerSerializerSet, **kwargs)
