class DieMods:
    @staticmethod
    def passenger_quality_mod(passenger_quality):
        if passenger_quality == 1:
            return -4
        elif passenger_quality == 4:
            return 1
        else:
            return 0

    @staticmethod
    def cargo_quality_mod(cargo_quality):
        if cargo_quality == 1:
            return -4
        elif cargo_quality == 3:
            return 2
        else:
            return 0

    @staticmethod
    def planet_population_passenger_mod(planet_population):
        if planet_population <= 1:
            return -4
        elif planet_population == 6 or planet_population == 7:
            return 1
        elif planet_population >= 8:
            return 3
        else:
            return 0

    @staticmethod
    def planet_population_cargo_mod(planet_population):
        if planet_population <= 1:
            return -4
        elif planet_population == 6 or planet_population == 7:
            return 2
        elif planet_population >= 8:
            return 4
        else:
            return 0

    @staticmethod
    def starport_quality_mod(starport_quality):
        if starport_quality == "A":
            return 2
        elif starport_quality == "B":
            return 1
        elif starport_quality == "E":
            return -1
        elif starport_quality == "X":
            return -3
        else:
            return 0

    @staticmethod
    def planet_zone_passenger_mod(planet_zone):
        if planet_zone == "A":
            return 1
        elif planet_zone == "R":
            return -4
        else:
            return 0

    @staticmethod
    def planet_zone_cargo_mod(planet_zone):
        if planet_zone == "A":
            return -2
        elif planet_zone == "R":
            return -6
        else:
            return 0

    def seeking_passengers_mods(
        self,
        die_roll,
        steward_skill,
        passenger_quality,
        source_planet,
        destination_planet,
        parsecs_traveled,
    ):
        die_mod = 0
        die_mod += die_roll - 8
        die_mod += steward_skill
        die_mod += self.passenger_quality_mod(passenger_quality)
        die_mod += self.planet_population_passenger_mod(
            int(source_planet.UWPObject.Population, 16)
        )
        die_mod += self.planet_population_passenger_mod(
            int(destination_planet.UWPObject.Population, 16)
        )
        die_mod += self.starport_quality_mod(source_planet.UWPObject.Starport)
        die_mod += self.starport_quality_mod(destination_planet.UWPObject.Starport)
        die_mod += self.planet_zone_passenger_mod(source_planet.TravelZone)
        die_mod += self.planet_zone_passenger_mod(destination_planet.TravelZone)
        die_mod += 1 - parsecs_traveled

        return die_mod

    def seeking_cargo_mods(
        self,
        source_planet,
        destination_planet,
        cargo_quality,
        die_roll,
        parsecs_traveled,
    ):
        die_mod = 0
        die_mod += die_roll - 8
        die_mod += self.cargo_quality_mod(cargo_quality)
        die_mod += self.planet_population_cargo_mod(
            int(source_planet.UWPObject.Population, 16)
        )
        die_mod += self.planet_population_cargo_mod(
            int(destination_planet.UWPObject.Population, 16)
        )
        die_mod += self.starport_quality_mod(source_planet.UWPObject.Starport)
        die_mod += self.starport_quality_mod(destination_planet.UWPObject.Starport)
        die_mod += self.planet_zone_cargo_mod(source_planet.TravelZone)
        die_mod += self.planet_zone_cargo_mod(destination_planet.TravelZone)
        die_mod += 1 - parsecs_traveled

        return die_mod

    def mail_freight_mod(
        self,
        source_planet,
        destination_planet,
    ):
        die_mod = 0
        die_mod += self.planet_population_cargo_mod(
            int(source_planet.UWPObject.Population, 16)
        )
        die_mod += self.planet_population_cargo_mod(
            int(destination_planet.UWPObject.Population, 16)
        )
        die_mod += self.starport_quality_mod(source_planet.UWPObject.Starport)
        die_mod += self.starport_quality_mod(destination_planet.UWPObject.Starport)
        die_mod += self.planet_zone_cargo_mod(source_planet.TravelZone)
        die_mod += self.planet_zone_cargo_mod(destination_planet.TravelZone)

        return die_mod

    def mail_mods(
        self,
        source_planet,
        destination_planet,
        armed,
        naval_or_scout_rank,
        social_die_mod,
    ):
        freight_traffic_die_mod = self.mail_freight_mod(
            source_planet, destination_planet
        )
        die_mod = 0
        if freight_traffic_die_mod <= -10:
            die_mod += -2
        elif -9 <= freight_traffic_die_mod <= -5:
            die_mod += -1
        elif -4 <= freight_traffic_die_mod <= 4:
            die_mod += 0
        elif 5 <= freight_traffic_die_mod <= 9:
            die_mod += 1
        else:
            die_mod += 2
        if armed:
            die_mod += 2
        if int(source_planet.UWPObject.TechLevel, 16) <= 5:
            die_mod += -4
        die_mod += naval_or_scout_rank
        die_mod += social_die_mod
        return die_mod
