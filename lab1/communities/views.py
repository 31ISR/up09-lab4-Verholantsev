from django.shortcuts import render
from .models import Community

def communities(req):
    Community1 = Community.objects.all().order_by('-date')
    return render(req, 'communities/communities.html', {'communities' : Community1})

def community_page(request, slug):
    Community2 = Community.objects.get(slug=slug)
    return render(request, 'communities/communities_page.html', {'community': Community2})

