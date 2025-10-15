from django.core.management.base import BaseCommand

from utils.support import measure_time_and_memory


class Command(BaseCommand):
    help = "CodeUp 6058"

    @measure_time_and_memory
    def handle(self, *args, **options):
        """
        본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
        ------

        2개의 정수값이 입력될 때,
        그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력하는 프로그램을 작성해보자.
        """
        a, b = map(int, input().split())
        print(not a and not b)
