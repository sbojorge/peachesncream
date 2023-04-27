from django.db import models
from django.contrib.auth.models import User


class Grocery(models.Model):
    """
    Model to create a grocery_list
    """
    name = models.CharField(max_length=100, default='My grocery list')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='grocery_owner')
    created_on = models.DateTimeField(auto_now_add=True)
    item = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
