from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'file', 'uploaded_at', 'documentoFirmado', 'redirect_url', 'url_firma', 'dni', 'email', 'nombre_y_apellido', 'ubicacion_geografica', 'ip', 'timestamp')
        read_only_fields = ('file','redirect_url', 'dni', 'email', 'nombre_y_apellido',)  # Atributos de solo lectura

