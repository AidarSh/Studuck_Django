# Generated by Django 4.1.3 on 2022-11-15 14:36

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название города')),
                ('slug', models.SlugField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_text', models.BooleanField(verbose_name='Есть общежитие?')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Например: КФУ', max_length=20, verbose_name='Название вуза')),
                ('fullname', models.CharField(help_text='Например: Казанский федеральный университет', max_length=255, verbose_name='Полное название вуза')),
                ('slug', models.SlugField(max_length=20)),
                ('rating', models.PositiveSmallIntegerField(unique=True, verbose_name='Место в рейтинге')),
                ('is_active', models.BooleanField(default=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.city')),
            ],
        ),
        migrations.CreateModel(
            name='StateAndPaidInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_price', models.PositiveSmallIntegerField(verbose_name='Средняя стоимость бюдж. обучения')),
                ('state_point', models.PositiveSmallIntegerField(verbose_name='Средний балл бюдж. обучения')),
                ('state_place', models.PositiveSmallIntegerField(verbose_name='Сред. кол-во бюдж мест')),
                ('paid_price', models.PositiveSmallIntegerField(verbose_name='Средняя стоимость плат. обучения')),
                ('paid_point', models.PositiveSmallIntegerField(verbose_name='Средний балл плат. обучения')),
                ('paid_place', models.PositiveSmallIntegerField(verbose_name='Сред. кол-во платных мест')),
                ('univers', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='info_stateandpaid', to='university.university')),
            ],
        ),
        migrations.CreateModel(
            name='BenefitsBoolean',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_univers', models.BooleanField(verbose_name='Государственный вуз?')),
                ('arm_univers', models.BooleanField(verbose_name='Есть военная кафедра?')),
                ('tech_univers', models.BooleanField(verbose_name='Технический вуз?')),
                ('humanitarian_univers', models.BooleanField(verbose_name='Гуманитарный вуз?')),
                ('hostel_univers', models.BooleanField(verbose_name='Есть общежитие?')),
                ('univers', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='benefits_univers', to='university.university')),
            ],
        ),
    ]
