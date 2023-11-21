from rest_framework import generics,status
from rest_framework.response import Response
from .models import User, Service
from .serializer import UserSerializer, ServiceSerializer
from django.http import HttpResponse

# Create your views here.


def default_view(request):
    return HttpResponse("Welcome to the Ordain Jango Server!")


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        # Customize the response format
        response_data = {
            'status': status.HTTP_201_CREATED,
            'message': 'Successfully created user',
            'data': serializer.data
        }

        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)


class UserDetailView (generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        # Customize the response format
        response_data = {
            'status': status.HTTP_201_CREATED,
            'message': 'Successfully created service',
            'data': serializer.data
        }

        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)


class ServiceListCreateView (generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetailView (generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
