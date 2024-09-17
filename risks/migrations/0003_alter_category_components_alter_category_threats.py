# Generated by Django 5.1.1 on 2024-09-17 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risks', '0002_alter_implementedcontrol_control'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='components',
            field=models.ManyToManyField(blank=True, related_name='categories', to='risks.component'),
        ),
        migrations.AlterField(
            model_name='category',
            name='threats',
            field=models.ManyToManyField(blank=True, related_name='categories', to='risks.threat'),
        ),
    ]
