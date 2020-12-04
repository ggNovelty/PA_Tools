# Write_stats.py - takes a file 'stats_differ.json' as input, 
# replacing stats in base_stats.json with values from stats_differ.json

import json


with open("stats_differ.json", "r") as to_write:
    new_stats = json.load(to_write)

with open("base_stats.json", "r") as old_base:
    edit_data = json.load(old_base)

to_write.close()
old_base.close()

# Updates base_stats.json with new values
for pokemon in new_stats:
    edit_data[pokemon]["attack"] = new_stats[pokemon]["atk"]
    edit_data[pokemon]["defense"] = new_stats[pokemon]["def"]
    edit_data[pokemon]["stamina"] = new_stats[pokemon]["sta"]

# Overwrites base_stats.json with our new values
with open("base_stats.json", "w") as new_base:
    json.dump(edit_data, new_base, indent=2)

new_base.close()
