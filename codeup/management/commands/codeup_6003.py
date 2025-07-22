from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "CodeUp 6003"

    def handle(self, *args, **options):
        print("Hello")
        print("World")
