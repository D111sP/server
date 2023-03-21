from django.db import models

class Key_base(models.Model):
    key = models.CharField(max_length=255)

class Date_user(models.Model):
    key = models.OneToOneField(Key_base, on_delete=models.CASCADE, primary_key=True)
    name_PC = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    stone = models.CharField(max_length=255)
    wfi = models.CharField(max_length=255)
    uname = models.CharField(max_length=255)
    time_creat = models.DateTimeField(auto_now_add=True)


class History_date_user(models.Model):
    key = models.CharField(max_length=255)
    name_PC = models.CharField(max_length=255)
    ip = models.CharField(max_length=255)
    stone = models.CharField(max_length=255)
    wfi = models.CharField(max_length=255)
    uname = models.CharField(max_length=255)
    status = models.BooleanField(null=True)
    time_creat = models.DateTimeField(auto_now_add=True)