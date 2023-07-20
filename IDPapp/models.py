from django.db import models

# Create your models here.

class Food_Details(models.Model):
   foodName = models.CharField( max_length=50)
   calories_kcal = models.IntegerField()
   carbohydrate_g = models.IntegerField()
   protein_g = models.IntegerField()
   fat_g = models.IntegerField()
   fiber_g = models.IntegerField()
   foodType = models.CharField(max_length=50)
   image = models.ImageField(upload_to='food_images/')