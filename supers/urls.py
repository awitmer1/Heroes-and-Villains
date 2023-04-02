from django.urls import path
from . import views

## Reflect ending of URL paths + link to API Views ##
## App URLs = Endpoint URLs ##
urlpatterns = [
    path('', views.supers_list),
    path('<int:pk>/', views.super_detail),
]