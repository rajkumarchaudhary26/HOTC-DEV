from django.db import models

class Download(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title