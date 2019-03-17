from django.shortcuts import render
from django.http import HttpResponse
from .models import Attribute, SubAttribute

def index(request):
    attribute = Attribute.objects.all()
    sub_attribute = SubAttribute.objects.all()
    context = {
        'attribute' : attribute,
        'sub_attribute' : sub_attribute
    }
    return render(request, 'index.html', context=context)
