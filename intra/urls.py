from . import views
from django.urls import path



urlpatterns=[

    path('',views.rejoindre, name='rejoindre'),
    path('faq',views.faq, name='faq'),
    path('moncompte',views.moncompte, name='moncompte'),
]
