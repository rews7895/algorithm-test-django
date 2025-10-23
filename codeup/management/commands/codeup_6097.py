from django.core.management.base import BaseCommand

from utils.support import measure_time_and_memory


class Command(BaseCommand):
    help = "CodeUp 6097"

    @measure_time_and_memory
    def handle(self, *args, **options):
        """
        본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
        ------

        부모님과 함께 놀러간 영일이는
        설탕과자(설탕을 녹여 물고기 등의 모양을 만든 것) 뽑기를 보게 되었다.

        길이가 다른 몇 개의 막대를 바둑판과 같은 격자판에 놓는데,

        막대에 있는 설탕과자 이름 아래에 있는 번호를 뽑으면 설탕과자를 가져가는 게임이었다.
        (잉어, 붕어, 용 등 여러 가지가 적혀있다.)

        격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
        막대를 놓는 방향(d:가로는 0, 세로는 1)과
        막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,

        격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.
        """

        h, w = list(map(int, input().split()))
        n = int(input())
        # h, w = [5, 5]
        # n = 3
        a = []
        for i in range(n):
            a.append(list(map(int, input().split())))
        # a.append(list(map(int, '2 0 1 1'.split())))
        # a.append(list(map(int, '3 1 2 3'.split())))
        # a.append(list(map(int, '4 1 2 5'.split())))
        
        r = []
        for i in range(h):
            r.append([0 for i in range(w)])
            
        for i in range(len(a)):
            for j in range(a[i][0]):
                if a[i][1] == 0:
                    r[a[i][2] - 1][a[i][3] + j - 1] = 1
                else: 
                    r[a[i][2] + j - 1][a[i][3] - 1] = 1
        

        for i in range(h):
            for j in range(w):
                print(r[i][j], end=' ')
            print()
        
        
        