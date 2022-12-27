from django.urls import path

from . import views

app_name = "university"

urlpatterns = [
    path("api/", views.UniversityListView.as_view(), name="university_home"),
    path("api/<slug:slug>/", views.Product.as_view(), name="university_page"),
]