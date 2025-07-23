from django.core.management.base import BaseCommand

from utils.support import measure_time_and_memory


class Command(BaseCommand):
    help = "CodeUp 6011"

    @measure_time_and_memory
    def handle(self, *args, **options):
        f = input()
        if f.replace('.', '', 1).isdigit():
            print(float(f))
        else:
            print("실수가 아닙니다.")
