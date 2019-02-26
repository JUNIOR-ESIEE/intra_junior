from . import views
from django.urls import path

urlpatterns = [
        path('',views.rejoindre, name='rejoindre'),

]
