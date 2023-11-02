from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):

    def create_user(self, username, first_name, last_name, email, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.set_password(password)
        self.save()


class Note(models.Model):
    text = models.TextField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def add_note(self, text, username):
        self.text = text
        self.username = username
        self.save()
