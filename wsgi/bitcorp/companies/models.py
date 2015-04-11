from django.db import models

from entrepreneurs.models import entrepreneur


class investment(models.Model):
    """shareholders and investment description"""
    shareholder = models.ForeignKey(entrepreneur)
    participation = models.FloatField()
    rol = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)

    def __unicode__(self):
        return '{:} owns {:}'.format(self.shareholder, self.participation)


class company(models.Model):
    """company registered"""
    name = models.CharField(max_length=100)
    company_type = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100)
    owner = models.ForeignKey(entrepreneur)
    company_composition = models.ManyToManyField(investment)
    description = models.TextField(max_length=1000, null=True, blank=True)

    def __unicode__(self):
        return '{:} from {:}'.format(self.name, self.location)
