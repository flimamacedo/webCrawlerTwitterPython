# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
#from painel_demandas.models import DEMANDAS

@login_required(login_url='/login')
def ShowTweets(request):
    from datetime import datetime
    data = datetime.now()
    return render(request, 'painel_tweets/tweets.html',
        {
            'data': data,
        })
