from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
import pickle
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import random
from pickle import load
import os
# model = load('./savedModels/model.pkl')
# Create your views here.
def home(request):
    return render(request,'home.html')


def main(request):
    return render(request,'choose.html')

def bmi(request):
    return render(request,'bmi.html')





# from django.shortcuts import render
# from surprise import Dataset, Reader, KNNBasic
# import pandas as pd
# from IDPapp.models import Food_Details  # Import the Food_Details model

# def generate_recommendation(request):
#     if request.method == 'POST':
#         calorie_intake = int(request.POST['calorie_intake'])
#         meal_frequency = int(request.POST['meal_frequency'])
        
#         # Load the data from your Excel file using pandas
#         df = pd.read_excel('D:/DjangoProjects/IntelligentDP/IntelligentDP/foodData/project_data2.xlsx')

#         # Define the reader object
#         reader = Reader(rating_scale=(1, 5))

#         # Add a dummy user ID and rating to the DataFrame
#         df['User'] = 'user'
#         df['Rating'] = 1

#         # Load the data into Surprise's Dataset format
#         data = Dataset.load_from_df(df[['User', 'FoodName', 'Rating']], reader)

#         # Build the full trainset
#         trainset = data.build_full_trainset()

#         # Use the KNNBasic algorithm with cosine similarity
#         algo = KNNBasic(k=40, sim_options={'name': 'cosine', 'user_based': False})

#         # Train the model on the full dataset
#         algo.fit(trainset)

#         # Get all unique items and their calorie information
#         all_items = df['FoodName'].unique()
#         calories_info = {item: df.loc[df['FoodName'] == item, 'Calories_Kcal'].values[0] for item in all_items}

#         # Generate personalized meal plans based on user inputs
#         meal_plan = []
#         remaining_calories = calorie_intake

#         for _ in range(meal_frequency):
#             # Calculate the average calorie per meal
#             avg_calorie_per_meal = remaining_calories / (meal_frequency - len(meal_plan))

#             # Find the closest matching meal within the calorie limit, excluding the meals already in the plan
#             closest_meal = min(calories_info, key=lambda x: abs(calories_info[x] - avg_calorie_per_meal) if x not in meal_plan else float('inf'))

#             # Add the closest meal to the meal plan
#             meal_plan.append(closest_meal)

#             # Update the remaining calories
#             remaining_calories -= calories_info[closest_meal]

#         # Shuffle the meal plan
#         random.shuffle(meal_plan)

#         # Prepare the data for rendering in the template
#         suggested_meals = []
#         for meal in meal_plan:
#             rating = algo.predict('user', meal).est
#             calorie = calories_info[meal]

#             # Get food details from the database
#             food = Food_Details.objects.get(foodName=meal)

#             # Create a dictionary with the meal details
#             suggested_meals.append({
#                 'meal': meal,
#                 'rating': rating,
#                 'calorie': calorie,
#                 'image': food.image.url,
#                 'carbohydrates': food.carbohydrate_g,
#                 'protein': food.protein_g,
#                 'fat': food.fat_g,
#                 'fiber': food.fiber_g
#             })

#         # Calculate the total calorie count for the meal plan
#         total_calories = sum([calories_info[meal] for meal in meal_plan])

#         # Pass the suggestions and other data to the template for rendering
#         context = {
#             'calorie_intake': calorie_intake,
#             'meal_frequency': meal_frequency,
#             'total_calories': total_calories,
#             'suggested_meals': suggested_meals
#         }

#         return render(request, 'recommendations.html', context)

#     return render(request, 'choose.html')

from django.shortcuts import render
from surprise import Dataset, Reader, KNNBasic
import pandas as pd
from IDPapp.models import Food_Details
import random

