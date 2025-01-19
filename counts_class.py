from other_methods import roll_die, roll_x_dice


class StuffCount:
    def __init__(
        self, passenger_counts_dict, freight_counts_dict, mail_exists, cargo_size_arr
    ):
        self.high_passengers = roll_x_dice(passenger_counts_dict[1])
        self.middle_passengers = roll_x_dice(passenger_counts_dict[2])
        self.basic_passengers = roll_x_dice(passenger_counts_dict[3])
        self.low_passengers = roll_x_dice(passenger_counts_dict[4])
        self.major_freight = roll_x_dice(freight_counts_dict[1])
        self.minor_freight = roll_x_dice(freight_counts_dict[2])
        self.incidental_freight = roll_x_dice(freight_counts_dict[3])
        self.major_freight_size = cargo_size_arr[0]
        self.minor_freight_size = cargo_size_arr[1]
        self.incidental_freight_size = cargo_size_arr[2]
        self.mail_exists = mail_exists
        if mail_exists:
            self.mail_containers = roll_die()

    # FIXME outdated - change to use self variables
    def print_available_traffic(
        self, passenger_counts_dict, freight_counts_dict, cargo_size_arr, mail_exists
    ):
        passage_dict = {1: "High", 2: "Middle", 3: "Basic", 4: "Low"}
        freight_dict = {1: "Major", 2: "Minor", 3: "Incidental"}
        for key, item in passenger_counts_dict.items():
            num_passengers = roll_x_dice(item)
            print(f"{num_passengers} {passage_dict[key]} Passage passengers available")

        for key, item in freight_counts_dict.items():
            num_pieces_of_freight = roll_x_dice(item)
            print(
                f"{num_pieces_of_freight} pieces of {cargo_size_arr[key - 1]} ton {freight_dict[key]} Freight available"
            )
        if mail_exists:
            num_mail_containers = roll_die()
            print(
                f"{num_mail_containers} five ton Mail containers available worth Cr25000"
            )
        return
