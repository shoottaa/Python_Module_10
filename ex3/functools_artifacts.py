import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": functools.partial(base_enchantment, element="fire",
                                          power=50),
        "ice_enchant": functools.partial(base_enchantment, element="ice",
                                         power=50),
        "lightning_enchant": functools.partial(base_enchantment,
                                               element="lightning", power=50)
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @functools.singledispatch
    def cast_spell(spell):
        return f"Unknown spell type: {type(spell)}"

    @cast_spell.register(int)
    def _(spell):
        return f"Damage spell: {spell} points of damage dealt!"

    @cast_spell.register(str)
    def _(spell):
        return f"Enchantment cast: '{spell}' enchantment applied!"

    @cast_spell.register(list)
    def _(spell):
        return f"Multi-cast: {len(spell)} spells fired — {spell}"

    return cast_spell


if __name__ == "__main__":
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    print(f"Min: {spell_reducer(spells, 'min')}")

    print("\nTesting partial enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{element}({power}) -> {target}"

    enchants = partial_enchanter(base_enchantment)
    print(enchants["fire_enchant"](target="sword"))
    print(enchants["ice_enchant"](target="shield"))
    print(enchants["lightning_enchant"](target="staff"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    cast = spell_dispatcher()
    print(cast(42))
    print(cast("fireball"))
    print(cast([1, 2, 3]))
