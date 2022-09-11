from django.db.models import Model, UUIDField, CharField, PositiveIntegerField, DateField, DateTimeField, TextField, SlugField, DecimalField, \
    FileField, ImageField, \
    ForeignKey, CASCADE

from django.template.defaultfilters import slugify

from venues_app.model_choices import SeatChoice, EmployeeChoice
from user_app.models import User

import uuid


class Venue(Model):
    id = UUIDField(
        primary_key=True,
        editable=False,
        unique=True,
        default=uuid.uuid4
    )

    name = CharField(max_length=256)
    description = TextField()
    max_capacity = PositiveIntegerField(default=100)

    logo = ImageField(upload_to='images/logos/venues/', blank=True, null=True)
    proof_of_registration = FileField(
        upload_to='documents/venues/registration_files/', blank=True, null=True)

    owner = ForeignKey(User, on_delete=CASCADE)

    established = DateField(blank=True, null=True)

    add_line_1 = CharField(max_length=128, blank=True, null=True)
    add_line_2 = CharField(max_length=128, blank=True, null=True)
    city = CharField(max_length=32)
    state = CharField(max_length=32, blank=True, null=True)
    country = CharField(max_length=32, blank=True, null=True)
    postal_code = CharField(max_length=10, blank=True, null=True)

    slug = SlugField(unique=True, blank=True, null=True)

    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.city}"

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        self.city = self.city.title()
        self.state = self.state.title()
        self.country = self.country.title()

        if not self.established:
            self.established = self.created.date

        self.slug = slugify(f"{self.name}, {self.city}")

        super(Venue, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('name', 'owner', 'established',
                           'city', 'state', 'country')
        verbose_name = 'Event Venue'
        verbose_name_plural = 'Event Venues'
        ordering = ('name', 'established')


class SeatSection(Model):
    id = UUIDField(
        primary_key=True,
        editable=False,
        unique=True,
        default=uuid.uuid4
    )

    name = CharField(max_length=32)
    venue = ForeignKey(Venue, on_delete=CASCADE)
    total_seats = PositiveIntegerField(default=1)
    price_per_seat = DecimalField(
        max_digits=7, decimal_places=2, default=250.00)

    slug = SlugField(unique=True, blank=True, null=True)

    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.venue}"

    def save(self, *args, **kwargs):
        self.name = self.name.title()

        self.slug = slugify(f"{self.name}, {self.venue}")

        super(SeatSection, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('name', 'venue')
        verbose_name = 'Seating Section'
        verbose_name_plural = 'Seating Sections'
        ordering = ('venue', 'name', '-created')


class Seat(Model):
    id = UUIDField(
        primary_key=True,
        editable=False,
        unique=True,
        default=uuid.uuid4
    )

    seat_number = CharField(max_length=16)
    section = ForeignKey(SeatSection, on_delete=CASCADE)
    status = CharField(
        max_length=16, choices=SeatChoice.STATUS_CHOICES, default=SeatChoice.available)
    price = DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    slug = SlugField(unique=True, blank=True, null=True)

    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.seat_number}, {self.section}"

    def save(self, *args, **kwargs):
        self.seat_number = self.seat_number.upper()

        if not self.price:
            self.price = self.section.price_per_seat

        self.slug = slugify(f"{self.seat_number}, {self.section}")

        super(Seat, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('seat_number', 'section')
        verbose_name = 'Seat'
        verbose_name_plural = 'Seats'
        ordering = ('section', 'seat_number')


class VenueEmployee(Model):
    id = UUIDField(
        primary_key=True,
        editable=False,
        unique=True,
        default=uuid.uuid4
    )

    employee = ForeignKey(User, on_delete=CASCADE)
    venue = ForeignKey(Venue, on_delete=CASCADE)
    employee_type = CharField(
        max_length=32, choices=EmployeeChoice.TYPE_CHOICES, default=EmployeeChoice.steward_rank)
    contract_type = CharField(
        max_length=32, choices=EmployeeChoice.CONTRACT_CHOICES, default=EmployeeChoice.permanent)
    valid_till = DateField(blank=True, null=True)

    slug = SlugField(unique=True, blank=True, null=True)

    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name}"

    def save(self, *args, **kwargs):
        if self.contract_type == EmployeeChoice.permanent:
            self.valid_till = None

        self.slug = slugify(
            f"{self.employee} ({self.employee_type}), {self.venue}")

        super(VenueEmployee, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('employee', 'venue')
        verbose_name = 'Venue Employee'
        verbose_name_plural = 'Venue Employees'
        ordering = ('venue', 'employee')
