
from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name="default" ),
    path('signup',views.signup,name="signup"),
    path('register',views.RegisterAPI.as_view(),name="register"),
    path('articles',views.feedsAll,name="articles"),

]
