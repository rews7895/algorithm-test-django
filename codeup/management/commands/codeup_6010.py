from django.core.management.base import BaseCommand

from utils.support import measure_time_and_memory


class Command(BaseCommand):
    help = "CodeUp 6010"

    @measure_time_and_memory
    def handle(self, *args, **options):
        n = input()
        if n.isdigit():
            print(int(n))
        else:
            print("정수가 아닙니다.")
