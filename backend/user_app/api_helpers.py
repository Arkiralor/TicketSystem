from user_app.serializers import UserGeneralSerializer
from django.contrib.auth.hashers import make_password

class UserRegistrationUtils:

    SUCCESS_CODE = 201
    FAILURE_CODE = 400

    @classmethod
    def handle_raw_user_data(cls, data:dict=None):
        resp = {}

        if not data.get('username') or not data.get('password') or not data.get('email'):
            resp['data'] = data
            resp['error'] = "'username', 'password' and 'email' are mandatory fields."
            resp['code'] = cls.FAILURE_CODE
            return resp

        if len(data.get('username')) == 0 or len(data.get('password')) == 0 or len(data.get('email')) == 0:
            resp['data'] = data
            resp['error'] = "'username', 'password' and 'email' are mandatory fields."
            resp['code'] = cls.FAILURE_CODE
            return resp

        data['password'] = make_password(data.get('password', ''))

        # Sanitizing request data
        if 'is_staff' in data.keys():
            data['is_staff'] = False
        if 'is_superuser' in data.keys():
            data['is_superuser'] = False
        
        deserialized = UserGeneralSerializer(data=data)

        if deserialized.is_valid():
            deserialized.save()
            resp['data'] = deserialized.data
            resp['error'] = None
            resp['code'] = cls.SUCCESS_CODE
            return resp
        else:
            resp['data'] = deserialized.data
            resp['error'] = str(deserialized.errors)
            resp['code'] = cls.FAILURE_CODE
            return resp