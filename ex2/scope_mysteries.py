def mage_counter() -> callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> callable:
    power = initial_power

    def accumulator(spell_power: int):
        nonlocal power
        power += spell_power
        return power
    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    def enchantment(item: str):
        return f"{enchantment_type} {item}"
    return enchantment


def memory_vault() -> dict[str, callable]:
    vault = {}

    def store(name: str, spell: callable):
        vault[name] = spell

    def recall(name: str) -> callable:
        return vault.get(name, lambda: "Memory not found")
    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("\nTesting mage counter...")
    counter = mage_counter()
    print(counter())
    print(counter())

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(10)
    print(accumulator(5))
    print(accumulator(3))

    print("\nTesting enchantment factory...")
    fire_enchant = enchantment_factory("Fire")
    ice_enchant = enchantment_factory("Frozen")
    print(fire_enchant("Sword"))
    print(ice_enchant("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("Fireball", lambda target: f"Fireball hits {target}")
    fireball_spell = vault["recall"]("Fireball")
    print(fireball_spell("Dragon"))
    print(vault["recall"]("Heal")())
