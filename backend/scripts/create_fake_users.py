from faker import Faker
from secrets import token_hex, choice
from typing import List

from django.contrib.auth.hashers import make_password

from user_app.models import User, UserProfile
from user_app.serializers import UserGeneralSerializer, UserProfileInputSerializer

from scripts import logger


class FakeUserUtils:

    fake = Faker('en-US')
    REGNAL_NUMBERS = tuple(num for num in range(1, 22))
    DIGITS = tuple(j for j in range(0, 10))

    @classmethod
    def generate_fake_users(cls, count:int=0):
        user_objs = []

        for i in range(count):
            user_data = {
                "first_name": cls.fake.first_name(),
                "last_name": cls.fake.last_name(),
                "regnal_number": choice(cls.REGNAL_NUMBERS),
                "username": cls.fake.profile().get("username"),
                "password": make_password("Password123"),
                "email": cls.fake.profile().get("mail"),
                "phone_primary": cls.create_fake_phone(10)
            }

            deserialized = UserGeneralSerializer(data=user_data)
            if deserialized.is_valid():
                deserialized.save()
                user_objs.append(deserialized.instance)
            else:
                logger.warn(f"ERROR:\t{deserialized.errors}")
        
        profiles = cls.create_fake_user_profile(user_objs)
        return user_objs, profiles

    @classmethod
    def create_fake_phone(cls, lenght:int=0):
        first_digit_list = tuple(i for i in range(6, 10))
        digit_list = [
            str(choice(first_digit_list)),
        ]
        for j in range(lenght-1):
            digit_list.append(str(choice(cls.DIGITS)))

        return ''.join(digit_list)

    @classmethod
    def create_fake_user_profile(cls, users:List[User]=None):
        profiles = []
        for user in users:
            profile = UserProfile.objects.filter(user=user).first()
            profile_data = {
                "user": user.id,
                "headline": cls.fake.sentence(),
                "about_me": cls.fake.text(),
                "birthday": cls.fake.profile().get("birthdate"),
                "location": cls.fake.profile().get("residence")
            }

            deserialized = UserProfileInputSerializer(instance=profile, data=profile_data)
            if deserialized.is_valid():
                deserialized.save()
                profiles.append(deserialized.instance)
            else:
                logger.warn(f"ERROR:\t{deserialized.errors}")

        return profiles


def main():
    users, profiles = FakeUserUtils.generate_fake_users(4)
    logger.info(f"Users:\t{users}")
    logger.info(f"User Profiles:\t{profiles}")

if __name__=="__main__":
    main()

