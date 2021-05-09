from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApi(APIView):
    def get(self,request,format=None):
        an_api=[
        'Requests passed to the handler methods will be REST framework Request instances, not Django HttpRequest instances.',
        'Logic for urls ',
        ]

        return Response({'Message':'Hello','an_api':an_api})
