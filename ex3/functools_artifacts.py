import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
            "add": operator.add,
            "multiply": operator.mul,
            "max": max,
            "min": min
            }
    if not spells:
        return 0

    try:
        return functools.reduce(operations[operation], spells)

    except KeyError:
        raise ValueError(f"Unknown operation: {operation}")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire_enchanter = functools.partial(base_enchantment, power=50, element="fire")
    ice_enchanter = functools.partial(base_enchantment, power=50, element="ice")
    wind_enchanter = functools.partial(base_enchantment, power=50, element="wind")

    return {
            "Fire": fire_enchanter,
            "Ice": ice_enchanter,
            "Wind": wind_enchanter
            }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Fibonacci sequence is not defined for negative numbers.")

    if n == 0:
        return 0
    if n == 1:
        return 1

    return memoized_fibonacci(n - 2) + memoized_fibonacci(n - 1)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatcher(spell: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatcher.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatcher.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatcher



def main() -> None:
    spell_powers = [40, 47, 25, 15, 17, 14]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [18, 14, 9]

    print(spell_reducer(spell_powers, "add"))


if __name__ == "__main__":
    main()
