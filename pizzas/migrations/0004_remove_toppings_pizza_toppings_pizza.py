# Generated by Django 4.0.6 on 2022-07-15 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_rename_text_toppings_topping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toppings',
            name='pizza',
        ),
        migrations.AddField(
            model_name='toppings',
            name='pizza',
            field=models.ManyToManyField(to='pizzas.pizza'),
        ),
    ]
