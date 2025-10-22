from django.core.management.base import BaseCommand

from utils.support import measure_time_and_memory


class Command(BaseCommand):
    help = "CodeUp 6079"

    @measure_time_and_memory
    def handle(self, *args, **options):
        """
        본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
        ------

        1, 2, 3 ... 을 계속 더해 나갈 때,
        그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만
        계속 더하는 프로그램을 작성해보자.

        즉, 1부터 n까지 정수를 계속 더해 나간다고 할 때,
        어디까지 더해야 입력한 수보다 같거나 커지는 지를 알아보고자하는 문제이다.
        """
        s = int(input())
        result = 0
        for i in range(s):
            if result >= s:
                result = i
                break
            result = result + i
            print(result)
            
        print(result)
