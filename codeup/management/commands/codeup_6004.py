from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "CodeUp 6004"

    def handle(self, *args, **options):
        print("'Hello'")
