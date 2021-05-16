from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import serializers
from rest_framework import status
from rest_framework import viewsets

# Create your views here.
class HelloApi(APIView):
    serializer_class=serializers.HelloSerializer
    def get(self,request,format=None):
        an_api=[
        'Requests passed to the handler methods will be REST framework Request instances, not Django HttpRequest instances.',
        'Logic for urls ',
        ]

        return Response({'Message':'Hello','an_api':an_api})


    def post(self,request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response(
            {'message':message})

        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """Handle  a partial update of an object"""
        return Response({'message':'PATCH'})

    def delete(self,request,pk=None):
        """Handle a delete of an object"""
        return Response({'message':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    serializer_class=serializers.HelloSerializer
    def list(self,request):
        """Return a hello message"""
        a_viewset=[
        'Uses actions (list,create,retrieve,update,partial_update)',
        'Automatically maps to URLs using Routers',
        'Provides more functionality with less code',
        ]

        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self,request):
        """Create  a new hello message """
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})

        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """Handle getting an object by its id"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handle removing an object"""
        return Response({'http_method':'DELETE'})
