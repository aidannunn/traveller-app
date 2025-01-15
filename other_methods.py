import random
from die_mod_methods import *
from trade_tables import *


def roll_die():
    return random.randit(1, 6)


def generate_available_passengers(
    die_mod_obj,
    table_obj,
    highest_skill,
    source_planet,
    destination_planet,
    passenger_quality,
    parsecs_travelled,
):
    die_roll = roll_die() + roll_die() + highest_skill
    die_mod = die_mod_obj.seeking_passenger_mods(
        source_planet,
        destination_planet,
        passenger_quality,
        die_roll,
        parsecs_travelled,
    )
    num_passengers = table_obj.passenger_traffic_table(roll_die() + roll_die(), die_mod)
    return num_passengers


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
    num_cargo = table_obj.cargo_traffic_table(roll_die() + roll_die(), die_mod)
    return num_cargo, die_mod


def generate_available_mail(
    die_mod_obj,
    table_obj,
    source_planet,
    destination_planet,
    freight_die_mod,
    armed,
    naval_or_scout_rank,
    social_die_mod,
):
    mail_exists = True
    mail_does_not_exist = False
    die_roll = roll_die() + roll_die()
    die_mod = die_mod_obj.mail_mods(
        freight_die_mod, armed, source_planet, naval_or_scout_rank, social_die_mod
    )
    if die_roll + die_mod >= 12:
        return mail_exists
    else:
        return mail_does_not_exist
