from django.urls import path, include

from education import views

urlpatterns = [
    path('', views.MainPage.as_view(), name="main_page"),
    path('category/<slug:cat_slug>/', views.ShowCategory.as_view(), name='show_category'),
    path('search/', views.Search.as_view(), name='search'),
]
