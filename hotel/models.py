from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category

class Bedtype(models.Model):
    bed_type = models.CharField(max_length=200)

    def __str__(self):
        return self.bed_type

class Guestnum(models.Model):
    guest_number = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.guest_number}'

class Apartment(models.Model):
    room_name = models.CharField(max_length=200)
    room_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    bed_type = models.ForeignKey(Bedtype, on_delete=models.CASCADE)
    balcony = models.BooleanField(default=False)
    max_number_of_guests = models.ForeignKey(Guestnum, on_delete=models.CASCADE)
    cost_per_night = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        if self.balcony == True:
             return f'{self.room_name} - {self.room_category} apartment with {self.bed_type} bed with balcony'
        else:
            return f'{self.room_name} - {self.room_category} apartment with {self.bed_type} bed'

class Booking(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=50, blank=True)
    check_in = models.DateField()
    check_out = models.DateField()
    extra_bed = models.BooleanField(default=False)
    total_cost = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'Check-in: {self.check_in} Check-out: {self.check_out} apartment: {self.apartment} total: {self.total_cost}'


