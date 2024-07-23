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
    genres = models.ManyToManyField(Genre) # Gênero
    release_date = models.DateField('release_year') # Ano de lançamento do filme

    def __str__(self):
        return self.title

# Salas de cinema
class MovieTheater(models.Model):
    theater_name = models.CharField(max_length=20) # Nome da sala "Sala 01" por exemplo
    theater_number = models.IntegerField() # Número equivalente ao nome
    capacity = models.IntegerField() # Quantas cadeiras há

    def __str__(self):
        return self.theater_name

# Sessão
class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE) # Nome do filme
    movie_theater = models.ForeignKey(MovieTheater, on_delete=models.CASCADE) # Sala de exibição
    date = models.DateField() # Dia de exibição
    time = models.TimeField() # Horário de exibição

    def __str__(self):
        return f"Sessão de {self.movie.title} - {self.movie_theater.theater_name} - Dia {self.date} às {self.time}"

# Cadeira da sala
class Seat(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, default=1000) # Sessão a que se refere a cadeira
    line = models.CharField(max_length=1) # Linha da cadeira (A, B, C, D ou E)
    column = models.CharField(max_length=5) # Coluna da cadeira (de 1 a 10)
    STATUS_CHOICES = [
        ('available', 'Disponível'),
        ('unavailable', 'Indisponível'),
    ]
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return f"{self.session.movie}, dia {self.session.date} | {self.session.movie_theater.theater_name} - Cadeira {self.line}{self.column}"

# Reserva da cadeira
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Quem reserva
    session = models.ForeignKey(Session, on_delete=models.CASCADE) # Sessão corespondente
    seats = models.ManyToManyField(Seat) # Cadeiras reservadas
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('confirmed', 'Confirmado'),
        ('cancelled', 'Cancelado'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pendente')

    def __str__(self):
        return f"Reserva de {self.user.username} - {self.session.movie.title}"
