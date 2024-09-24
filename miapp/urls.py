from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index,name="index"),
    path('tarea/',views.tarea,name="tarea"),
    path('tarea/completed',views.tarea_completed,name='tarea_completed'),
    path('tarea_nueva/', views.tareas_nuevas,name="tarea_nueva"),
    path('tarea_detail/<int:tareas_id>/', views.tarea_detail,name="tarea_detail"),
    path('tarea_detail/<int:tareas_id>/complete/', views.complete_tarea,name="complete_tarea"),
    path('tarea_detail/<int:tareas_id>/delete/', views.delete_tarea,name="delete_tarea"),
    path('signup/', views.sign_up,name="sign_up"),
    path('logout/', views.sign_out,name="log_out"),
    path('signin/', views.sign_in,name="sign_in")
]
