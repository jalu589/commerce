from time import time
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.URLField(blank=True)
    categories = ((1,"Clothing/Footwear"), (2,"Books"), (3,"Electronics"), (4,"Cosmetics"), (5,"Toys"), (6,"Home/Garden"), (7,"Sport/Leisure"))
    category = models.CharField(choices=categories, max_length=2)
    starting_price = models.DecimalField(decimal_places=2, max_digits=10)
    lister = models.ForeignKey(User, on_delete=models.CASCADE, related_name="selling")
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} in {self.category}"



class Bid(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buying")
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bidder} bid {self.amount} -{self.time}"


class Comment(models.Model):
    comment = models.TextField(blank=False)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.commenter}: "{self.comment}" -{self.time}'

