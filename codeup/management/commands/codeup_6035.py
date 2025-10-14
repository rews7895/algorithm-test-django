from django.core.management.base import BaseCommand

from utils.support import measure_time_and_memory


class Command(BaseCommand):
    help = "CodeUp 6035"

    @measure_time_and_memory
    def handle(self, *args, **options):
        """
        본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
        ------

        실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자.

        예시
        ...
        m = f1 * f2
        print(m)

        참고
        수 * 수는 곱(multiplication)이 계산된다.
        """
        s = input().split(' ')
        print(float(s[0]) * float(s[1]))
