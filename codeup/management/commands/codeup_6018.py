from django.core.management.base import BaseCommand

from utils.support import measure_time_and_memory


class Command(BaseCommand):
    help = "CodeUp 6018"

    @measure_time_and_memory
    def handle(self, *args, **options):
        a, b = input().split(':')
        # sep: seperator의 약자
        print(a, b, sep=':')
