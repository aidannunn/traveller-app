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
        [sg.Text(f"Thank you for using the Galactic Trade Network!")],
        [sg.Button("Back"), sg.Button("Exit")],
    ]
    return layout2
