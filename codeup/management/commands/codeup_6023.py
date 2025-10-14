from django.core.management.base import BaseCommand

from utils.support import measure_time_and_memory


class Command(BaseCommand):
    help = "CodeUp 6023"

    @measure_time_and_memory
    def handle(self, *args, **options):
        """
        본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
        ------

        시:분:초 형식으로 시간이 입력될 때 분만 출력해보자.

        어떻게 분만 출력해야 할지 주의 깊게 생각해야한다.
        """
        s = input()
        a = s.split(':')
        print(a[1])
