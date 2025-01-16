from other_methods import *
from trade_tables import *
from die_mod_methods import *
from UWPCalc.PlanetAPI import PlanetAPI


if __name__ == "__main__":
    planet_api_obj = PlanetAPI()

    print("Welcome to the Galactic Trade Network")

    departure_planet = "Corgi"  # input("Enter your departure planet:")
    destination_planet = "Corgi2"  # input("Enter your destination planet:")
    parsecs_travelled = 1  # input("Enter the number of parsecs you are travelling:")
    highest_skill = 1  # input(
    # "Enter the highest from among broker, carouse, or streetwise:"
    # )

    print(
        f"Here is the available traffic from {departure_planet} to {destination_planet}\n"
    )

    steward_skill = -3

    source_planet = planet_api_obj.Planets[departure_planet]
    destination_planet = planet_api_obj.Planets[destination_planet]

    trade_tables_obj = TradeTables()
    die_mods_obj = DieMods()

    passenger_quality_arr = [1, 2, 3, 4]
    passenger_counts_dict = generate_passenger_counts(
        passenger_quality_arr,
        die_mods_obj,
        trade_tables_obj,
        highest_skill,
        steward_skill,
        source_planet,
        destination_planet,
        parsecs_travelled,
    )

    freight_quality_arr = [1, 2, 3]
    freight_counts_dict = generate_freight_counts(
        freight_quality_arr,
        die_mods_obj,
        trade_tables_obj,
        highest_skill,
        source_planet,
        destination_planet,
        parsecs_travelled,
    )

    cargo_size_arr = generate_freight_sizes()

    mail_exists = check_if_mail_exists(
        die_mods_obj,
        source_planet,
        destination_planet,
        armed=0,
        naval_or_scout_rank=4,
        social_die_mod=1,
    )

    print_available_traffic(
        passenger_counts_dict, freight_counts_dict, cargo_size_arr, mail_exists
    )

    print("\nThank you for using the Galactic Trade Network!")
