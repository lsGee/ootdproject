# Generated by Django 3.1 on 2020-08-26 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.IntegerField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=10, verbose_name='시군구명')),
                ('city_lat', models.FloatField(default=0.0)),
                ('city_lng', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Sido',
            fields=[
                ('sido_id', models.IntegerField(primary_key=True, serialize=False)),
                ('sido_name', models.CharField(max_length=10, verbose_name='시도명')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=10, verbose_name='작성자')),
                ('image_like', models.IntegerField(default=0)),
                ('image_dislike', models.IntegerField(default=0)),
                ('image_cnt', models.IntegerField(default=0)),
                ('image_date', models.DateTimeField(auto_now_add=True)),
                ('image_file', models.FileField(blank=True, upload_to='photo_%Y_%m_%d')),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.city')),
                ('sido_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.sido')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='sido_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.sido'),
        ),
    ]
