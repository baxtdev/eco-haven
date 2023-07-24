from rest_framework import serializers
from .models import*
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email' )


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True},}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
    
class NewsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = News
        fields = ('id','category','title','description','photo','user')

class AdvicesSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Adviсe
        fields = ('id','category','title','description','user')        

class CategorySerializer(serializers.ModelSerializer):
    news = NewsSerializer(
        many=True,
        read_only=True 
          )
    advices = AdvicesSerializers(
        many=True,
        read_only=True 
          )
    class Meta:
        model = Category
        fields = ('id','title','description','advices','news')