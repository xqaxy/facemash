from django.template import loader, Context
from django.http import HttpResponse
from gallery.models import Girl
from gallery.models import Image
import random

GIRLCOUNT = 1000
IMAGECOUNT = 1183

def top(request):
    top_images = []
    girls = Girl.objects.all().order_by('-votes')[:100]
    for girl in girls:
        images = Image.objects.filter(owner=girl.id)
        if len(images) > 0:
            image = images[0]
            top_images.append([girl, image])
    t = loader.get_template("top.html")
    c = Context({ 'top_images': top_images })
    return HttpResponse(t.render(c))

    
    
def browse(request):
    top_images = []
    girls = Girl.objects.all().order_by('?')[:200]
    for girl in girls:
        images = Image.objects.filter(owner=girl.id)
        if len(images) > 0:
            image = images[0]
            top_images.append([girl, image])
    t = loader.get_template("browse.html")
    c = Context({ 'top_images': top_images })
    return HttpResponse(t.render(c))


def index(request):
    ## Get vote page    
    vote_girls = []
    images = Image.objects.all().order_by('?')[0:2]
    for image in images:
        girl = Girl.objects.get(pk=image.owner)
        vote_girls.append([girl, image])
    t = loader.get_template("vote.html")
    c = Context({ 'vote_girls': vote_girls })
    return HttpResponse(t.render(c))    
    

def vote(request, param):
    ## Update girl vote
    if param != "":
        voteid = int(param)
        girl = Girl.objects.get(pk=voteid)
        girl.votes += 1
        girl.save()
    ## Get vote page    
    vote_girls = []
    images = Image.objects.all().order_by('?')[0:2]
    for image in images:
        girl = Girl.objects.get(pk=image.owner)
        vote_girls.append([girl, image])
    t = loader.get_template("vote.html")
    c = Context({ 'vote_girls': vote_girls })
    return HttpResponse(t.render(c))
    
 
def detail(request, param):
    ## Update girl vote
    if param != "":
        girlid = int(param)
        girl = Girl.objects.get(pk=girlid) 
        detail_images = []
        images = Image.objects.all().filter(owner=girl.id)
        for image in images:
            detail_images.append(image)
        t = loader.get_template("detail.html")
        c = Context({ 'detail_images': detail_images, 'girl': girl })
    return HttpResponse(t.render(c)) 

    