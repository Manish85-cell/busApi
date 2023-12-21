# myapp/management/commands/my_command.py

from django.core.management.base import BaseCommand
from models import BusStand 

class Command(BaseCommand):
    help = 'Example Django management command'

    def handle(self, *args, **options):
        # Assuming you have a Django model named 'MyModel'
        my_objects = BusStand.objects.filter(name='example')

        # The SQL query would be executed when you access the data
        print(my_objects.query)
        print(list(my_objects))
