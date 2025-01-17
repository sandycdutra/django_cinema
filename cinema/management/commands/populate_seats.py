# Automatizando preenchimento do banco de dados
# Enchendo uma sessão de cadeiras

from django.core.management.base import BaseCommand
from cinema.models import Session, Seat

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('session_id', type=int)

    def handle(self, *args, **kwargs):
        session_id = kwargs['session_id']
        try:
            session = Session.objects.get(id=session_id)
            lines = ['A', 'B', 'C', 'D', 'E']
            columns = range(1, 11)

            for line in lines:
                for column in columns:
                    Seat.objects.create(session=session, line=line, column=column)

            self.stdout.write(self.style.SUCCESS(f'Successfully populated seats for session {session_id}'))
        except Session.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Session with ID {session_id} does not exist'))

# Command: python manage.py populate_seats <session_id>