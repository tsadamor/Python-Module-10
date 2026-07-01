from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combine_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return combine_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplify_power(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplify_power


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast_conditionally(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"

    return cast_conditionally


def spell_sequence(spells: list[Callable]) -> Callable:
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
    print(f"{combined(test_targets[0], test_values[0])}")

    print("\nTesting power amplifier...")
    amplified = power_amplifier(avada_kedabra, 3)
    print(f"{amplified(test_targets[1], test_values[1])}")


if __name__ == "__main__":
    main()
