from django.core.management.base import BaseCommand

from utils.support import measure_time_and_memory


class Command(BaseCommand):
    help = "CodeUp 6019"

    @measure_time_and_memory
    def handle(self, *args, **options):
        y, m, d = input().split('.')
        print(d, m, y, sep='-')
