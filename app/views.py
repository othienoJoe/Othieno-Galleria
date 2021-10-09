from django.shortcuts import render
import datetime as dt
from .models import Image, Location, Category
from django.http import HttpResponse

# Create your views here.
def welcome(request):
	return HttpResponse('Welcome to the Othieno Galleria')

# The index function for displaying the images
def index(request):
	images = Image.objects.all().order_by('-id')
	locations = Location.objects.all()
	category = Category.objects.all()
	title = 'Homepage'
	return render(request, 'index.html', {'images': images, 'location': locations, 'category': category, 'title': title})

# Search function to search for the images
def search(request):
	if 'category' in request.GET and request.GET["category"]:
		search_term = request.GET.get("category").lower()