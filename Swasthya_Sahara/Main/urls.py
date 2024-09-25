from django.urls import path
from . import views 
urlpatterns = [
    path('',views.home,name="home"),
    path('dashboard/',views.user,name="dashboard"),
    path('profile',views.user_profile,name="user_profile"),
    path('profile/doctors/',views.doctors_list,name="doctors_list"),
    
    path('dashboard/chat',views.chat,name="chat"),
    path('blogs',views.blog_home,name='blog-home'),
    path('blog/<int:pk>/',views.blog_post,name='blog_post'),
    path('post/',views.post,name='posts'),
    path('login-redirect/', views.handle_login_redirect, name='login_redirect'),   
    path('chat/', views.chat_view, name='get_response'),
    path('journal/',views.journal_list, name='journal_list'),
    path('journal/delete',views.delete_all_journal_entries, name='delete_journal'),
    
]