from django.db import models

# Create your models here.


class Relation(models.Model):
    sharer = models.CharField(max_length=255)
    moocher = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    def __str__(self):
        str = '{\n"owner": "' + self.sharer + '",\n'
        str += '"moocher": "' + self.moocher + '",\n'
        str += '"service": "' + self.service + '"\n}'
        return str
    
class Uname(models.Model):
    username = models.CharField(max_length=32)
    ip=models.CharField(max_length=32)
    def __str__(self):
        str = '{\n"username": "' + self.username + '",\n'
        str += '"ip_address": "' + self.ip + '"\n}'
        return str


class Cookie(models.Model):
    username = models.CharField(max_length=32)
    moocher = models.CharField(max_length=32)
    service = models.CharField(max_length=64)
    text = models.CharField(max_length=16000)
    def __str__(self):
        return self.text
