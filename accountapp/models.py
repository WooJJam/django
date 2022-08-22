from django.db import models

# Create your models here.

class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False) # null 은 공백 true이면 공백이 있어도됨, false 이면 공백이 없어야함
    