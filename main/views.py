from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
# from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
# from django.template.context_processors import csrf
# from django.views.decorators.csrf import csrf_exempt
# from datetime import *
# import random
# import string
from .models import Item, Category
# Create your views here.


def home(request):
    tovars = Item.objects.all()
    context = {
        'title': 'HelloWorld',
        'tovars': tovars,
    }
    return render(request, 'index.html', context)


def item(request, alias):
    try:
        tovar = Item.objects.get(alias=alias)
    except:
        return Http404
    context = {
        'tovar': tovar,
    }
    return HttpResponse(render_to_string('item.html', context))
