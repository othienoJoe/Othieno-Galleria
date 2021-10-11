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
		searched_images = Image.filter_by_category(search_term)
		message = f"{search_term}"
		locations = Location.objects.all()

		return render(request, 'search.html', {"message": message, "images": searched_images, 'locations': locations})

	else:
		locations = Location.objects.all()
		message = "You haven't searched for any term"
		return render(request, 'search.html', {"message": message, 'locations': locations})


# This displays all images in a specific location
def location(request, location_id):
    locations = Location.objects.all()
    images = Image.objects.filter(location_id=location_id)
    location = Location.objects.get(id=location_id)
    title = location
    return render(request, 'location.html', {'images': images, 'locations': locations, 'title': title})


# For displaying single image details
def image(request, image_id):
    locations = Location.objects.all()
    image = Image.objects.get(id=image_id)
    title = image
    return render(request, 'image.html', {'image': image, 'locations': locations, 'title': title})