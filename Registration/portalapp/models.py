from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.

class User(AbstractUser):
	middle_name = models.CharField(max_length=30, blank=True, null=True)
	gender = models.CharField(max_length=10, blank=True, null=True)
	registered_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	rotation = models.CharField(max_length=30, blank=True, null=True)

    


class Rotation(models.Model):
	name = models.CharField(max_length=30, unique=True)
	limit = models.IntegerField(default=25, blank=False, null=False)
	#user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True, related_name='rotation' )


	def __str__(self):
		return self.name