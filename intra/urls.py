from . import views
from django.urls import path

urlpatterns=[

    path('faq',views.faq, name='faq'),
    path('moncompte',views.moncompte, name='moncompte'),
]
