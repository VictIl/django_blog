
from django.urls import path, re_path
 
from .views import * 
 
urlpatterns = [
   # path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), 
   # path('genres/<int:genre_id>/', genres),
   # re_path(r'^date/(?P<year>[0-9]{4})/', date),

    #path('home/', home_v, name='home'),
    path('home/', MovieMain.as_view(), name='home'),
   # path('home/', BlogListView.as_view(), name='home'),
    path('',index,name='index'),
    path('test/<int:pk>/', testd,name='test'),
   # path('login/', login_ref,name='login'),
    path('login/', LoginUser.as_view(),name='login'),
     path('logout/', logout_user,name='logout'),
    #path('register/', register,name='register'),
    path('signup/', SignUp.as_view(),name='signup'),
      #path('add/', add_v,name='add'),
      path('add/', add_v.as_view(),name='add'),
    path('rate/<int:rating_id>/', rate_v,name='rate'),
       


]