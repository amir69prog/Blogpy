from django.db import models
from django.contrib.auth import get_user_model

from ckeditor_uploader.fields import RichTextUploadingField


User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='files/user_avatar')
    description = models.TextField()

    def __str__(self) -> str:
        return self.user.username


class Article(models.Model):
    title = models.CharField(max_length=512)
    cover = models.ImageField(upload_to='files/articles_covers')
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, models.CASCADE)

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=128)
    cover = models.ImageField(upload_to='files/category_covers')

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.title