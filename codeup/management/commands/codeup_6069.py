from django.core.management.base import BaseCommand

from utils.support import measure_time_and_memory


class Command(BaseCommand):
    help = "CodeUp 6069"

    @measure_time_and_memory
    def handle(self, *args, **options):
        """
        본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
        ------

        평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.

        평가 내용
        평가 : 내용
        A : best!!!
        B : good!!
        C : run!
        D : slowly~
        나머지 문자들 : what?
        """
        s = input()
        match s:
            case s if s == 'A':
                print('best!!!')
            case s if s == 'B':
                print('good!!')
            case s if s == 'C':
                print('run!')
            case s if s == 'D':
                print('slowly~')
            case s if s != 'A' and s != 'B' and s != 'C' and s != 'D':
                print('what?')
                
