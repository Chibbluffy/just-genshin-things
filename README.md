# Simple Comprehensive Genshin Damage Calculator
Link: https://chibbluffy.github.io/just-genshin-things/fullDamageCalculator.html

## Sources
- Genshin character stats and skill multipliers are from [HoneyImpact](https://genshin.honeyhunterworld.com/?lang=EN)
- Genshin damage calculations are from the [wiki](https://genshin-impact.fandom.com/wiki/Genshin_Impact_Wiki)

## Inputs
- character name
- character talent levels
    - if talent does elemental damage
        - Ex. if character is a catalyst, talent 1 should be dealing elemental damage, not physical damage
        - Ex. Eula's talent 3 deals physical damage, not elemental damage
- character total stats (from more details screen)
    - hp
    - atk
    - def
    - crit rate
    - crit dmg
    - elemental mastery
    - elemental damage
    - energy recharge
- character additional bonuses (from weapon, artifact, constellation, etc.)
    - weapon
    - artifact
    - elemental bonus damages
    - NA bonus damages
    - CA bonus damages
    - plunge bonus damages
    - skill bonus damages
    - burst bonus damages
    - all damage bonuses
- enemy stats
    - enemy name (to autofill resistances)
    - level
    - elemental resistance
    - physical resistance

## Outputs
- minimun, maximum, and average damages for the below with no buffs
    - Normal attacks
    - Charge attacks
    - Skill DMG
    - Burst DMG
- minimun, maximum, and average damages for the below with relevant elemental reactions
    - Normal attacks
    - Charge attacks
    - Skill DMG
    - Burst DMG

## Planned Future Features
- enemy resistances/level
- special artifacts (emblem)

## How to update data for local host
- run `python getHoneyCharacterData.py`
- if a character has some sort of infusion or buff, make sure to add a new function to the calculate method since it isn't a normal calculation.
