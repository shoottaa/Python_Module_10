def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact['power'],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        'max_power': max(mages, key=lambda x: x['power']),
        'min_power': min(mages, key=lambda x: x['power']),
        'avg_power': sum(mage['power'] for mage in mages) / len(mages)
    }


if __name__ == "__main__":
    print("\nTesting artifact sorter...")
    artifacts = [
        {'name': 'Fire Staff', 'power': 92},
        {'name': 'Crystal Orb', 'power': 85}
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    first = sorted_artifacts[0]
    second = sorted_artifacts[1]
    print(f"{first['name']} ({first['power']} power) comes before "
          f"{second['name']} ({second['power']} power)")

    print("\nTesting spell transformer...")
    spells = ['fireball', 'heal', 'shield']
    transformed = spell_transformer(spells)
    print(' '.join(transformed))

    print("\nTesting power filter...")
    mages = [
        {'name': 'Gandalf', 'power': 95},
        {'name': 'Merlin', 'power': 80},
        {'name': 'Apprentice', 'power': 30}
    ]
    powerful = power_filter(mages, 75)
    print(f"Mages with power >= 75: {[m['name'] for m in powerful]}")

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    max_mage = stats['max_power']
    min_mage = stats['min_power']
    print(f"Strongest: {max_mage['name']} ({max_mage['power']})")
    print(f"Weakest: {min_mage['name']} ({min_mage['power']})")
    print(f"Average power: {stats['avg_power']:.1f}")
