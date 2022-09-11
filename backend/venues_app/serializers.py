from rest_framework.serializers import ModelSerializer

from user_app.serializers import UserOutputSerializer
from venues_app.models import Venue, SeatSection, Seat, VenueEmployee


class VenueSerializer(ModelSerializer):

    class Meta:
        model = Venue
        fields = '__all__'


class SeatSectionInputSerializer(ModelSerializer):

    class Meta:
        model = SeatSection
        fields = '__all__'


class SeatSectionOutputSerializer(ModelSerializer):

    venue = VenueSerializer()

    class Meta:
        model = SeatSection
        fields = '__all__'


class SeatInputSerializer(ModelSerializer):

    class Meta:
        model = Seat
        fields = '__all__'


class SeatOutputSerializer(ModelSerializer):

    section = SeatSectionOutputSerializer()

    class Meta:
        model = Seat
        fields = '__all__'


class VenueEmployeeInputSerializer(ModelSerializer):

    class Meta:
        model = VenueEmployee
        fields = '__all__'


class VenueEmployeeOutputSerializer(ModelSerializer):
    employee = UserOutputSerializer()
    venue = VenueSerializer()

    class Meta:
        model = VenueEmployee
        fields = '__all__'
