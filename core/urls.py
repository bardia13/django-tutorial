from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('question/<int:question_id>/', views.detail, name='detail'),
    path('question/<int:question_id>/results/', views.result, name='results'),
    path('question/<int:question_id>/vote/', views.result, name='results'),

]