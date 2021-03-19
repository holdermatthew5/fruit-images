from django.db import models
from django.contrib.auth import get_user_model

class BraeburnApple(models.Model):
    uploaded_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)