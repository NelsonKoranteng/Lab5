from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('post/<int:id>/', views.view_post, name='view_post'),
    path('create/', views.create_post, name='create_post'),
    path('post/<int:id>/edit/', views.update_post, name='update_post'),
    path('post/<int:id>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:id>/add_comment/', views.add_comment, name='add_comment'),
    path('login/', views.login_user, name='login'),  # Corrected view name
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
]
