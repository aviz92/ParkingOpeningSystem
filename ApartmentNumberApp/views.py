from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ExternalScripts.RefactorViewFunctions import ViewFunctions

from .models import ApartmentNumber, ApartmentNumberApartmentOwner
from .serializers import ApartmentNumberSerializer, ApartmentNumberSerializerSet, \
    ApartmentNumberApartmentOwnerSerializer, ApartmentNumberApartmentOwnerSerializerSet


class ApartmentNumberView(generics.ListCreateAPIView):
    queryset = ApartmentNumber.objects.all()
    serializer_class = ApartmentNumberSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return ViewFunctions().get_function_view(request, ApartmentNumber, ApartmentNumberSerializer)

    def post(self, request, *args, **kwargs):
        return ViewFunctions().post_function(request, ApartmentNumberSerializerSet)


class ApartmentNumberViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApartmentNumber.objects.all()
    serializer_class = ApartmentNumberSerializerSet
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return ViewFunctions().get_function_viewset(request, ApartmentNumber, ApartmentNumberSerializer, **kwargs)

    def put(self, request, *args, **kwargs):
        return ViewFunctions().put_function(request, ApartmentNumber, ApartmentNumberSerializer, ApartmentNumberSerializerSet, **kwargs)


class ApartmentNumberApartmentOwnerView(generics.ListCreateAPIView):
    queryset = ApartmentNumberApartmentOwner.objects.all()
    serializer_class = ApartmentNumberApartmentOwnerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return ViewFunctions().get_function_view(request, ApartmentNumberApartmentOwner, ApartmentNumberApartmentOwnerSerializer)

    def post(self, request, *args, **kwargs):
        return ViewFunctions().post_function(request, ApartmentNumberApartmentOwnerSerializerSet)


class ApartmentNumberApartmentOwnerViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApartmentNumberApartmentOwner.objects.all()
    serializer_class = ApartmentNumberApartmentOwnerSerializerSet
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return ViewFunctions().get_function_viewset(request, ApartmentNumberApartmentOwner, ApartmentNumberApartmentOwnerSerializer, **kwargs)

    def put(self, request, *args, **kwargs):
        return ViewFunctions().put_function(request, ApartmentNumberApartmentOwner, ApartmentNumberApartmentOwnerSerializer, ApartmentNumberApartmentOwnerSerializerSet, **kwargs)
