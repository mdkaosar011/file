from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Post(models.Model):
    caption = models.TextField()
    image = models.ImageField(upload_to='Images/Post', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  self.caption


class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    profile_pic = models.ImageField(upload_to='Images/Profile', null=True, blank=True)
    contact_info = models.CharField(max_length=200)
    author = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
