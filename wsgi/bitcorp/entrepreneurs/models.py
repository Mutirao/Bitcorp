from django.db import models


class entrepreneur(models.Model):
    """creates an entrepreneur, can own a company or be a shareholder"""
    name = models.TextField(max_length=100)
    lastname = models.TextField(max_length=100)
    photo = models.ImageField(upload_to='photos')
    url_id = models.TextField(max_length=200)
    register_date = models.DateTimeField(now)

    def __unicode__(self):
        return '{:} {:}'.format(self.name, self.lastname)
