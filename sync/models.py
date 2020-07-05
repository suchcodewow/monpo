import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class LogEntry(models.Model):
    severity = models.CharField(max_length=50)
    entry_date = models.DateTimeField('date logged')
    def __str__(self):
        return self.severity
    def was_published_recently(self):
        return self.entry_date >= timezone.now() - datetime.timedelta(days=1)


class SNServers(models.Model):
    server_name = models.CharField('server name', max_length=12)
    env = models.IntegerField(default=0)
    mnemonic = models.CharField(max_length=3)
    def __str__(self):
        return self.snservers_text
