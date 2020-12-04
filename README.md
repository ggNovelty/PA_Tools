## PA\_Tools

Some (badly written) tools to check PokeAlarm's base\_stats.json against the Game Master.
May be useful from time to time as new Pokemon are added or as base stats are modified.
Currently only checks Attack, Defense, and Stamina values.

Everything here uses Python3.

You will need a fresh copy of the Game Master in json format.
Recommended: [PokeMiners](https://github.com/PokeMiners/game_masters/tree/master/latest)

#To use:

* First, try to get `base_stats.json` and `game_master.json` within the same folder as these scripts. If not possible, make sure to edit them to point to the correct location.

* Second, run `check_stats.py`. This will generate a new json file, `stats_differ.json`. Double check some of the values in this file to make sure everything ran properly.

* Finally, run `write_stats.py`. It will modify `base_stats.json`, overwriting the old values with new ones from the Game Master.
