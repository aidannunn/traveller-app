from idlelib.mainmenu import menudefs
from pathlib import Path

from gui import *
from other_methods import *
from trade_tables import *
from die_mod_methods import *
from UWPCalc.PlanetAPI import PlanetAPI
import PySimpleGUI as sg

if __name__ == "__main__":
    planet_api_obj = PlanetAPI()
    home_dir = Path(__file__).parent
    icon_path = home_dir.joinpath("ship-logo.ico")
    departure_planet = ""
    destination_planet = ""

    # All the stuff inside your window.
    sg.theme("Neon Green 1")

    layout = create_layout_1()

    # Create the Window
    window = sg.Window("Trade Federation Network", layout, icon=icon_path)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        if (
            event == sg.WIN_CLOSED or event == "Cancel" or event == "Exit"
        ):  # if user closes window or clicks cancel
            break

        if event == "Back":
            departure_planet = ""
            destination_planet = ""
            highest_skill = 0
            parsecs_travelled = 0
            values = []
            window.close()
            layout = create_layout_1()
            window = sg.Window("Trade Federation Network", layout, icon=icon_path)

        if event == "Ok":

            departure_planet = values[0]
            destination_planet = values[1]
            highest_skill = int(values[2])
            parsecs_travelled = int(values[3])
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
            window.close()
            layout = create_layout_2()
            window = sg.Window("Trade Federation Network", layout, icon=icon_path)

            print_available_traffic(
                passenger_counts_dict, freight_counts_dict, cargo_size_arr, mail_exists
            )

    window.close()
