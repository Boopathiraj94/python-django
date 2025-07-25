# Generated by Django 5.2.4 on 2025-07-14 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=250)),
                ('student_phone', models.CharField(max_length=20, null=True)),
                ('student_class', models.CharField(max_length=20, null=True)),
                ('student_section', models.CharField(max_length=20, null=True)),
                ('student_email', models.EmailField(max_length=200, null=True)),
                ('student_address', models.TextField(null=True)),
            ],
        ),
    ]
