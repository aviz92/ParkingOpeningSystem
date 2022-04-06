from rest_framework import status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import ipaddress

from ExternalScripts.RefactorViewFunctions import ViewFunctions
from .models import LeveledTree, Categories, Parameters, ParametersTree
from .serializers import LeveledTreeSerializer, LeveledTreeSerializerSet, \
    CategoriesSerializer, CategoriesSerializerSet, \
    ParametersSerializer, ParametersSerializerSet, \
    ParametersTreeSerializer, ParametersTreeSerializerSet


class LeveledTreeView(generics.ListCreateAPIView):
    queryset = LeveledTree.objects.all()
    # print(queryset)
    serializer_class = LeveledTreeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return ViewFunctions().get_function_view(request, LeveledTree, LeveledTreeSerializer)

    def post(self, request, *args, **kwargs):
        return ViewFunctions().post_function(request, LeveledTreeSerializerSet)


class LeveledTreeViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeveledTree.objects.all()
    serializer_class = LeveledTreeSerializerSet
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # permission_classes = (AllowAny,)

    # def get(self, request, *args, **kwargs):
    #     return ViewFunctions().get_function_viewset(request, LeveledTree, LeveledTreeSerializer, **kwargs)
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            print('pk not exist')
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            # queryset = LeveledTree.objects.all().filter(pk=kwargs.get('pk'))
            queryset = LeveledTree.objects.get(pk=kwargs.get('pk')).get_ancestors(include_self=True)
        except LeveledTree.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = LeveledTreeSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        return ViewFunctions().put_function(request, LeveledTree, LeveledTreeSerializer, LeveledTreeSerializerSet, **kwargs)


class LeveledTreeViewSet2(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeveledTree.objects.all()
    serializer_class = LeveledTreeSerializerSet
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return ViewFunctions().get_function_viewset(request, LeveledTree, LeveledTreeSerializer, **kwargs)

    def put(self, request, *args, **kwargs):
        return ViewFunctions().put_function(request, LeveledTree, LeveledTreeSerializer, LeveledTreeSerializerSet, **kwargs)


class LeveledTreeFullHierarchy(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeveledTree.objects.all()
    serializer_class = LeveledTreeSerializerSet
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        from mptt.templatetags.mptt_tags import cache_tree_children

        def recursive_node_to_dict(node):
            result = {
                'id': node.pk,
                'name': node.name,
                'level': node.level,
            }
            if children := [recursive_node_to_dict(c) for c in node.get_children()]:
                result['children'] = children
            return result

        root_nodes = cache_tree_children(LeveledTree.objects.all())
        dicts = []
        for n in root_nodes:
            dicts.append(recursive_node_to_dict(n))

        # import json
        # print(json.dumps(dicts, indent=4))
        return Response(dicts)


class LeveledTreeHierarchyWithoutTestPlan(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeveledTree.objects.all()
    serializer_class = LeveledTreeSerializerSet
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        from mptt.templatetags.mptt_tags import cache_tree_children

        def recursive_node_to_dict(node):
            result = {
                'id': node.pk,
                'name': node.name,
                'level': node.level,
            }
            if children := [
                recursive_node_to_dict(c)
                for c in node.get_children()
                if list(c.get_children())
            ]:
                result['children'] = children
            return result

        root_nodes = cache_tree_children(LeveledTree.objects.all())
        dicts = []
        for n in root_nodes:
            dicts.append(recursive_node_to_dict(n))

        # import json
        # print(json.dumps(dicts, indent=4))
        return Response(dicts)


class LeveledTreeViewByFilterAndFields(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeveledTree.objects.all()
    serializer_class = LeveledTreeSerializerSet
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            if request.query_params:
                list_fields = ['id', 'name']
                dict_fields = {}
                for k, v in request.query_params.items():
                    list_fields.append(k)
                    if v and v != '':
                        dict_fields[k] = v
                response = LeveledTree.objects.all().values(*list_fields).filter(**dict_fields)
                for resp_index, resp in enumerate(response, start=0):
                    for field in resp:
                        if type(response[resp_index][field]) in [
                            ipaddress.IPv4Address,
                            ipaddress.IPv6Address,
                        ]:
                            response[resp_index][field] = str(response[resp_index][field])
                return Response(response)
            else:
                queryset = LeveledTree.objects.all()
                serializer = LeveledTreeSerializer(queryset, context={'request': request}, many=True)
                return Response(serializer.data)
        except LeveledTree.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class LeveledTreeViewRoot(generics.ListCreateAPIView):
    queryset = LeveledTree.objects.all()
    # print(queryset)
    serializer_class = LeveledTreeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            queryset = LeveledTree.objects.all().filter(parent_id__isnull=True)
        except LeveledTree.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = LeveledTreeSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)


class CategoriesView(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    # print(queryset)
    serializer_class = CategoriesSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            # queryset = Categories.objects.all().filter(parent_id__isnull=True)
            queryset = Categories.objects.all()
        except Categories.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CategoriesSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CategoriesSerializerSet(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriesViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializerSet
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            print('pk not exist')
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            queryset = Categories.objects.all().filter(pk=kwargs.get('pk'))
        except Categories.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CategoriesSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            print('pk not exist')
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            queryset = Categories.objects.get(pk=pk)
        except Categories.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategoriesSerializerSet(queryset, context={'request': request}, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            serializer = CategoriesSerializer(Categories.objects.get(pk=serializer.data['id']),
                                              context={'request': request})
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ParametersView(generics.ListCreateAPIView):
    queryset = Parameters.objects.all()
    # print(queryset)
    serializer_class = ParametersSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            # queryset = Parameters.objects.all().filter(parent_id__isnull=True)
            queryset = Parameters.objects.all()
        except Parameters.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ParametersSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ParametersSerializerSet(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ParametersViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parameters.objects.all()
    serializer_class = ParametersSerializerSet
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            print('pk not exist')
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            queryset = Parameters.objects.all().filter(pk=kwargs.get('pk'))
        except Parameters.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ParametersSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            print('pk not exist')
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            queryset = Parameters.objects.get(pk=pk)
        except Parameters.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ParametersSerializerSet(queryset, context={'request': request}, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            serializer = ParametersSerializer(Parameters.objects.get(pk=serializer.data['id']),
                                              context={'request': request})
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ParametersTreeView(generics.ListCreateAPIView):
    queryset = ParametersTree.objects.all()
    # print(queryset)
    serializer_class = ParametersTreeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            # queryset = ParametersTree.objects.all().filter(parent_id__isnull=True)
            queryset = ParametersTree.objects.all()
        except ParametersTree.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ParametersTreeSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ParametersTreeSerializerSet(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ParametersTreeViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParametersTree.objects.all()
    serializer_class = ParametersTreeSerializerSet
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    # permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            print('pk not exist')
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            queryset = ParametersTree.objects.all().filter(pk=kwargs.get('pk'))
        except ParametersTree.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ParametersTreeSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            print('pk not exist')
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            queryset = ParametersTree.objects.get(pk=pk)
        except ParametersTree.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ParametersTreeSerializerSet(queryset, context={'request': request}, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            serializer = ParametersTreeSerializer(ParametersTree.objects.get(pk=serializer.data['id']),
                                                  context={'request': request})
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
