from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Gênero do filme
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Filme e suas informações
class Movie(models.Model):
    title = models.CharField(max_length=200) # Título
    description = models.TextField() # Descrição
    duration = models.IntegerField(default=0)  # Duração em minutos
    #poster = models.ImageField(upload_to='posters/') # Poster
    genres = models.ManyToManyField(Genre) # Gênero
    release_date = models.DateField('release_year') # Ano de lançamento do filme

    def __str__(self):
        return self.title

class MovieTheater(models.Model):
    theater_name = models.CharField(max_length=20) # Nome da sala "Sala 01" por exemplo
    theater_number = models.IntegerField() # Número equivalente ao nome
    capacity = models.IntegerField() # Quantas cadeiras há

    def __str__(self):
        return self.theater_name

class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE) # Nome do filme
    movie_theater = models.ForeignKey(MovieTheater, on_delete=models.CASCADE) # Sala de exibição
    date = models.DateField() # Dia de exibição
    time = models.TimeField() # Horário de exibição

    def __str__(self):
        return f"Sessão de {self.movie.title} - {self.movie_theater.theater_name} - Dia {self.date} às {self.time}"


class Seat(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, default=1000)
    line = models.CharField(max_length=1)
    column = models.CharField(max_length=5)
    STATUS_CHOICES = [
        ('available', 'Disponível'),
        ('unavailable', 'Indisponível'),
    ]
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return f"{self.session.movie}, dia {self.session.date} | {self.session.movie_theater.theater_name} - Cadeira {self.line}{self.column}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    seats = models.ManyToManyField(Seat)
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('confirmed', 'Confirmado'),
        ('cancelled', 'Cancelado'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pendente')

    def __str__(self):
        return f"Reserva de {self.user.username} - {self.session.movie.title}"
