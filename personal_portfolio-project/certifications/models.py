from django.db import models

class Certification(models.Model):
    title = models.CharField(max_length = 100)
    date = models.DateField(editable=True)
    image = models.ImageField(upload_to='portfolio/images/certification')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title