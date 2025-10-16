from django.core.management.base import BaseCommand

from utils.support import measure_time_and_memory


class Command(BaseCommand):
    help = "CodeUp 6070"

    @measure_time_and_memory
    def handle(self, *args, **options):
        """
        본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
        ------

        월이 입력될 때 계절 이름이 출력되도록 해보자.

        월 : 계절 이름
        12, 1, 2 : winter
        3, 4, 5 : spring
        6, 7, 8 : summer
        9, 10, 11 : fall

        예시
        ...
        if n//3==1 :
        print("spring")
        ...

        참고
        때때로 수들의 특징을 관찰하고 이용하면 매우 간단히 해결할 수도 있다.
        """
        s = int(input())
        match s:
            case s if s in [12, 1, 2]:
                print('winter')
            case s if s in [3, 4, 5]:
                print('spring')
            case s if s in [6, 7, 8]:
                print('summer')
            case s if s in [9, 10, 11]:
                print('fall')