def generate_recommendation(request):
    if request.method == 'POST':
        calorie_intake = int(request.POST['calorie_intake'])
        meal_frequency = int(request.POST['meal_frequency'])
        
        # Load the data from your Excel file using pandas
        df = pd.read_excel('D:/DjangoProjects/IntelligentDP/IntelligentDP/foodData/project_data2.xlsx')

        # Define the reader object
        reader = Reader(rating_scale=(1, 5))

        # Add a dummy user ID and rating to the DataFrame
        df['User'] = 'user'
        df['Rating'] = 1

        # Load the data into Surprise's Dataset format
        data = Dataset.load_from_df(df[['User', 'FoodName', 'Rating']], reader)

        # Build the full trainset
        trainset = data.build_full_trainset()

        # Use the KNNBasic algorithm with cosine similarity
        algo = KNNBasic(k=40, sim_options={'name': 'cosine', 'user_based': False})

        # Train the model on the full dataset
        algo.fit(trainset)

        # Get all unique items and their calorie information
        all_items = df['FoodName'].unique()
        calories_info = {item: df.loc[df['FoodName'] == item, 'Calories_Kcal'].values[0] for item in all_items}
        food_types = {item: df.loc[df['FoodName'] == item, 'FoodType'].values[0] for item in all_items}

        # Generate personalized meal plans based on user inputs
        meal_order = []

        if meal_frequency == 2:
            meal_order = ['breakfast', 'lunch']
        elif meal_frequency == 3:
            meal_order = ['breakfast', 'lunch', 'dinner']
        elif meal_frequency == 4:
            meal_order = ['breakfast', 'snack', 'lunch', 'dinner']
        elif meal_frequency == 5:
            meal_order = ['breakfast', 'snack', 'lunch', 'snack', 'dinner']
        elif meal_frequency == 6:
            meal_order = ['breakfast', 'snack', 'lunch', 'snack', 'dinner','snack']
        else:
            raise ValueError("Invalid meal frequency. Supported values are 2, 3, 4,5 or 6.")

        meal_plan = []
        remaining_calories = calorie_intake

        for meal_type in meal_order:
            # Calculate the average calorie per meal
            avg_calorie_per_meal = remaining_calories / meal_frequency

            # Generate a random number of food items for the meal (between 1 and 3)
            num_food_items = random.randint(1, 3)

            meal_items = []
            remaining_calories_in_this_meal = avg_calorie_per_meal
            while len(meal_items) < num_food_items:
                # Calculate the average calorie per food item
                avg_calorie_per_food = remaining_calories_in_this_meal / num_food_items

                # Find the closest matching meals within the calorie limit, excluding the meals already in the plan
                closest_meals = [meal for meal in calories_info if (meal_type == 'dinner' and (food_types[meal] == 'lunch' or food_types[meal] == 'dinner')) or (meal_type != 'dinner' and food_types[meal] == meal_type) and meal not in meal_items]

                # Sort the meals by their distance to the average calorie per food item
                closest_meals.sort(key=lambda x: abs(calories_info[x] - avg_calorie_per_food))

                if closest_meals:
                    # Add the closest meal to the meal items
                    meal_items.append(closest_meals[0])
                    remaining_calories_in_this_meal -= calories_info[closest_meals[0]]

            # Add the meal items to the meal plan
            meal_plan.append(meal_items)

            meal_frequency -= 1

            # Update the remaining calories
            remaining_calories -= sum([calories_info[meal] for meal in meal_items])

        # Prepare the data for rendering in the template
        suggested_meals = []

        for meal_items in meal_plan:
            # Calculate the average rating for the meal items
            avg_rating = sum([algo.predict('user', meal_item).est for meal_item in meal_items]) / len(meal_items)

            # Create a dictionary with the meal details
            meal_details = []
            for meal_item in meal_items:
                 try:
                    food = Food_Details.objects.get(foodName=meal_item)
                    meal_detail = {
                        'foodName': food.foodName,
                        'calories': calories_info[meal_item],
                        'rating': avg_rating,
                        'carbohydrates': food.carbohydrate_g,
                        'protein': food.protein_g,
                        'fat': food.fat_g,
                        'fiber': food.fiber_g,
                        'image': food.image.url
                    }
                    meal_details.append(meal_detail)
                 except Food_Details.DoesNotExist:
                    # Handle if food item does not exist in the database
                    pass

            suggested_meals.append({
                'meal': meal_items,
                'calorie': sum([calories_info[meal_item] for meal_item in meal_items]),
                'foods': meal_details
            })
        #print(suggested_meals)

        # Calculate the total calorie count for the meal plan
        total_calories = sum([sum([calories_info[meal_item] for meal_item in meal_items]) for meal_items in meal_plan])

        # Compare total calories with the user's specified calorie intake
        calorie_difference = total_calories - calorie_intake

        # Pass the suggestions and other data to the template for rendering
        meal_recommendations = {meal_type: foods for meal_type, foods in zip(meal_order, meal_plan)}
        print(meal_recommendations.items)

        context = {
            'calorie_intake': calorie_intake,
            'meal_frequency': meal_frequency,
            'total_calories': total_calories,
            'calorie_difference': calorie_difference,
            'meal_recommendations': meal_recommendations,
            'suggested_meals':suggested_meals
        }
        # print(calorie_intake)
        # print(meal_frequency)
        # print(total_calories)
        #print(meal_recommendations)
       


        return render(request, 'predict.html', context)

    return render(request, 'choose.html')



