
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('category/<int:id>/',views.category_detail, name='category_detail'),
    path('category/',views.category_list, name='category_list'),
    path('login',views.login,name='login'),
    path('logout',views.log_out,name='logout'),
    path('signup',views.signup,name='signup'),
    path('tag/<int:id>/',views.tag_detail, name='tag_detail'),
    path('tag/',views.tag_list, name='tag_list'),
    path('profile/',views.user_profile,name='user_profile'),
    path('profile-detail/',views.profile_update,name='profile_update'),
]

