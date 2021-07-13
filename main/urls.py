
from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.home),
    path('blog/', views.blog),

]