from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('student_list_create/', views.StudentListCreate.as_view()),
    path('student_retrieve_update_destroy/<int:pk>/', 
         views.StudentRetrieUpdateDestroy.as_view()),
]

