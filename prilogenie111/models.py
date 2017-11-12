from django.db import models
from django.utils import timezone

class MyFirstModel(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    my_field_1 = models.TextField()
    my_field_2 = models.TextField()
    my_field_3 = models.TextField()
    my_field_4 = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class MyModelForSum(models.Model):
    aaa = models.TextField()
    bbb = models.TextField()
    ccc = models.TextField()

    def __str__(self):
        return "It_Is_My_Record"