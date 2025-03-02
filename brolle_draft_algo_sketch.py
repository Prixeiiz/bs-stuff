class Map:
    def __init__(self, map_name, mode, range_rating):
        self.map_name = map_name
        self.mode = mode
        self.range_rating = range_rating

class Brawler:
    def __init__(self, brawl_name, categories, range, hp, play_pos, water_playable):
        self.brawl_name = brawl_name
        self.categories = categories
        self.range = range
        self.hp = hp
        self.play_pos = play_pos
        self.water_playable = water_playable

brawlers = {
    "tick": Brawler("TICK", ["thrower"], "long", 2200, ["mid","lane"], False),
    "frank": Brawler("FRANK", ["tank"], "short", 6700, ["lane"], False),
    "byron": Brawler("BYRON",["sniper", "support"], "long", 2400, ["mid", "lane"], False),
    "angelo": Brawler("ANGELO", ["sniper"], "long", 3000, ["mid", "lane"], True),
    "piper": Brawler("PIPER", ["sniper", "DPS"], "long", 2300, ["mid", "lane"], False),
    "primo": Brawler("EL PRIMO", ["tank"], "short", 6000, ["lane"], False),
    "nani": Brawler("NANI", ["sniper", "DPS"], "long", 2400, ["mid", "lane"], False),
    "draco": Brawler("DRACO", ["tank"], "short", 5500, ["lane"], False)
}

maps = {
    "snake prairie": Map("Snake Prairie", "bounty", None),
    "tripple dribble": Map("Tripple Dribble", "brawl ball", None),
}


def lowest_hp(brawler_list):
    hp_list = [brawlers[brawler].hp for brawler in brawler_list]
    return min(hp_list)

def highest_hp(brawler_list):
    hp_list = [brawlers[brawler].hp for brawler in brawler_list]
    return max(hp_list)

print(highest_hp(["tick", "piper", "frank"]))


def hp_rating(brawler_list):        #räknar alla hp som lvl 1 brawlers
    if len(brawler_list) == 1:
        min_sum = brawlers["tick"].hp                        #tick (minst)
        max_sum = brawlers["frank"].hp                        #franks hp (störst)
        #skala in värdena:
    elif len(brawler_list) == 2:
        minsum = brawlers["tick"].hp + brawlers["piper"].hp         #minst hp
        maxsum = brawlers["frank"].hp + brawlers["primo"].hp        #störst hp
    elif len(brawler_list) == 3:
        sum_min = brawlers["tick"].hp + brawlers["piper"].hp + brawlers["nani"].hp              #minst hp
        sum_max = brawlers["frank"].hp + brawlers["primo"].hp + brawlers["draco"].hp            #störst hp
