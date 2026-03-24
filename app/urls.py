from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('keywords/', add_keyword),
    path('scan/', scan),
    path('flags/', get_flags),
    path('flags/<int:pk>/', update_flag),
]