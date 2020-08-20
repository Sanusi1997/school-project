from django.urls import include,path
from members import views

urlpatterns = [
    path('teachers/', views.Teacher_List.as_view()),
    path('teachers/<int:pk>/', views.Teacher_Detail.as_view()),
    path('students/', views.Student_List.as_view()),
    path('students/<int:pk>/', views.Student_Detail.as_view()),

]
urlpatterns += [
    path('login/', include('rest_framework.urls')),
]

