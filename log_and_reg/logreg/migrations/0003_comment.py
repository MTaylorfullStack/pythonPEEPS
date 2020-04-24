# Generated by Django 2.2 on 2020-04-24 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logreg', '0002_wall_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to='logreg.User')),
                ('wall_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='logreg.Wall_Message')),
            ],
        ),
    ]