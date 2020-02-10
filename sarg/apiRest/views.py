from django.contrib.auth.models import User, Group
from apiRest.models import Tweets
from rest_framework import viewsets
from apiRest.serializers import TweetsSerializer#, UserSerializer, GroupSerializer


#class UserViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows users to be viewed or edited.
#    """
#    queryset = User.objects.all().order_by('-date_joined')
#    serializer_class = UserSerializer
#
#
#class GroupViewSet(viewsets.ModelViewSet):
#    """
#    API endpoint that allows groups to be viewed or edited.
#    """
#    queryset = Group.objects.all()
#    serializer_class = GroupSerializer
#
class TweetsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tweets to be viewed or edited.
    """
    queryset = Tweets.objects.all()
    serializer_class = TweetsSerializer
