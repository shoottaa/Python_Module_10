def spell_combiner(spell1: callable, spell2: callable) -> callable:
    # *args = arguments positionnels
    # **kwargs = arguments nommés
    def combined(*args, **kwargs):
        return (
            spell1(*args, **kwargs),
            spell2(*args, **kwargs)
        )
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args, **kwargs):
        results = []
        for spell in spells:
            results.append(spell(*args, **kwargs))
        return results
    return sequence


if __name__ == "__main__":
    def fireball(target):
        return f"Fireball hits {target}"

    def heal(target):
        return f"Heals {target}"

    def damage(target):
        return 10

    def is_enemy(target):
        return target == "Dragon"

    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    mega_damage = power_amplifier(damage, 3)
    original = damage("Dragon")
    amplified = mega_damage("Dragon")
    print(f"Original: {original}, Amplified: {amplified}")

    print("\nTesting conditional caster...")
    conditional_fireball = conditional_caster(is_enemy, fireball)
    print(f"On Dragon: {conditional_fireball('Dragon')}")
    print(f"On Ally: {conditional_fireball('Ally')}")

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, fireball])
    results = sequence("Dragon")
    print(f"Sequence results: {results}")
