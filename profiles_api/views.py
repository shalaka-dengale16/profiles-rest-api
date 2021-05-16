from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import serializers
from rest_framework import status

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
