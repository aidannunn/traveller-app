import random
from die_mod_methods import *
from trade_tables import *


def roll_die():
    return random.randit(1, 6)

def generate_

def generate_available_freight(
    die_mod_obj,
    table_obj,
    highest_skill,
    source_planet,
    destination_planet,
    cargo_quality,
    parsecs_travelled,
):
    die_roll = roll_die() + roll_die() + highest_skill
    die_mod = die_mod_obj.seeking_cargo_mods(
        source_planet,
        destination_planet,
        cargo_quality,
        die_roll,
        parsecs_travelled,
    )
    num_passengers = table_obj.passenger_traffic_table(roll_die() + roll_die(), die_mod)
    return num_passengers


def generate_available_passengers(
    die_mod_obj,
    table_obj,
    highest_skill,
    source_planet,
    destination_planet,
    steward_skill,
    passenger_quality,
    parsecs_travelled,
):
    die_roll = roll_die() + roll_die() + highest_skill
    die_mod = die_mod_obj.seeking_passengers_mods(
        die_roll,
        steward_skill,
        passenger_quality,
        source_planet,
        destination_planet,
        parsecs_travelled,
    )
    num_passengers = table_obj.passenger_traffic_table(roll_die() + roll_die(), die_mod)
    return num_passengers
