import json

class ShipStats:
    def __init__(self):
        with open('ship_stats.json') as file:
            self.stats = json.load(file)
        self.current_location = self.stats.get("location")
        self.highest_skill = self.stats.get("highest_skill")
        self.steward_skill = self.stats.get("steward_skill")
        self.armed = self.stats.get("armed")
        self.naval_or_scout_rank = self.stats.get("naval_or_scout_rank")
        self.social_die_mod = self.stats.get("social_die_mod")

    def set_stats(self, location, highest_skill, steward, armed, naval_or_scout, social):
        self.current_location = location
        self.highest_skill = highest_skill
        self.steward_skill = steward
        self.armed = armed
        self.naval_or_scout_rank = naval_or_scout
        self.social_die_mod = social

    def save_stats(self):
        self.stats["location"] = self.current_location
        self.stats["highest_skill"] = self.highest_skill
        self.stats["steward_skill"] = self.steward_skill
        self.stats["armed"] = self.armed
        self.stats["naval_or_scout_rank"] = self.naval_or_scout_rank
        self.stats["social_die_mod"] = self.social_die_mod
        with open('ship_stats.json', 'w') as file:
            json.dump(self.stats, file, indent=4)
