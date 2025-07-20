from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from django.utils import timezone

class Movie(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="movies/")
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    cast = models.TextField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Theater(models.Model):
    name = models.CharField(max_length=255)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='theaters')
    time = models.DateTimeField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('10.00'))

    def __str__(self):
        return f'{self.name} - {self.movie.name} at {self.time}'

    def get_current_price(self):
        now = timezone.now()
        time_to_show = self.time - now
        days_to_show = time_to_show.days

        if days_to_show > 7:
            time_multiplier = Decimal('1.0')
        elif days_to_show > 2:
            time_multiplier = Decimal('0.9')
        else:
            time_multiplier = Decimal('0.8')

        total_seats = self.seats.count()
        booked_seats = self.seats.filter(is_booked=True).count()

        if total_seats == 0:
            seat_multiplier = Decimal('1.0')
        else:
            booked_percentage = booked_seats / total_seats
            if booked_percentage < 0.5:
                seat_multiplier = Decimal('1.0')
            elif booked_percentage < 0.8:
                seat_multiplier = Decimal('1.2')
            else:
                seat_multiplier = Decimal('1.5')

        current_price = self.base_price * seat_multiplier * time_multiplier
        return current_price

class Seat(models.Model):
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, related_name='seats')
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.seat_number} in {self.theater.name}'

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return f'Booking by {self.user.username} for {self.seat.seat_number} at {self.theater.name}'