from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Document
from .serializers import DocumentSerializer

class DocumentUploadView(APIView):
    def post(self, request, format=None):
        file = request.FILES.get('file')
        redirect_url = request.data.get('redirect_url')
        dni = request.data.get('dni')
        email = request.data.get('email')
        nombre_y_apellido = request.data.get('nombre_y_apellido')

        if file and file.content_type == 'application/pdf' and redirect_url and dni and email and nombre_y_apellido:
            document = Document(
                file=file, 
                redirect_url=redirect_url, 
                dni=dni, 
                email=email, 
                nombre_y_apellido=nombre_y_apellido
            )
            document.save()
            serializer = DocumentSerializer(document)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response({'error': 'Invalid file type or missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

class DocumentDetailView(APIView):
    def get_object(self, pk):
        try:
            return Document.objects.get(pk=pk)
        except Document.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        document = self.get_object(pk)
        serializer = DocumentSerializer(document)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        document = self.get_object(pk)
        data = request.data.copy()

        # Ignorar cambios en los atributos inalterables
        data.pop('file', None)
        data.pop('redirect_url', None)
        data.pop('dni', None)
        data.pop('email', None)
        data.pop('nombre_y_apellido', None)

        serializer = DocumentSerializer(document, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentListView(APIView):
    def get(self, request, format=None):
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)
