import PySimpleGUI as sg


def create_layout_1():
    layout1 = [
        [sg.Text("Welcome to the Trade Federation Network")],
        [sg.Text("Departure:"), sg.InputText()],
        [sg.Text("Destination:"), sg.InputText()],
        [sg.Text("Distance:"), sg.InputText()],
        [
            sg.Text("Highest skill among broker, carouse, or streetwise:"),
            sg.InputText(),
        ],
        [sg.Button("Ok"), sg.Button("Cancel")],
    ]
    return layout1


def create_layout_2(counts_obj, departure_planet, destination_planet):
    layout2 = [
        [
            sg.Text(
                f"Here is the available traffic from {departure_planet} to {destination_planet}"
            )
        ],
        [sg.Text(f"High Passengers: {counts_obj.high_passengers}")],
        [sg.Text(f"Middle Passengers: {counts_obj.middle_passengers}")],
        [sg.Text(f"Basic Passengers: {counts_obj.basic_passengers}")],
        [sg.Text(f"Low Passengers: {counts_obj.low_passengers}")],
        [sg.Text(f"Major Freight: {counts_obj.major_freight}")],
        [sg.Text(f"Minor Freight: {counts_obj.minor_freight}")],
        [sg.Text(f"Incidental Freight: {counts_obj.incidental_freight}")],
        [sg.Text(f"Thank you for using the Galactic Trade Network!")],
        [sg.Button("Back"), sg.Button("Exit")],
    ]
    if counts_obj.mail_exists:
        layout2 = [
            [
                sg.Text(
                    f"Here is the available traffic from {departure_planet} to {destination_planet}"
                )
            ],
            [sg.Text(f"High Passengers: {counts_obj.high_passengers}")],
            [sg.Text(f"Middle Passengers: {counts_obj.middle_passengers}")],
            [sg.Text(f"Basic Passengers: {counts_obj.basic_passengers}")],
            [sg.Text(f"Low Passengers: {counts_obj.low_passengers}")],
            [sg.Text(f"Major Freight: {counts_obj.major_freight}")],
            [sg.Text(f"Minor Freight: {counts_obj.minor_freight}")],
            [sg.Text(f"Incidental Freight: {counts_obj.incidental_freight}")],
            [sg.Text(f"Mail Containers: {counts_obj.mail_containers}")],
            [sg.Text(f"Thank you for using the Galactic Trade Network!")],
            [sg.Button("Back"), sg.Button("Exit")],
        ]

    return layout2
