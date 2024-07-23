from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Movie, Session, Seat, Booking

# Create your views here.

def home(request):
    movies = Movie.objects.all()
    return render(request, 'cinema/home.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    sessions = Session.objects.filter(movie=movie)
    return render(request, 'cinema/movie_detail.html', {'movie': movie, 'sessions': sessions})

def session_detail(request, movie_id, session_id):
    session = get_object_or_404(Session, id=session_id)
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(session=session)
    return render(request, 'cinema/session_detail.html', {'session': session, 'seats': seats})

def book_seat(request, session_id, seat_id):
    session = get_object_or_404(Session, id=session_id)
    seat = get_object_or_404(Seat, id=seat_id)
    if request.method == 'POST':
        # Lógica de reserva
        booking = Booking.objects.create(user=request.user, session=session)
        booking.seats.add(seat)
        booking.status = 'confirmed'
        booking.save()
        seat.status = 'unavailable'
        seat.save()
        return render(request, 'cinema/booking_confirmation.html', {'booking': booking})
    return render(request, 'cinema/book_seat.html', {'session': session, 'seat': seat})

def about(request):
    return render(request, 'cinema/about.html')