from rest_framework import generics
from auth_app.models import User
from auth_app.serializers import RegisterSerializer



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer