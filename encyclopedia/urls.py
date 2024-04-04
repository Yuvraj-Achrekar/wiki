from django.urls import path

from . import views

app_name = 'wiki'

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/create", views.create, name="create"),
    path("wiki/<str:name>", views.entry, name="entry"),
    path("wiki/search/<str:query>", views.search, name="search"),
]
