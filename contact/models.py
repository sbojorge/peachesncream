from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    """
    Model to create a contact form
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='contact_owner')
    reason = models.CharField(max_length=50)
    content = models.TextField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.user} : {self.reason}"
