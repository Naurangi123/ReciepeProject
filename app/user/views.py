
from rest_framework import (generics,authentication,permissions)
from user.serializers import (UserSerializer,AuthTokenSerializer)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class CreateUserView(generics.CreateAPIView):
    
    serializer_class=UserSerializer
    
    
class CreateTokenView(ObtainAuthToken):
    serializer_class=AuthTokenSerializer
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES
    
    
# class ManageUserView(generics.RetrieveUpdateAPIView):
#     serializer_class=UserSerializer
#     authentication_classes=[authentication.TokenAuthentication]
#     pagination_class=[permissions.IsAuthenticated]
    
#     def get_object(self):
#         return self.request.user
    
    
class ManageUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)