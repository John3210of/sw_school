from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import *
from .models import *

class IndexView(TemplateView):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        string = kwargs.get('string')
        if string:
            message = f'You entered: {string}'
        else:
            message = 'Welcome to myweb homepage'
        context = self.get_context_data(**kwargs)
        context['message'] = message
        return self.render_to_response(context)
    
class SetCookieView(APIView):
    def get(self, request):
        cookieSerializer = CookieSerializer(data={"message": "cookie created"})
        if cookieSerializer.is_valid():
            response_data = cookieSerializer.data
            response = Response(response_data, status=status.HTTP_200_OK)
            response.set_cookie('cookie', 'cookie_value', max_age=200)
        else:
            response_data = cookieSerializer.errors
            response = Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        return response

class GetCookieView(APIView):
    def get(self,request):
        cookie_value = request.COOKIES.get('cookie')
        if cookie_value:
            return Response({"message": f"The value of 'cookie' is: {cookie_value}"})
        else:
            return Response({"message": "No cookie found."})

class ItemView(APIView):
    def get(self,request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# class ItemViewSet(viewsets.ModelViewSet):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer