from django.db import models
from django.urls import reverse


class City(models.Model):
    name = models.CharField(verbose_name="Название города", max_length=150)
    slug = models.SlugField(max_length=150)




    def get_absolute_url(self):
        return reverse("university:city_list", args=[self.slug])

    def __str__(self):
        return self.name

class University(models.Model):
    name = models.CharField(verbose_name="Название вуза", help_text="Например: КФУ", max_length=20)
    fullname = models.CharField(verbose_name="Полное название вуза", help_text="Например: Казанский федеральный университет", max_length=255)
    slug = models.SlugField(max_length=20)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(verbose_name="Место в рейтинге", unique=True)
    is_active = models.BooleanField(default=True)
    logo = models.ImageField(
        verbose_name=("image"),
        help_text=("Upload a product image"),
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name=("Alturnative text"),
        help_text=("Please add alturnative text"),
        max_length=255,
        null=True,
        blank=True,
    )
    
    def get_absolute_url(self):
        return reverse("university:university_list", args=[self.slug])

    def __str__(self):
        return self.name



class BenefitsBoolean(models.Model):
    univers = models.OneToOneField(University, on_delete=models.CASCADE, related_name="benefits_univers")
    state_univers = models.BooleanField(verbose_name="Государственный вуз?")
    arm_univers = models.BooleanField(verbose_name="Есть военная кафедра?")
    tech_univers = models.BooleanField(verbose_name="Технический вуз?")
    humanitarian_univers = models.BooleanField(verbose_name="Гуманитарный вуз?")
    hostel_univers = models.BooleanField(verbose_name="Есть общежитие?")


class StateAndPaidInfo(models.Model):
    univers = models.OneToOneField(University, on_delete=models.CASCADE, related_name="info_stateandpaid")
    state_price = models.PositiveIntegerField(verbose_name="Средняя стоимость бюдж. обучения")
    state_point = models.PositiveIntegerField(verbose_name="Средний балл бюдж. обучения")
    state_place = models.PositiveIntegerField(verbose_name="Сред. кол-во бюдж мест")
    paid_price = models.PositiveIntegerField(verbose_name="Средняя стоимость плат. обучения")
    paid_point = models.PositiveIntegerField(verbose_name="Средний балл плат. обучения")
    paid_place = models.PositiveIntegerField(verbose_name="Сред. кол-во платных мест")

class Hostel(models.Model):
    univers = models.ForeignKey(University, on_delete=models.CASCADE, related_name="hostel_univers")
    name = models.CharField(verbose_name="Название общежития", max_length=150)
    date = models.PositiveSmallIntegerField(verbose_name="Год основания")
    address = models.TextField(verbose_name="Адрес")
    link_address = models.TextField(verbose_name="Сслыка на адрес")
