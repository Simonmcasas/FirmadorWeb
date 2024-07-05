from django.db import models

# Create your models here.
class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    documentoFirmado = models.BooleanField(default=False)
    redirect_url = models.URLField(max_length=200)
    url_firma = models.TextField(blank=True, default='')
    dni = models.CharField(max_length=20, default='00000000')  # Valor predeterminado temporal
    email = models.EmailField(default='example@example.com')  # Valor predeterminado temporal
    nombre_y_apellido = models.CharField(max_length=255, default='Nombre Apellido')  # Valor predeterminado temporal

    def save(self, *args, **kwargs):
        if self.pk is not None:
            orig = Document.objects.get(pk=self.pk)
            # Ignorar cambios en los atributos inalterables
            self.file = orig.file
            self.redirect_url = orig.redirect_url
            self.dni = orig.dni
            self.email = orig.email
            self.nombre_y_apellido = orig.nombre_y_apellido
        super().save(*args, **kwargs)