from django.urls import path
from django.views.generic import TemplateView
from home.views import (IndexView,
                        CategoriesView,
                        DetailProductView,
                        TypeView)


app_name = "home"


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('all/', CategoriesView.as_view(), name="all"),
    path('product/<int:pk>/', DetailProductView.as_view(), name="product"),
    
    path('about/', TemplateView.as_view(template_name="index/about.html"), name="about"),
    path('contact/', TemplateView.as_view(template_name="index/contact.html"), name="contact"),
    
    path('product/<str:category>/', TypeView.as_view(), name="category"),
]
