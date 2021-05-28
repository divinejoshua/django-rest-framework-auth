from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse


#from rest_framework import permissions
from . import serializers
from .models import Account

from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView


#For authentication
from django.contrib.auth import authenticate

#For email verification

#Get Users
class getUser_view(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {}
        try:
            user = Account.objects.get(email=request.user)
            serializer = serializers.AccountSerializer(user)
            # print(request.META['HTTP_USER_AGENT'])
            data = serializer.data
            data['email_verified'] = user.email_verified


            # context = []
            # for n in range(5):
            #     user = serializer.data
            #     user['fullname'] = username.fullname
            #     context.append(user)
            #     print(context)


            return Response(data,  status=status.HTTP_200_OK)

        except:    
            return Response(status=status.HTTP_404_NOT_FOUND)




#Register users
class register_view(APIView):
    statusCode = None
    data = {}

    #The post request
    def post(self, request):
        data = {}                                                           #This is all the data that is been passed to the api Eg. Contex variables
        # current_site = get_current_site(request)
        serializer = serializers.RegisterSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            data['success'] = "Successfully registered."
            data['fullname'] = account.fullname
            data['username'] = account.username
            data['email'] = account.email
            print(account)
           

        else:
            data = serializer.errors

        return Response(data)



#Login view for validation
class login_view(APIView):
    data = {}
    
    def post(self, request):
        credentials = request.data['username']
        password = request.data['password']
        # print(credentials)

        # Check if username or email exist 
        if Account.objects.filter(email=credentials).exists()==True:
            account_cred =  Account.objects.get(email=credentials) 	

        elif Account.objects.filter(username=credentials).exists()==True:
            account_cred =  Account.objects.get(username=credentials) 	

        else:
            account_cred = None
            self.data['error'] = "Username/Email not found"


        # If it does, it means the password doesnt match 
        if account_cred:
            # Check if username and passowrd match
            userAuth = authenticate(username=account_cred, password=password) 

            if userAuth is not None:					 		
                self.data['error'] = False
            else:
                self.data['error'] = "Incorrect password"



        return Response(self.data)

