from django.db import models

# Create your models here.


class Rental(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name



class Reservations(models.Model):
    rental_id = models.ForeignKey(Rental, related_name="rental_id", on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()

    def __str__(self) -> str:
        return f"{self.rental_id.name}, {self.id}"
