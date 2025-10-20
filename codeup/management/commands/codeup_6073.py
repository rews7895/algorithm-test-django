from django.core.management.base import BaseCommand

from utils.support import measure_time_and_memory


class Command(BaseCommand):
    help = "CodeUp 6073"

    @measure_time_and_memory
    def handle(self, *args, **options):
        """
        본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다.
        ------

        정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

        while 조건식 :
        ...
        ...

        반복 실행구조를 사용해 보자.

        참고
        조건검사, 출력, 감소의 순서와 타이밍을 잘 생각해보자.
        """
        s = int(input())
        while s > 0:
            s = s - 1
            print(s)

