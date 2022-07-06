from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name="home page"),
    path('courses',views.Courses,name="Courses"),
    path('<int:course_id>/', views.details,name="details")
]
