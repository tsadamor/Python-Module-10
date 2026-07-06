#!/usr/bin/env python3

from collections.abc import Callable


def spell_combiner(
        spell1: Callable[[str, int], str], spell2: Callable[[str, int], str]
        ) -> Callable[[str, int], tuple[str, str]]:
    def combine_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return combine_spell


def power_amplifier(
        base_spell: Callable[[str, int], str], multiplier: int
        ) -> Callable[[str, int], str]:
    def amplify_power(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplify_power


def conditional_caster(
        condition: Callable[[str, int], bool], spell: Callable[[str, int], str]
        ) -> Callable[[str, int], str]:
    def cast_conditionally(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"

    return cast_conditionally


def spell_sequence(
        spells: list[Callable[[str, int], str]]
        ) -> Callable[[str, int], list[str]]:
    def order_spells(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return order_spells


def avada_kedabra(target: str, power: int) -> str:
    return f"{target} dies {power} times"


def expelliarmus(target: str, power: int) -> str:
    return f"{target} loses {power} weapons"


def main() -> None:
    test_values = [25, 20, 17]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    print("\nTesting spell combiner...")
    combined = spell_combiner(avada_kedabra, expelliarmus)
    result = combined(test_targets[0], test_values[0])
    print(f"Combined spell result: {result}")

    print("\nTesting power amplifier...")
    amplified = power_amplifier(avada_kedabra, 3)
    print(f"Original power: {test_values[1]}")
    print(f"Amplifird power: {amplified(test_targets[1], test_values[1])}")

    print("\nTesting conditional caster...")
    conditional_spell = conditional_caster(
            lambda target, power: power >= 20, expelliarmus
            )
    print(f"Success case (power 30): {conditional_spell('Voldemort', 30)}")
    print(f"Failed case (power 15): {conditional_spell('Voldemort', 15)}")

    print("\nTesting spell sequence...")
    sequence = spell_sequence([avada_kedabra, expelliarmus])
    print(f"{sequence('Wizard', 10)}")


if __name__ == "__main__":
    main()
