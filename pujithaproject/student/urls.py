from django.urls import path

from student import views

urlpatterns = [
path('',views.student_home,name='student_home'),
path('add',views.add_student,name='add_student'),
path('view',views.view_students,name='view_students'),
path('update/<int:id>',views.update_students,name='update_students'),
path('delete/<int:id>',views.delete_students,name='delete_students'),
path('student',views.student_profile,name='student_profile'),
path('available',views.available_drives,name='available_drives'),
path('applied',views.applied_drives,name='applied_drives'),

]