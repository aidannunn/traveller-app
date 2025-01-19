from other_methods import *
from trade_tables import *
from die_mod_methods import *
import PySimpleGUI as Sg
from counts_class import StuffCount


class TradeGUI:
    def __init__(self, icon_path, planet_api_obj):
        self.icon_path = icon_path
        self.planet_api_obj = planet_api_obj
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
                values = []
                self.window.close()
                layout = self.create_layout_1()
                self.window = Sg.Window(
                    "Trade Federation Network", layout, icon=self.icon_path
                )

            if event == "Ok":
                if not self.validate_inputs(values):
                    # event = ""
                    self.window.close()
                    self.window = Sg.Window(
                        "Trade Federation Network",
                        self.create_layout_3(),
                        icon=self.icon_path,
                    )
                    continue

                departure_planet_name = values[0].strip().lower()
                destination_planet_name = values[1].strip().lower()
                highest_skill = int(values[2])
                parsecs_travelled = int(values[3])
                steward_skill = -3

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
                    armed=0,
                    naval_or_scout_rank=4,
                    social_die_mod=1,
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

        self.window.close()

    @staticmethod
    def create_layout_1():
        layout1 = [
            [Sg.Text("Welcome to the Trade Federation Network")],
            [Sg.Text("Departure:"), Sg.InputText()],
            [Sg.Text("Destination:"), Sg.InputText()],
            [Sg.Text("Distance:"), Sg.InputText()],
            [
                Sg.Text("Highest skill among broker, carouse, or streetwise:"),
                Sg.InputText(),
            ],
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
            [Sg.Text(f"Thank you for using the Galactic Trade Network!")],
            [Sg.Button("Back"), Sg.Button("Exit")],
        ]
        if counts_obj.mail_exists:
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
                [Sg.Text(f"Minor Freight: {counts_obj.minor_freight}")],
                [Sg.Text(f"Incidental Freight: {counts_obj.incidental_freight}")],
                [Sg.Text(f"Mail Containers: {counts_obj.mail_containers}")],
                [Sg.Text(f"Thank you for using the Galactic Trade Network!")],
                [Sg.Button("Back"), Sg.Button("Exit")],
            ]

        return layout2

    @staticmethod
    def create_layout_3():
        layout3 = [
            [Sg.Text("Welcome to the Trade Federation Network")],
            [Sg.Text("\nInvalid input detected. Please try again.\n")],
            [Sg.Text("Departure:"), Sg.InputText()],
            [Sg.Text("Destination:"), Sg.InputText()],
            [Sg.Text("Distance:"), Sg.InputText()],
            [
                Sg.Text("Highest skill among broker, carouse, or streetwise:"),
                Sg.InputText(),
            ],
            [Sg.Button("Ok"), Sg.Button("Cancel")],
        ]
        return layout3

    def validate_inputs(self, values):
        if (
            values[0].strip().lower() not in self.planet_api_obj.planets_dict.keys()
            or values[1].strip().lower() not in self.planet_api_obj.planets_dict.keys()
            or int(values[2]) < 1
            or int(values[2]) > 6
            or int(values[3]) < 0
        ):
            return False

        return True
