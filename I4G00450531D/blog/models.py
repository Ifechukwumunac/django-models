from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    # the get_user_model is the best of three other ways to refer to user either the user(the basic user gotten fron django)
    # the auth_user_model which permits one to either just the user name or build fron scratch. the get_user_model uses whichever is available.
    # check README.md for more.
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    pub_date = models.DateTimeField("date published")
    creation_date = models.DateTimeField("date created")

    # to ensure that i see the title in my admin panel instead of the less informative default
    def __str__(self):
        return self.title
