from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ExternalScripts.RefactorViewFunctions import ViewFunctions

from .models import ApartmentOwner
from .serializers import ApartmentOwnerSerializer, ApartmentOwnerSerializerSet


class ApartmentOwnerView(generics.ListCreateAPIView):
    queryset = ApartmentOwner.objects.all()
    serializer_class = ApartmentOwnerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return ViewFunctions().get_function_view(request, ApartmentOwner, ApartmentOwnerSerializer)

    def post(self, request, *args, **kwargs):
        return ViewFunctions().post_function(request, ApartmentOwnerSerializerSet)


class ApartmentOwnerViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApartmentOwner.objects.all()
    serializer_class = ApartmentOwnerSerializerSet
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return ViewFunctions().get_function_viewset(request, ApartmentOwner, ApartmentOwnerSerializer, **kwargs)

    def put(self, request, *args, **kwargs):
        return ViewFunctions().put_function(request, ApartmentOwner, ApartmentOwnerSerializer, ApartmentOwnerSerializerSet, **kwargs)
