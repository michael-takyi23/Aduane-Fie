from django.apps import AppConfig
from django.core.management import call_command
from django.db.models.signals import post_migrate


def run_populate_db(sender, **kwargs):
    from django.core.management import BaseCommand
    command = BaseCommand()
    command.handle = lambda *args, **kwargs: call_command('populate_db')
    command.handle()

class BookingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookings'

    def ready(self):
        from .management.commands.populate_db import Command
        post_migrate.connect(run_populate_db, sender=self)


