from django.contrib import admin

# Register your models here.

from .models import Movie, Genre, MovieTheater, Session, Seat, Booking

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(MovieTheater)
admin.site.register(Session)
admin.site.register(Seat)
admin.site.register(Booking)