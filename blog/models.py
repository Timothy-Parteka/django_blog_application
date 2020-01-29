from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)

    # ForeignKey allows a many-to-one relationship.
    # This means that a given user can be the author
    # of many different blog posts.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    body = models.TextField()

    def __str__(self):
        return self.title
