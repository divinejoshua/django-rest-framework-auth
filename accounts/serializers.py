from rest_framework import serializers
from .models import Account
import re 	#This is for the username validator 


#Register a user
class RegisterSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(style={'input_type' : 'password'}, write_only=True)


    class Meta:
        model = Account
        fields = ['email','username', 'password', 'password2' ]
        extra_kwarg = {
            'password' : {'write_only' : True}
        }

    def save(self):
        account = Account (email=self.validated_data['email'], username=self.validated_data['username'])
        password = self.validated_data['password']    
        password2 = self.validated_data['password2']   
        username = self.validated_data['username']

        #Add validations before saving
        if (len(username) < 3) or (len(username) >15):
            raise serializers.ValidationError({'username' : 'Username must be between 3 to 15 characters.'})

        if not re.match(r'^[.A-Za-z0-9_-]+$', username):
            raise serializers.ValidationError({'username' : 'Username must only contain [A-Z], [a-z], [0-9], [_-.]characters.'})

        if password != password2:
            raise serializers.ValidationError({'password' : 'Passwords do not match.'})


        account.set_password(password)
        account.save()
        return account






#Check user with username
class AccountSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Account
        fields = ['id','username', 'email', 'fullname' ]

    def update(self, instance, validated_data):
        instance.username = self.validated_data['username']
        instance.email = self.validated_data['email']
        instance.fullname = self.validated_data['fullname']
        
        #Username validations before saving
        username = instance.username
        if (len(username) < 3) or (len(username) >15):
            raise serializers.ValidationError({'username' : 'Username must be between 3 to 15 characters.'})

        if not re.match(r'^[.A-Za-z0-9_-]+$', username):
            raise serializers.ValidationError({'username' : 'Username must only contain [A-Z], [a-z], [0-9], [_-.]characters.'})

        
        # Save the instance 
        instance.save()
        return instance