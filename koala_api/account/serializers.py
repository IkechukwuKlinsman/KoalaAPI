
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password= serializers.CharField(max_length= 255, write_only= True) #used to make the password not readable in the json template, just saved

    class Meta:
        model = User
        # fields ='__all__'
        fields = ['id','first_name','last_name','email',
                    'phone','date_joined']