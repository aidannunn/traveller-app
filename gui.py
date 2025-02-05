import re

from other_methods import *
from trade_tables import *
from die_mod_methods import *
import PySimpleGUI as Sg
from counts_class import StuffCount


class TradeGUI:
    def __init__(self, icon_path, planet_api_obj, ship_stats_obj):
        self.icon_path = icon_path
        self.planet_api_obj = planet_api_obj
        self.ship_stats_obj = ship_stats_obj
        self.theme = Sg.theme("Neon Green 1")
        self.initial_layout = self.create_layout_1()
        self.window = Sg.Window(
            "Trade Federation Network", self.initial_layout, icon=self.icon_path
        )

    def run_gui(self):

        while True:
            event, values = self.window.read()

            if event == Sg.WIN_CLOSED or event == "Cancel" or event == "Exit":
                break

            if event == "Back":
                self.window.close()
                layout = self.create_layout_1()
                self.window = Sg.Window(
                    "Trade Federation Network", layout, icon=self.icon_path
                )

            if event == "Ok":
                invalid_field = self.validate_inputs(values)
                if len(invalid_field) > 0:
                    self.window.close()
                    layout = self.create_layout_3(invalid_field)
                    self.window = Sg.Window(
                        "Trade Federation Network",
                        layout,
                        icon=self.icon_path,
                    )
                    continue

                departure_planet_name = values[0].strip().lower()
                destination_planet_name = values[1].strip().lower()
                highest_skill = int(values[2])
                parsecs_travelled = int(values[3])
                steward_skill = int(values[4])
                if values[5]:
                    armed = True
                else:
                    armed = False
                naval_or_scout_rank = int(values[6])
                social_die_mod = int(values[7])

                self.ship_stats_obj.set_stats(destination_planet_name, highest_skill, steward_skill, armed, naval_or_scout_rank, social_die_mod)

                source_planet = self.planet_api_obj.planets_dict[departure_planet_name]
                destination_planet = self.planet_api_obj.planets_dict[
                    destination_planet_name
                ]

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
                    armed,
                    naval_or_scout_rank,
                    social_die_mod,
                )

                counts_obj = StuffCount(
                    passenger_counts_dict,
                    freight_counts_dict,
                    mail_exists,
                    cargo_size_arr,
                )

                self.window.close()
                layout = self.create_layout_2(
                    counts_obj, departure_planet_name, destination_planet_name
                )
                self.window = Sg.Window(
                    "Trade Federation Network", layout, icon=self.icon_path
                )

        self.ship_stats_obj.save_stats()
        self.window.close()

    def create_layout_1(self):
        layout1 = [
            [Sg.Text("Welcome to the Trade Federation Network")],
            [Sg.Text("Departure:"), Sg.InputText(default_text=self.ship_stats_obj.current_location)],
            [Sg.Text("Destination:"), Sg.InputText()],
            [Sg.Text("Distance:"), Sg.InputText()],
            [
                Sg.Text("Highest skill among broker, carouse, or streetwise:"),
                Sg.InputText(default_text=self.ship_stats_obj.highest_skill),
            ],
            [Sg.Text("Steward skill:"), Sg.InputText(default_text=self.ship_stats_obj.steward_skill)],
            [Sg.Checkbox("Ship armed?", default=self.ship_stats_obj.armed)],
            [Sg.Text("Naval or scout rank:"), Sg.InputText(default_text=self.ship_stats_obj.naval_or_scout_rank)],
            [Sg.Text("Social mod:"), Sg.InputText(default_text=self.ship_stats_obj.social_die_mod)],
            [Sg.Button("Ok"), Sg.Button("Cancel")],
        ]
        return layout1

    @staticmethod
    def create_layout_2(counts_obj, departure_planet, destination_planet):
        layout2 = [
            [
                Sg.Text(
                    f"Here is the available traffic from {departure_planet} to {destination_planet}"
                )
            ],
            [Sg.Text(f"High Passengers: {counts_obj.high_passengers}")],
            [Sg.Text(f"Middle Passengers: {counts_obj.middle_passengers}")],
            [Sg.Text(f"Basic Passengers: {counts_obj.basic_passengers}")],
            [Sg.Text(f"Low Passengers: {counts_obj.low_passengers}")],
            [Sg.Text(f"Major Freight: {counts_obj.major_freight}")],
            [Sg.Text(f"Major Freight Size: {counts_obj.major_freight_size}")],
            [Sg.Text(f"Minor Freight: {counts_obj.minor_freight}")],
            [Sg.Text(f"Minor Freight Size: {counts_obj.minor_freight_size}")],
            [Sg.Text(f"Incidental Freight: {counts_obj.incidental_freight}")],
            [Sg.Text(f"Incidental Freight Size: {counts_obj.incidental_freight_size}")],
            [Sg.Text(f"Mail Containers: {counts_obj.mail_containers}")],
            [Sg.Text(f"Thank you for using the Galactic Trade Network!")],
            [Sg.Button("Back"), Sg.Button("Exit")],
        ]
        return layout2

    def create_layout_3(self, invalid_field_list):

        welcome_message = [Sg.Text("Welcome to the Trade Federation Network")]
        departure_message = [Sg.Text("Departure:"), Sg.InputText(default_text=self.ship_stats_obj.current_location)]
        destination_message = [Sg.Text("Destination:"), Sg.InputText()]
        distance_message = [Sg.Text("Distance:"), Sg.InputText()]
        skill_message = [
            Sg.Text("Highest skill among broker, carouse, or streetwise:"),
            Sg.InputText(),
        ]
        steward_message = [Sg.Text("Steward skill:"), Sg.InputText(default_text=self.ship_stats_obj.steward_skill)]
        armed_message = [Sg.Checkbox("Ship armed?", default=self.ship_stats_obj.armed)]
        naval_or_scout_message = [Sg.Text("Naval or scout rank:"), Sg.InputText(default_text=self.ship_stats_obj.naval_or_scout_rank)]
        social_mod_message = [Sg.Text("Social mod:"), Sg.InputText(default_text=self.ship_stats_obj.social_die_mod)]
        button_message = [Sg.Button("Ok"), Sg.Button("Cancel")]

        layout3 = [
            welcome_message,
            departure_message,
            destination_message,
            distance_message,
            skill_message,
            steward_message,
            armed_message,
            naval_or_scout_message,
            social_mod_message,
            button_message,
        ]

        invalid_departure_message = [
            Sg.Text("\nInvalid departure input detected. Please try again.\n")
        ]
        invalid_destination_message = [
            Sg.Text("\nInvalid destination input detected. Please try again.\n")
        ]
        invalid_distance_message = [
            Sg.Text("\nInvalid distance input detected. Please try again.\n")
        ]
        invalid_skill_message = [
            Sg.Text("\nInvalid skill input detected. Please try again.\n")
        ]
        invalid_steward_message = [
            Sg.Text("\nInvalid steward skill input detected. Please try again.\n")
        ]

        if "departure_invalid" in invalid_field_list:
            layout3.insert(
                layout3.index(departure_message) + 1, invalid_departure_message
            )
        if "destination_invalid" in invalid_field_list:
            layout3.insert(
                layout3.index(destination_message) + 1, invalid_destination_message
            )
        if "distance_invalid" in invalid_field_list:
            layout3.insert(
                layout3.index(distance_message) + 1, invalid_distance_message
            )
        if "skill_invalid" in invalid_field_list:
            layout3.insert(layout3.index(skill_message) + 1, invalid_skill_message)

        if "steward_skill_invalid" in invalid_field_list:
            layout3.insert(layout3.index(steward_message) + 1, invalid_steward_message)

        return layout3

    def validate_inputs(self, values):
        invalid_field_list = []
        if values[0].strip().lower() not in self.planet_api_obj.planets_dict.keys():
            invalid_field_list.append("departure_invalid")

        if values[1].strip().lower() not in self.planet_api_obj.planets_dict.keys():
            invalid_field_list.append("destination_invalid")

        if values[2].strip().lower() == '':
            invalid_field_list.append("distance_invalid")
        elif int(values[2]) < 1 or int(values[2]) > 6:
            invalid_field_list.append("distance_invalid")

        if values[3].strip().lower() == '':
            invalid_field_list.append("skill_invalid")
        elif int(values[3]) < 0:
            invalid_field_list.append("skill_invalid")

        if values[4].strip().lower() == '':
            invalid_field_list.append("steward_skill_invalid")
        elif not self.invalid_int_input(values[4]):
            invalid_field_list.append("steward_skill_invalid")

        return invalid_field_list

    @staticmethod
    def invalid_int_input(input_str):
        if re.fullmatch(r"-?\d+", input_str):
            return True
        return False

