from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.hashers import make_password

import json



class Command(BaseCommand):
    help = "Closes the specified poll for voting"


    def handle(self, *args, **options):
        pass

