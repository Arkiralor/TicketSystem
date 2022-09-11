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
            resp['data'] = data
            resp['error'] = None
            resp['code'] = cls.SUCCESS_CODE
            return resp
        else:
            resp['data'] = data
            resp['error'] = str(deserialized.errors)
            resp['code'] = cls.FAILURE_CODE
            return resp

    
class UserModelUtils:
    """
    Class to hold methods to handle User Object details.
    """
    REGNAL_DICT = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI", 
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
        11: "XI",
        12: "XII",
        13: "XIII",
        14: "XIV",
        15: "XV",
        16: "XVI",
        17: "XVII",
        18: "XVIII",
        19: "XIX",
        20: "XX",
        21: "XXI"
    }

    @classmethod
    def translate_regnal_number(cls, regnal_number:int=None):
        if regnal_number in cls.REGNAL_DICT.keys():
            return cls.REGNAL_DICT[regnal_number], None
        else:
            resp = {
                "error": "Regnal number not supported."
            }
            return None, resp