# Generated by Django 4.2.1 on 2023-07-15 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodName', models.CharField(max_length=50)),
                ('calories_kcal', models.IntegerField()),
                ('carbohydrate_g', models.IntegerField()),
                ('protein_g', models.IntegerField()),
                ('fat_g', models.IntegerField()),
                ('fiber_g', models.IntegerField()),
                ('foodType', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='food_images/')),
            ],
        ),
    ]
