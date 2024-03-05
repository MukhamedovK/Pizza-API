from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=200)
    cost = models.SmallIntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    status = models.CharField(max_length=50, default='delivering')
    phone_number = models.SmallIntegerField(blank=True, null=True)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order: {self.pizza.name}, status: {self.status}"

