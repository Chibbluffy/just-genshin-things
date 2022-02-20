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
- character additional bonuses (from weapon, artifact, constellation, etc.)
    - elemental bonus damages
    - NA bonus damages
    - CA bonus damages
    - plunge bonus damages
    - skill bonus damages
    - burst bonus damages
    - all damage bonuses

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
- enemy level gap damage difference
- enemy resistances
- damage from lowering enemy defense and resistances
- shield strength

## How to update data
- run `python getHoneyCharacterData.py`
- update talent_categories.js file with new data
    - If you don't, you may get incorrect calculations if it automatically categorizes the damage to the wrong talent
- if a character has some sort of infusion or buff, make sure to add a new function to the calculate method since it isn't a normal calculation.

Chongyun