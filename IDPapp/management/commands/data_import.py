import csv
import os
from django.core.files import File
from django.conf import settings
from IDPapp.models import Food_Details

# def add_food_data():
#     file_path = 'D:/DjangoProjects/IntelligentDP/IntelligentDP/foodData/project_data_details.csv'
#     with open(file_path, 'r') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             food = Food_Details()
#             food.foodName = row['foodName']
#             food.calories_kcal = row['calories_kcal']
#             food.carbohydrate_g = row['carbohydrate(g)']
#             food.protein_g = row['protein(g)']
#             food.fat_g = row['fat_g']
#             food.fiber_g = row['fiber(g)']
#             food.foodType = row['FoodType']
#             food.image = row['image']

            
#             # Construct the image file path
#             image_path = os.path.join(settings.MEDIA_ROOT, 'Food_images', row['image'])
            
#             # Open the image file and save it to the 'image' field
#             with open(image_path, 'rb') as img_file:
#                 food.image.save(row['image'], File(img_file), save=False)
            
#             food.save()
from django.core.management.base import BaseCommand
from IDPapp.models import Food_Details

# class Command(BaseCommand):
#     help = 'Imports food data into the database'

#     def handle(self, *args, **options):
#         # Your code to import data goes here
#         file_path = 'D:/DjangoProjects/IntelligentDP/IntelligentDP/foodData/project_data_details.csv'
#         with open(file_path, 'r') as csvfile:
#           reader = csv.DictReader(csvfile)
#           for row in reader:
#             food = Food_Details()
#             food.foodName = row['FoodName']
#             food.calories_kcal = (row['Calories_Kcal'])
#             food.carbohydrate_g = float(row['Carbohydrate(g)'])
#             food.protein_g = float(row['Protein(g)'])
#             food.fat_g = float(row['Fat(g)'])
#             food.fiber_g = float(row['Fiber(g)'])
#             food.foodType = row['FoodType']
#             #food.image = row['image']

#            # Construct the image file path based on the food name
#             image_filename = row['FoodName'] + '.jpg'
#             image_path = os.path.join(settings.MEDIA_ROOT, 'Food Images', image_filename)

#             # Open the image file and save it to the 'image' field
#             with open(image_path, 'rb') as img_file:
#                 food.image.save(image_filename, File(img_file), save=False)

#             food.save()
from django.core.exceptions import ObjectDoesNotExist

#from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = 'Imports food data into the database'

    def handle(self, *args, **options):
        file_path = 'D:/DjangoProjects/IntelligentDP/IntelligentDP/foodData/project_data_details.csv'
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                food = Food_Details()
                food.foodName = row['FoodName']
                food.calories_kcal = row['Calories_Kcal']
                food.carbohydrate_g = float(row['Carbohydrate(g)'])
                food.protein_g = float(row['Protein(g)'])
                food.fat_g = float(row['Fat(g)'])
                food.fiber_g = float(row['Fiber(g)'])
                food.foodType = row['FoodType']
                # food.image = row['image']

                # Construct the image file path based on the food name
                image_filename = row['FoodName'] + '.jpg'
                image_path = os.path.join(settings.MEDIA_ROOT, 'Food Images', image_filename)

                try:
                    # Check if the image file exists
                    with open(image_path, 'rb') as img_file:
                        food.image.save(image_filename, File(img_file), save=False)
                except FileNotFoundError:
                    # Skip this food if image file is not found
                    continue

                # Check if the food already exists in the database
                existing_foods = Food_Details.objects.filter(foodName=food.foodName)
                if existing_foods.exists():
                    # Update the first existing food with new data
                    existing_food = existing_foods.first()
                    existing_food.calories_kcal = food.calories_kcal
                    existing_food.carbohydrate_g = food.carbohydrate_g
                    existing_food.protein_g = food.protein_g
                    existing_food.fat_g = food.fat_g
                    existing_food.fiber_g = food.fiber_g
                    existing_food.foodType = food.foodType
                    existing_food.image.name = food.image.name
                    existing_food.save()
                else:
                    # Save the new food to the database
                    food.save()
