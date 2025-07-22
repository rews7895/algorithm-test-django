from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "CodeUp 6009"

    def handle(self, *args, **options):
        c = input()
        print(c)
