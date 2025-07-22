from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "CodeUp 6002"

    def handle(self, *args, **options):
        print("Hello", "World")
