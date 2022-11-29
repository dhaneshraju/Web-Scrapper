from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('jobs/', views.jobs, name='jobs'),
    path('jobs/search/', views.search, name='jobs'),
    path('movie/', views.movie, name='movie'),
    path('movie/trend/', views.trendingmovies, name='movie'),
    path('movie/genre/', views.genres, name='movie'),
    path('movie/popular/', views.populars, name='movie'),
    path('insta/', views.insta, name='insta'),
    path('insta/hashtag/', views.insta_hashtag, name='insta'),
    path('insta/user/', views.insta_user, name='insta'),
    path('insta/hashtag/hashtags/', views.target_hashtag, name='insta'),
    path('insta/user/users/', views.target_user, name='insta'),
    path('ads/', views.ads, name='ads'),
    path('ads/new_search/', views.new_search, name='add'),
    path('linkedin/', views.linkedin, name='linkedin'),
    path('linkedin/profile/userprofile/', views.linkedin_profile, name='linkedin'),
    path('linkedin/profile/', views.profile, name='linkedin'),
    path('linkedin/company/', views.company, name='linkedin'),
    path('linkedin/company/companys/', views.linkedin_company, name='linkedin'),
    path('linkedin/demo/', views.demo_linkedin, name='linkedin'),
    path('linkedin/demo/demos', views.linkedin_demo, name='linkedin'),
]
