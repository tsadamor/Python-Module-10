from collections.abc import Callable


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def accumulator(power_to_add: int) -> int:
        nonlocal total_power
        total_power += power_to_add
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant_item(item: str) -> str:
        return f"{enchantment_type} {item}"

    return enchant_item


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: int) -> None:
        memory[key] = value

    def recall(key: str) -> int | str:
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    frame_factory = enchantment_factory("Flaming")
    print(f"{frame_factory('Sword')}")


if __name__ == "__main__":
    main()
