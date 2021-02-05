#from django.contrib.auth.models import User, Group
from apiRest.models import Tweets
from rest_framework import serializers


#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = User
#        fields = ['url', 'username', 'email', 'groups']
#
#
#class GroupSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = Group
#        fields = ['url', 'name']
#

class TweetsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tweets
        fields = ['created_at', 'followers_count', 'lang',  'username', 'location', 'place', 'tweet', 'retweet_count',]        
