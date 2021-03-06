# Generated by Django 3.0.7 on 2020-07-23 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(default='', max_length=50)),
                ('rollno', models.CharField(default='', max_length=20)),
                ('gpa', models.CharField(default='', max_length=5)),
                ('phn', models.CharField(default='', max_length=12)),
                ('res', models.FileField(default='', upload_to='static/info')),
            ],
        ),
    ]
