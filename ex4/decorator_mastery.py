import time
import functools
from typing import Any
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def time_execution(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return res

    return time_execution


def power_validator(min_power: int) -> Callable:
    def validate_power(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            if args:
                power = args[0]
            else:
                power = kwargs.get("power")
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return validate_power


def retry_spell(max_attempts: int) -> Callable:
    def recite(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for i in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                            f"Spell failed, retrying... "
                            f"(attempt {i + 1}/{max_attempts})"
                            )
                    continue
                return "Spell casting failed after max_attempts attempts"
        return wrapper
    return recite

