#!/usr/bin/env python3

import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    operations: dict[str, Callable[[int, int], int]] = {
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


def partial_enchanter(base_enchantment: Callable[..., str]) -> dict[str, Callable[..., str]]:
    fire_enchanter = functools.partial(
            base_enchantment, power=50, element="fire"
            )
    ice_enchanter = functools.partial(
            base_enchantment, power=50, element="ice"
            )
    wind_enchanter = functools.partial(
            base_enchantment, power=50, element="wind"
            )

    return {
            "Fire": fire_enchanter,
            "Ice": ice_enchanter,
            "Wind": wind_enchanter
            }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError(
                "Fibonacci sequence is undefined for negative numbers."
                )

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
    def _(spell: list[Any]) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatcher


def main() -> None:
    spell_powers = [10, 20, 30, 40]

    print(f"Testing spell reducer...(with {spell_powers})")
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
    print(f"Max: {spell_reducer(spell_powers, 'max')}")

    print("\nTesting partial enchanter...")

    def base_spell(power: int, element: str, target: str) -> str:
        return f"Cast {element} on {target} with {power} power"

    enchanters = partial_enchanter(base_spell)
    print(enchanters["Fire"](target="Dragon"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch(["fire", "ice", "wind"]))
    print(dispatch(3.14))


if __name__ == "__main__":
    main()
