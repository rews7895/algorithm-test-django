from django.core.management.base import BaseCommand

from utils.support import measure_time_and_memory


class Command(BaseCommand):
    help = "CodeUp 6020"

    @measure_time_and_memory
    def handle(self, *args, **options):
        a = input().split('-')
        print(a[0], a[1], sep='')
