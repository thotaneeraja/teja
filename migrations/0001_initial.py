# Generated by Django 4.0 on 2022-01-04 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('costperitem', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stockquantity', models.DecimalField(decimal_places=3, max_digits=10)),
                ('volume', models.BigIntegerField(null=True)),
            ],
        ),
    ]
