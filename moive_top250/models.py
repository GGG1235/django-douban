from django.db import models

# Create your models here.

class douban_top250(models.Model):
    serial_number=models.IntegerField()
    movie_name=models.CharField(max_length=255)
    introduce=models.CharField(max_length=255)
    star=models.FloatField(max_length=12)
    evaluate=models.CharField(max_length=255)
    describe=models.CharField(max_length=255)
    datetime=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.movie_name