class DieMods:

    def seeking_passengers_mods(
        self,
        source_planet,
        destination_planet,
        steward_skill,
        passenger_quality,
        die_roll,
    ):
        die_mod = 0
        die_mod += die_roll - 8
        die_mod += steward_skill
        if passenger_quality == 0:
            die_mod += -4
        elif passenger_quality == 3:
            die_mod += 1
        if source_planet.population <= 1:
            die_mod += -4
        elif source_planet.population == 6 or source_planet.population == 7:
            die_mod += 1
        elif source_planet.population >= 8:
            die_mod += 3
        if destination_planet.population <= 1:
            die_mod += -4
        elif destination_planet.population == 6 or destination_planet.population == 7:
            die_mod += 1
        elif destination_planet.population >= 8:
            die_mod += 3
        if source_planet.starport == "A":
            