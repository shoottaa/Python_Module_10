def mage_counter() -> callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    total = initial_power

    def accumulate(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(item: str) -> str:
        return f"{enchantment_type} {item}"

    return enchant


def memory_vault() -> dict[str, callable]:
    vault = {}

    def store(key: str, value) -> None:
        vault[key] = value

    def recall(key: str):
        return vault.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("\nTesting spell accumulator...")
    accumulate = spell_accumulator(100)
    print(accumulate(50))
    print(accumulate(25))

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("spell", "fireball")
    vault["store"]("power", 42)
    print(vault["recall"]("spell"))
    print(vault["recall"]("power"))
    print(vault["recall"]("test"))
