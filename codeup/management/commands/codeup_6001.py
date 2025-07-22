from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "CodeUp 6001"

    def handle(self, *args, **options):
        print("Hello")
