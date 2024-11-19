from django.urls import path
from . import views
app_name = 'pages'
urlpatterns = [
    path('',views.emp_list,name='home'),
    path('detail/<int:id>',views.emp_detail,name='detail'),
    path('update/<int:id>',views.emp_update,name='update'),
    path('delete/<int:id>',views.emp_delete,name='delete'),
    path('create/',views.emp_create,name='create'),
    
]