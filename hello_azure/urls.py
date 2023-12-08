from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('hello', views.hello, name='hello'),
    # path('', views.index, name='index'),
    # path('reviews', views.show_reviews, name='show_reviews'),
    path('', views.show_reviews, name='show_reviews'),
]