import time
import tracemalloc
from functools import wraps


def _format_time(seconds):
    """실행 시간을 일, 시, 분, 초로 변환합니다."""
    if seconds < 60:
        return f"{seconds:.4f}초"

    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)

    d, h, m = int(d), int(h), int(m)

    parts = []
    if d > 0:
        parts.append(f"{d}일")
    if h > 0:
        parts.append(f"{h}시간")
    if m > 0:
        parts.append(f"{m}분")

    parts.append(f"{s:.4f}초")
    return " ".join(parts)


def _format_memory(size_in_bytes):
    """메모리 사용량을 B, KB, MB, GB, TB, PB 단위로 변환합니다."""
    if size_in_bytes == 0:
        return "0B"
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    i = 0
    size = float(size_in_bytes)
    while size >= 1024 and i < len(units) - 1:
        size /= 1024
        i += 1
    return f"{size:.2f}{units[i]}"


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

        elapsed_time = end_time - start_time
        print(f"[{func.__name__}] 실행 시간: {_format_time(elapsed_time)}")
        print(
            f"[{func.__name__}] 메모리 사용량: 현재 {_format_memory(current)}, 최대 {_format_memory(peak)}"
        )
        return result

    return wrapper
