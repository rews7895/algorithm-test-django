from django.core.management.base import BaseCommand

from utils.support import measure_time_and_memory


class Command(BaseCommand):
    help = "CodeUp 6075"

    @measure_time_and_memory
    def handle(self, *args, **options):
        """
        본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
        ------

        정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.
        """
        s = int(input())
        i = 0
        while i <= s:
            print(i)
            i = i + 1
