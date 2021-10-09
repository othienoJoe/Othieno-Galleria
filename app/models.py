from django.db import models
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
    name = models.CharField(max_length = 60)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)

    # Save image to database
    def save_image(self):
        self.save()
