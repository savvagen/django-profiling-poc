# Generated by Django 3.1.4 on 2020-12-22 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('article', '0002_auto_20201222_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='author.author'),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
