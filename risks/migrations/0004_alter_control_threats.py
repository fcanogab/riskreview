# Generated by Django 5.1.1 on 2024-09-17 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risks', '0003_alter_category_components_alter_category_threats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='control',
            name='threats',
            field=models.ManyToManyField(related_name='controls', to='risks.threat'),
        ),
    ]
