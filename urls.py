from django.urls import path
from student_list import views
urlpatterns = [
   path('index',views.index,name="index"),
   path('',views.mexico,name="mexico"),
   path('student',views.student,name="student"),
   path('form',views.form,name='form'),
   path('update/<int:id>' ,views.update,name="update"),
]