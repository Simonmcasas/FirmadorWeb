from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'file', 'uploaded_at', 'documentoFirmado', 'redirect_url', 'url_firma')
        ead_only_fields = ('file','redirect_url')  # Atributos de solo lectura

