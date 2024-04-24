from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from core.auth.serializers import RegisterSerializer
from core.auth.permissions import UserPermission

class RegisterViewSet(ViewSet):
    serializer_class = RegisterSerializer
    permission_classes = [ AllowAny]
    http_method_names = ['post']

    def create(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        response = {
            "user":serializer.data,
            "access":f"{refresh.access_token}",
            "refresh":f"{refresh}"
        }
        return Response(response,status=status.HTTP_201_CREATED)

