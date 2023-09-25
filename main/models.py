from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Service(models.Model):
    service = models.CharField(max_length=255)
    def __str__(self):
        return self.service
class Service2(models.Model):
    service2 = models.CharField(max_length=255)
    def __str__(self):
        return self.service2

class Nationality(models.Model):
    nationality = models.CharField(max_length=255)
    def __str__(self):
        return self.nationality
    

class Refugee(models.Model):
    name = models.CharField(max_length=255)
    file_no = models.CharField(max_length=12)
    phone_number = models.IntegerField()
    nationality = models.ForeignKey(Nationality,default="", on_delete=models.DO_NOTHING)
    service = models.ForeignKey(Service,default="", on_delete=models.DO_NOTHING)
    service2 = models.ForeignKey(Service2, on_delete=models.DO_NOTHING)
    message = models.CharField(max_length=1000,default="")
    case_status = models.CharField(default='Open', max_length=100)
    data_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return None
    