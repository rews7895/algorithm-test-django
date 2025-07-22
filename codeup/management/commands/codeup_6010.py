from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "CodeUp 6010"

    def handle(self, *args, **options):
        n = input()
        if n.isdigit():
            print(int(n))
        else:
            print("정수가 아닙니다.")
