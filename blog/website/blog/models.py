from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    title = models.SlugField()
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='post')
    draft = models.BooleanField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'pk': self.pk})


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text}'

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'pk': self.pk})
