from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField


class Grocery(models.Model):
    """
    Model to create a grocery_list
    """
    CATEGORIES = [("groceries", "Groceries"),
                  ("school", "School"),
                  ("hardware", "Hardware"),
                  ("travel", "Travel"),
                  ("gifts", "Gifts"),
                  ("decoration", "Decoration"),
                  ("lifestyle", "Lifestyle"),
                  ("wishlist", "Wishlist")]

    name = models.CharField(max_length=500, default='My grocery list')
    category = models.CharField(max_length=20, choices=CATEGORIES,
                                default='groceries')
    shop = models.CharField(max_length=500, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='grocery_owner')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    item = RichTextField(max_length=10000, null=False, blank=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
