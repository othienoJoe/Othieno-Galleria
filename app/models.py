from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt

# Create your models here.
# The location model
class Location(models.Model):
    name = models.CharField(max_length=60, unique=True)
    # To save location to database
    def save_location(self):
        self.save()
    # Update location
    def update_location(self, name):
        self.name = name
        self.save()
     # Delete location from database
    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name

# The category model
class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)
    # Save category to database
    def save_category(self):
        self.save()
    # To update category
    def update_category(self, name):
        self.name = name
        self.save()
    # Delete category from database
    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name

# Image model
class Image(models.Model):
    # new_field = models.CharField(max_length=140, default=True)
    name = models.CharField(max_length = 60)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)

    # Save image to database
    def save_image(self):
        self.save()

# Lets Update the images
def update_image(self, name, description, location, category):
    self.name = name
    self.description = description
    self.location = location
    self.category = category
    self.save()

# To Get ll images
@classmethod
def get_all_images(cls):
    images = Image.objects.all()
    return images

# Getting Image by id
@classmethod
def get_image_by_id(cls, id):
    image = Image.objects.get(id=id)
    return image

# To get images by location
@classmethod
def filter_by_location(cls, location):
    images = Image.objects.filter(location__name=location)
    return images

# To get images by category
@classmethod
def filter_by_category(cls, category):
    images = Image.objects.filter(category__name=category)
    return images

# For searching images
@classmethod
def search_image(cls, search_term):
    images = cls.objects.filter(name__icontains=search_term)
    return images

# To delete image from database
def delete_image(self):
    self.delete()

def __str__(self):
    return self.name
