from django.core.management.base import BaseCommand

from utils.support import measure_time_and_memory


class Command(BaseCommand):
    help = "CodeUp 6007"

    @measure_time_and_memory
    def handle(self, *args, **options):
        print('"C:\\Download\\hello\'.py"')
