# Generated by Django 3.2.8 on 2022-06-21 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solcareapp', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('person_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=10)),
                ('nic', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=1)),
                ('date_of_birth', models.DateField()),
                ('address', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=20)),
                ('religion', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='employee',
        ),
    ]
