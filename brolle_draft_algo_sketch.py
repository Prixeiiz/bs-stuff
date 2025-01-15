maps = [
    {
        "name": "snake prairie",
        "mode": "bounty",
        "best_categories": ["tank", "assassin"],
        "range_rating": None
    },
    {
        "name": "safe zone",
        "mode": "heist",
        "best_categories": ["tank_counter/DPS", "sniper", "tank"],
        "range_rating": (693-86)/693    #andel tiles som är öppen map eller buskar
    },
    {
        "name": "shooting star",
        "mode": "bounty",
        "best_categories": ["sniper", "assassin", "thrower"],
        "range_rating": (693-72)/693    #andel tiles som är öppen map eller buskar
    }
]


class Brawler:
    def __init__(self, brawl_name, categories, range, hp):
        self.brawl_name = brawl_name
        self.categories = categories
        self.range = range
        self.hp = hp



'''
brawlers = [
    {
        "name": "shelly",
        "categories": ["tank_counter/DPS", "tank"],
        "range": "short"
    },
    {
        "name": "nita",
        "categories": ["tank_counter/DPS"],
        "range": "mid"
    },
    {
        "name": "colt",
        "categories": ["sniper", "tank_counter/DPS"],
        "range": "long"
    },
    {
        "name": "bull",
        "categories": ["tank"],
        "range": "short"
    }
]'''

#en typ av datastruktur, jobbigt med lista pga ordnade element?
brawlers = [
            Brawler("tick", ["thrower"], "long", 2200),
            Brawler("frank", ["tank"], "short", 6700),
            Brawler("barley",["thrower"], "mid", 2400),
            Brawler("brock", ["sniper", "tank counter/DPS"], "long", 2400),
            Brawler("byron", ["sniper", "support"], "long", 2400),
            Brawler("crow", ["assassin"], "mid", 2400),
            Brawler("nani", ["sniper", "tank counter/DPS"], "long", 2400),
            Brawler("piper", ["sniper", "tank counter/DPS"], "long", 2300),
            Brawler("primo", ["tank"], "short", 6000),
            Brawler("draco", ["tank"], "short", 5500)
            ]


#bättre med dict?
brawlers_test = {
    "tick": Brawler("TICK", ["thrower"], "long", 2200),
    "frank": Brawler("FRANK", ["tank"], "short", 6700),
    "byron": Brawler("BYRON",["sniper", "support"], "long", 2400)
}

print(brawlers_test["tick"].hp)
print(brawlers[9].brawl_name)

def hp_rating(brawler_list):        #räknar alla hp som lvl 1 brawlers
    if len(brawler_list) == 1:
        min_sum = brawlers[0].hp                        #tick (lägst)
        max_sum = brawlers[1].hp                        #franks hp (högst)
        #skala in värdena:
    elif len(brawler_list) == 2:
        minsum = brawlers[0].hp + brawlers[7].hp        #ticks + pipers hp
        maxsum = brawlers[1].hp + brawlers[8].hp        #franks + primos hp
    elif len(brawler_list) == 3:
        sum_min = brawlers[0].hp + brawlers[7].hp + brawlers[6].hp  #ticks + pipers + nanis hp
        sum_max = brawlers[1].hp + brawlers[8].hp + brawlers[9].hp      #franks + primos + dracos hp (högst o fallande)
