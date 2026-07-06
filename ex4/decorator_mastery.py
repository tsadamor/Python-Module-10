#!/usr/bin/env python3

import time
import functools
from typing import Any
from collections.abc import Callable


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def time_execution(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return res

    return time_execution


def power_validator(min_power: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def validate_power(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if "power" in kwargs:
                power = kwargs["power"]
            elif args:
                power = args[0]
            else:
                return "Power argument is missed"

            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return validate_power


def retry_spell(max_attempts: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def recite(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for i in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                            f"Spell failed, retrying... "
                            f"(attempt {i + 1}/{max_attempts})"
                            )
                    continue
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return recite


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast spell_name with {power} power"


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(1.0)
        return "Result: Fireball cast!"

    print(fireball())

    print("\nTesting retrying spell...")

    @retry_spell(max_attempts=3)
    def failing_spell() -> Any:
        raise ValueError("Boom!")

    @retry_spell(max_attempts=3)
    def success_spell() -> str:
        return "Waaaaaaagh spelled !"

    print(failing_spell())
    print()
    print(success_spell())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Alex"))
    print(guild.validate_mage_name("A!"))

    print(guild.cast_spell(spell_name="Lightning", power=15))
    print(guild.cast_spell(spell_name="Lightning", power=5))


if __name__ == "__main__":
    main()
