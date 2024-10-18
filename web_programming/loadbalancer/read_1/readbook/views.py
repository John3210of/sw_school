# readbook/views.py
from django.http import HttpResponse

def hello_world(request):
    ip = request.META.get('REMOTE_ADDR')
    port = request.META.get('SERVER_PORT')
    message = f"Hello, World! Your IP: {ip}, Port: {port}"
    return HttpResponse(message)
