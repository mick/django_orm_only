from django.db import models

class NewTable(models.Model):
     text = models.CharField(max_length=255)
