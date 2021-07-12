from django.urls import path
from . import views
urlpatterns = [
    path('',views.index1,name="index1"),
    path('upImages',views.upImages,name="upImages")
   #path('register',views.index,name="register")
]