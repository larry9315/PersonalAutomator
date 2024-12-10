from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, World!"})

@api_view(['GET'])
def another_endpoint(request):
    return Response({"data": "This is another endpoint!"})