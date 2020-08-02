from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from .models import UserDocs

# Create your views here.
class SaveDocs(APIView):
    def post(self, request):
        print("dataaaa")
        user_id = json.loads(request.data['user_id'])
        user_name = json.loads(request.data['user_name'])
        obj = UserDocs()
        obj.user_id = user_id
        obj.user_name = user_name
        obj.user_doc = request.data['document']
        obj.save()
        return Response("successfully saved")

class UserDocsGet(APIView):
    def post(self,request):
        userDoc = UserDocs.objects.filter(user_id=request.data['user_id'])
        doc = userDoc[0].user_doc.url
        data = {"document":doc}
        return Response(data)

class UserDocsUpdate(APIView):
    def post(self,request):
        user_id = json.loads(request.data['user_id'])
        userDoc = UserDocs.objects.get(user_id=user_id)
        userDoc.user_doc = request.data['document']
        userDoc.save()
        return Response("Document updated successfully")

class UserDocsDelete(APIView):
    def post(self,request):
        UserDocs.objects.filter(user_id=request.data['user_id']).delete()

        return Response("successfully deleted")