from rest_framework import status
from rest_framework.response import Response
import ipaddress


class ViewFunctions:
    @staticmethod
    def post_function(request, model_serializer_set_class):
        serializer = model_serializer_set_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def put_function(request, model_class, model_serializer_class, model_serializer_set_class, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            print('pk not exist')
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            queryset = model_class.objects.get(pk=pk)
        except model_class.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = model_serializer_set_class(queryset, context={'request': request}, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            serializer = model_serializer_class(model_class.objects.get(pk=serializer.data['id']), context={'request': request})
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get_function_view(request, model_class, model_serializer_class):
        try:
            if request.query_params:
                list_fields = ['id', 'name']
                dict_fields = {}
                for k, v in request.query_params.items():
                    list_fields.append(k)
                    if v and v != '':
                        dict_fields.update({k: v})
                if '__all__' in list_fields:
                    response = model_class.objects.all().filter(**dict_fields)
                    serializer = model_serializer_class(response, context={'request': request}, many=True)
                    return Response(serializer.data)
                else:
                    response = model_class.objects.all().values(*list_fields).filter(**dict_fields)
                for resp_index, resp in enumerate(response, start=0):
                    for field in resp:
                        if type(response[resp_index][field]) in [ipaddress.IPv4Address, ipaddress.IPv6Address]:
                            response[resp_index][field] = str(response[resp_index][field])
                return Response(response)
            else:
                queryset = model_class.objects.all()
                serializer = model_serializer_class(queryset, context={'request': request}, many=True)
                return Response(serializer.data)
        except model_class.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def get_function_viewset(request, model_class, model_serializer_class, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            print('pk not exist')
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            if request.query_params:
                list_fields = ['id', 'name']
                dict_fields = {}
                for k, v in request.query_params.items():
                    list_fields.append(k)
                    if v and v != '':
                        dict_fields.update({k: v})
                if '__all__' in list_fields:
                    response = model_class.objects.all().filter(**dict_fields)
                    serializer = model_serializer_class(response, context={'request': request}, many=True)
                    return Response(serializer.data)
                else:
                    response = model_class.objects.all().values(*list_fields).filter(**dict_fields)
                for resp_index, resp in enumerate(response, start=0):
                    for field in resp:
                        if type(response[resp_index][field]) in [ipaddress.IPv4Address, ipaddress.IPv6Address]:
                            response[resp_index][field] = str(response[resp_index][field])
                return Response(response)
            else:
                queryset = model_class.objects.all().filter(pk=kwargs.get('pk'))
                serializer = model_serializer_class(queryset, context={'request': request}, many=True)
                return Response(serializer.data)
        except model_class.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
