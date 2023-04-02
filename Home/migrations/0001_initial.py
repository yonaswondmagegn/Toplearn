# Generated by Django 4.1.7 on 2023-03-04 18:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profile', '0003_alter_profile_grade_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherMatterialsForTheVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='other_matterials_forthevideo')),
                ('description', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('uploder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.profile')),
            ],
        ),
        migrations.CreateModel(
            name='VideoFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('thumbnail', models.ImageField(default='video_thumbnail.jpg', upload_to='thumbnail_field')),
                ('video', models.FileField(upload_to='course_videos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MP4', 'AVI'])])),
                ('description', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('other_matterials', models.ManyToManyField(blank=True, related_name='other_matterial', to='Home.othermatterialsforthevideo')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('thumbnail', models.ImageField(default='course_thumbnail.jpg', upload_to='course_thumbnail')),
                ('description', models.TextField()),
                ('date', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('lectures', models.ManyToManyField(related_name='lectures', to='Profile.profile')),
                ('videos', models.ManyToManyField(related_name='videoFiles', to='Home.videofiles')),
            ],
        ),
    ]
