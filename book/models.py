from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.CharField(max_length=50)
    publisher = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    covers = models.ImageField(upload_to='book_covers', null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])


class Comment(models.Model):
    COMMENT_STAR = (
        ('1', 'BAD'),
        ('2', 'NORMAL'),
        ('3', 'GOOD')
    )

    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    recommend = models.BooleanField()
    star = models.CharField(choices=COMMENT_STAR, max_length=10)

    def __str__(self):
        return f"{self.user} --> {self.text}"

