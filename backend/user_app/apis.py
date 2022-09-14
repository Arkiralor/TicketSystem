from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, AllowAny

from user_app.api_helpers import UserRegistrationUtils

class RegisterUserAPI(APIView):
    
    SUCCESS_CODE = 201
    FAILURE_CODE = 400

    def post(self, request, *args, **kwargs):
        data = request.data

        register = UserRegistrationUtils.handle_raw_user_data(data=data)

        if not register.get('code', 400) is self.SUCCESS_CODE:
            return Response(
                register,
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            register,
            status=status.HTTP_200_OK
        )