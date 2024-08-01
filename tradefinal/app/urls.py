from django.urls import path
from .views import landing,contact_list,contact_create,contact_delete,contact_update, cadastro_clientes,demonstrativo_tabelas,realizar_venda, login_view, register_view, logout_view

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/',register_view, name='register'),
    path('home/', landing, name='landing'),
    path('create/', contact_create, name='contact_create'),
    path('list/', contact_list, name='contact_list'),
    path('update/<int:pk>', contact_update, name='contact_update'),
    path('delete/<int:pk>', contact_delete, name='contact_delete'),
    path('cadastro_clientes/', cadastro_clientes, name='cadastro_clientes'),
    path('demonstrativo_tabelas/', demonstrativo_tabelas, name='demonstrativo_tabelas'),
    path('realizar_venda/', realizar_venda, name='realizar_venda'),

]
