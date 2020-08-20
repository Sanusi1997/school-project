from django.urls import path
from members import views

urlpatterns = [
    path('members/', views.Teacher_List.as_view()),
    path('members/<int:pk>/', views.Teacher_Detail.as_view()),
]
