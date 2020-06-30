from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("apartments", views.apartments, name="apartments"),
    path("<int:apartment_id>", views.apartment, name="apartment"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("book", views.book, name="book"),
    path("bookings", views.bookings, name="bookings"),
    path("about", views.about, name="about"),
    path("search", views.search, name="search"),
]