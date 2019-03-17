from django.shortcuts import render,render_to_response
from django.http import HttpResponse

from . import models
# Create your views here.

def render404(request):
    return HttpResponse("404")

def render500(request):
    return HttpResponse("500")

def index(request):
    moives = models.douban_top250.objects.all()
    page=request.GET.get('page')
    if page==None:
        page=1
        return render(request, 'html/index.html', {'moives': moives[:25],'page':int(page)})
    else:
        return render(request,'html/index.html',{'moives':moives[(int(page)-1)*25:(int(page)-1)*25+25],'page':int(page)})




def moive_info(request,movie_id):
    moive=models.douban_top250.objects.get(pk=movie_id)
    return render(request,'html/moive.html',{'moive':moive})