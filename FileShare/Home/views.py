from django.shortcuts import render
from rest_framework.views import APIView
from . models import FolderModel, FilesModel
from . serializer import FileSerializer, FileListSerializer
from rest_framework.response import Response

# Create your views here.
def home_view(request):
    return render(request,'Home/home.html')

class HandleFileUpload(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = FileListSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Files uploaded successfully', 'data':serializer.data})
            return Response({'message':'Something went wrong','data':serializer.errors})
        except Exception as e:
            print(e)

    def get(self, request):
        data= FilesModel.objects.all()

        serializer = FileSerializer(data, many= True)

        return Response(serializer.data)
    
def download_view(request,uid):
    context={'uid':uid}
    return render(request,'Home/download.html',context)