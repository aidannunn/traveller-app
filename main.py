from other_methods import *
from trade_tables import *
from die_mod_methods import *


if __name__ == "__main__":
    print("Welcome to the Galactic Trade Simplifier")
    departure_planet = input("Enter your departure planet:")
    destination_planet = input("Enter your destination planet:")
    parsecs_travelled = input("Enter the number of parsecs you are travelling:")
    highest_skill = input(
        "Enter the highest from among broker, carouse, or streetwise:"
    )

    # convert departure planet to planet class

    # convert destination planet to planet class

    trade_tables_obj = TradeTables()
    die_mods_obj = DieMods()
    passenger_quality_arr = [1, 2, 3, 4]
    for quality in passenger_quality_arr:
        generate_available_passengers(
            die_mods_obj,
            trade_tables_obj,
            highest_skill,
            source_planet,
            destination_planet,
            quality,
            parsecs_travelled,
        )

    # generate array of potential passengers
    # calculate earnings from passengers
    # generate array of potential freight
    # calculate earnings from freight
    # generate potential mail
    # calculate earnings from mail
