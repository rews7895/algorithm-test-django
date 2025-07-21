import time
import tracemalloc
from functools import wraps


def measure_time_and_memory(func):
    """
    함수의 실행 시간과 메모리 사용량을 측정하는 데코레이터
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"[{func.__name__}] 실행 시간: {end_time - start_time:.4f}초")
        print(
            f"[{func.__name__}] 메모리 사용량: 현재 {current / 1024:.2f}KB, 최대 {peak / 1024:.2f}KB"
        )
        return result

    return wrapper
