from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "CodeUp 6008"

    def handle(self, *args, **options):
        print('print("Hello\\nWorld")')
