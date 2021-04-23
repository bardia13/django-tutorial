from django.urls import path
from .views import detail, person_list, person_detail

urlpatterns = [
    path('<int:pk>/', detail),
    path('person/', person_list, name="person_list"),
    path('person/<int:pk>/', person_detail, name="person_detail")
]