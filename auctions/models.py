from time import time
from django.contrib.auth.models import AbstractUser
from django.db import models
from model_utils import Choices


class User(AbstractUser):
    pass


class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(blank=True)
    categories = Choices("Clothing/Footwear","Books","Electronics","Cosmetics","Toys","Home/Garden","Sport/Leisure")
    category = models.CharField(choices=categories, max_length=32)
    starting_price = models.DecimalField(decimal_places=2, max_digits=10)
    lister = models.ForeignKey(User, on_delete=models.CASCADE, related_name="selling")

    def __str__(self):
        return f"{self.title} in {self.category}"



class Bid(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buying")
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")


    def __str__(self):
        return f"{self.bidder} bid {self.amount}"


class Comment(models.Model):
    comment = models.TextField(blank=False)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")


    def __str__(self):
        return f'{self.commenter}: "{self.comment}"'

