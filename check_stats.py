# check_stats.py - Checks base_stats.json vs game_master.json. 
# Writes mons with differing values to a 3rd file, stats_differ.json .

import json
import os


# Edit path to json if not within same dir
with open("base_stats.json") as base_stats:
    base = json.load(base_stats)

# Edit path to json if not within same dir
with open("game_master.json") as game_master:
    gm = json.load(game_master)

write_these = open("stats_differ.json", "a")

# Begin json
write_these.write("{\n")

for poke in base:
    
    #Get currently used data
    dex_num = poke
    base_atk = base[poke]['attack']
    base_def = base[poke]['defense']
    base_sta = base[poke]['stamina']

    for data in gm:
        #Just trying to get normal pokemon stats, not shadows, purified, etc.
        if (data["templateId"][:5] == ("V0" + dex_num)) and (data["templateId"][-6:] == "NORMAL"):
            stamina, attack, defense = data['data']['pokemonSettings']['stats'].values()
            break

        elif data["templateId"][:14] == ("V0" + dex_num + "_POKEMON_"):
            try:
                stamina, attack, defense = data['data']['pokemonSettings']['stats'].values()
            except:
                #Some pkmn have empty stats dict in GM
                stamina = attack = defense = "empty"
            break

        else:
            stamina = attack = defense = "error"

    if stamina == "error":
        #write_these.write(poke + " error, could not find mon in gm\n")
        pass

    elif stamina == "empty":
        #write_these.write(poke + " error, empty stats in gm\n")
        pass

    #These pokemon have at least one stat which differs between GM and base_stats
    elif base_atk != attack or base_def != defense or base_sta != stamina:
        write_these.write('  "' + poke + '": {\n    "atk": ' + str(attack) + ', "def": ' + str(defense) + ', "sta": ' + str(stamina) + "\n  },\n")

# End json
write_these.close()

# Remove last comma
with open("stats_differ.json", "rb+") as temp:
    temp.seek(-2, os.SEEK_END)
    temp.truncate()

temp.close()

with open("stats_differ.json", "a") as temp:
    temp.write("\n}")

temp.close()
