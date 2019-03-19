from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import userprofile
from .serializers import UpdateSerializer
# Create your views here.
class SnippetList(APIView):
    def post(self, request):
        print (request.data)
        obj = userprofile()  # gets new object
        obj.firstName = request.data['firstName']
        obj.lastname = request.data['lastname']
        obj.phone = request.data['phone']
        obj.password = request.data['password']
        obj.state = request.data['state']
        obj.country = request.data['country']
        obj.check = request.data['check']
        obj.gender = request.data['gender']
        obj.email = request.data['email']
        obj.save()
        return Response('sucesssfully')
class Getvalues(APIView):
    def get(self, request):
            print (request.data)
            entry = userprofile.objects.all().values()
            return Response(entry)

class Deleterecord(APIView):
    def post(self, request):
            print (request.data)
            phone=request.data['phone']
            userprofile.objects.get(phone=phone).delete()
            return Response("delated sucesfuly")
class Getuser(APIView):
    def post(self, request):
        print (request.data)
        entry = userprofile.objects.filter(id=request.data).values()
        print("entry",entry)
        return Response(entry)

class Updateuser(APIView):
    def post(self, request):
        print (request.data)
        id = request.data['id']
        userprofile.objects.filter(id=id).update(firstName=request.data['firstName'],lastname=request.data['lastname'],phone=request.data['phone'],
         password =request.data['password'], state =request.data['state'],country =request.data['country'], check =request.data['check'],gender =request.data['gender'],email = request.data['email'])
        # userprofile.objects.filter(id=id).update()
        # obj.save()
        # details = userprofile.objects.filter(id=id)
        # serializer = UpdateSerializer(details,id)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response("Updated")
        # else:
        return Response("Updated")
        print("*********",serializer.errors)