import requests
import re

base_url = 'https://genshin.honeyhunterworld.com/db/char/'
page = requests.get(base_url + 'characters/?lang=EN').content.decode("utf-8") 
pattern = r'<div class=char_sea_cont><a href="/db/char/(.*?)\/\?lang=EN"><img'
characters = re.findall(pattern, page)

with open('character_stats.js', 'w', encoding="utf-8") as file:
    file.write('let data = [\n')
    for character in characters:
        if character == "feiyan":
            file.write('"CHARACTER_NAME: yanfei",\n')
        elif character == "shougun":
            file.write('"CHARACTER_NAME: raiden",\n')
        elif "traveler_boy" in character:
            file.write(f'"CHARACTER_NAME: traveler_{character[13:]}",\n')
        elif "traveler_girl" in character:
            continue
            file.write(f'"CHARACTER_NAME: lumine_{character[14:]}",\n')
        else:
            file.write('"CHARACTER_NAME: ' + character + '",\n')

        page = requests.get(base_url + character).content
        element = re.search(br'\/img\/icons\/element\/(.*?)_', page).group(1)
        file.write(f'"CHARACTER_ELEMENT: {element.decode()}",\n')

        element = re.search(br'Weapon Type<\/td><td><a href="\/db\/weapon\/(.*?)\/', page).group(1)
        file.write(f'"CHARACTER_WEAPON: {element.decode()}",\n')

        pattern = br'<table class=add_stat_table .*?<\/table>'
        tables = [t for t in re.findall(pattern, page)]

        talent = 1
        if character in ["mona", "ayaka"]:
            for table in tables[:2]:
                pattern = br'<tr>.*?</tr>'
                stats = [s for s in re.findall(pattern, table)]

                for stat in stats:
                    if b'Lv15' in stat:
                        file.write(f'"TALENT_LEVEL: {talent}",\n')
                        talent += 1
                    else:
                        file.write(f'"{stat.decode()}",\n')
            # talent 4 because these characters have dash on talent 3
            pattern = br'<tr>.*?</tr>'
            stats = [s for s in re.findall(pattern, tables[3])]

            for stat in stats:
                if b'Lv15' in stat:
                    file.write(f'"TALENT_LEVEL: {talent}",\n')
                    talent += 1
                else:
                    file.write(f'"{stat.decode()}",\n')
        else: 
            for table in tables[:3]:
                pattern = br'<tr>.*?</tr>'
                stats = [s for s in re.findall(pattern, table)]

                for stat in stats:
                    if b'Lv15' in stat:
                        file.write(f'"TALENT_LEVEL: {talent}",\n')
                        talent += 1
                    else:
                        file.write(f'"{stat.decode()}",\n')
        file.write('"",\n')
    file.write('];')