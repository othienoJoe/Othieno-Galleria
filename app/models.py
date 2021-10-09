from django.db import models

# Create your models here.
# Image model
class Image(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='uploads/images/')
    # image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)

    # save image to database
    def save_image(self):
        self.save()