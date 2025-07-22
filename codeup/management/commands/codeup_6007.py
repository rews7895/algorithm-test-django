from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "CodeUp 6007"

    def handle(self, *args, **options):
        print('"C:\\Download\\hello\'.py"')
