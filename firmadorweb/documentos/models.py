from django.db import models

# Create your models here.
class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    documentoFirmado = models.BooleanField(default=False)
    redirect_url = models.URLField(max_length=200)
    url_firma = models.TextField(blank=True, default='')
