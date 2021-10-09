from django.shortcuts import render
from .models import Image
from django.http import HttpResponse

# Create your views here.
def welcome(request):
	return HttpResponse()

# The index function for displaying the images
def index(request):
	images = Images.objects.all().order_by('-id')