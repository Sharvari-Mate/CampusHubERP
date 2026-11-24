
import time
from functools import wraps


def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function Started")

        try:
            return func(*args, **kwargs)
        finally:
            print("Function Completed")

    return wrapper


def time_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        end_time = time.perf_counter()

        print("Execution Time:", end_time - start_time, "seconds")

        return result

    return wrapper
