#!/usr/bin/env python3

from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
            artifacts, key=lambda artifact: artifact["power"], reverse=True
            )


def power_filter(
        mages: list[dict[str, Any]], min_power: int
        ) -> list[dict[str, Any]]:
    return list(
            filter(lambda mage: mage["power"] >= min_power, mages)
            )


def spell_transformer(spells: list[str]) -> list[str]:
    return list(
            map(lambda spell: "* " + spell + " *", spells)
            )


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    return {
            "max_power": max(mages, key=lambda mage: mage["power"])["power"],
            "min_power": min(mages, key=lambda mage: mage["power"])["power"],
            "avg_power": round(
                sum(map(lambda mage: mage["power"], mages))
                / len(mages), 2)
            }


def main() -> None:
    artifacts = [
            {'name': 'Crystal Orb', 'power': 83, 'type': 'weapon'},
            {'name': 'Wind Cloak', 'power': 114, 'type': 'weapon'},
            {'name': 'Crystal Orb', 'power': 110, 'type': 'accessory'},
            {'name': 'Crystal Orb', 'power': 107, 'type': 'weapon'}
            ]

    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0].get('name')} "
          f" ({sorted_artifacts[0].get('power')} power) comes before "
          f"{sorted_artifacts[1].get('name')} "
          f"({sorted_artifacts[1].get('power')} power)"
          )

    mages = [
            {'name': 'Kai', 'power': 72, 'element': 'lightning'},
            {'name': 'Alex', 'power': 79, 'element': 'wind'},
            {'name': 'Phoenix', 'power': 59, 'element': 'shadow'},
            {'name': 'Luna', 'power': 50, 'element': 'wind'},
            {'name': 'Ash', 'power': 79, 'element': 'shadow'}
            ]

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(stats)

    spells = ['tsunami', 'freeze', 'meteor', 'blizzard']

    print("\nTesting spell transformer...")
    transformed_spells = spell_transformer(spells)
    print(", ".join(transformed_spells))


if __name__ == "__main__":
    main()
