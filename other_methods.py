from random import randint


def roll_die():
    return randint(1, 6)


def roll_on_passenger_traffic_table(
    die_mod_obj,
    table_obj,
    highest_skill,
    steward_skill,
    source_planet,
    destination_planet,
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


def roll_on_freight_traffic_table(
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
    num_cargo = table_obj.freight_traffic_table(roll_die() + roll_die(), die_mod)
    return num_cargo


def check_if_mail_exists(
    die_mod_obj,
    source_planet,
    destination_planet,
    armed,
    naval_or_scout_rank,
    social_die_mod,
):
    mail_exists = True
    mail_does_not_exist = False
    die_roll = roll_die() + roll_die()
    die_mod = die_mod_obj.mail_mods(
        source_planet, destination_planet, armed, naval_or_scout_rank, social_die_mod
    )
    if die_roll + die_mod >= 12:
        return mail_exists
    else:
        return mail_does_not_exist


def generate_passenger_counts(
    passenger_quality_arr,
    die_mods_obj,
    trade_tables_obj,
    highest_skill,
    steward_skill,
    source_planet,
    destination_planet,
    parsecs_travelled,
):
    passenger_rolls_dict = {}
    for quality in passenger_quality_arr:
        traffic = roll_on_passenger_traffic_table(
            die_mods_obj,
            trade_tables_obj,
            highest_skill,
            steward_skill,
            source_planet,
            destination_planet,
            quality,
            parsecs_travelled,
        )
        passenger_rolls_dict.update({quality: traffic})
    return passenger_rolls_dict


def generate_freight_counts(
    freight_quality_arr,
    die_mods_obj,
    trade_tables_obj,
    highest_skill,
    source_planet,
    destination_planet,
    parsecs_travelled,
):
    freight_rolls_dict = {}
    for quality in freight_quality_arr:
        traffic = roll_on_freight_traffic_table(
            die_mods_obj,
            trade_tables_obj,
            highest_skill,
            source_planet,
            destination_planet,
            quality,
            parsecs_travelled,
        )
        freight_rolls_dict.update({quality: traffic})
    return freight_rolls_dict


def generate_freight_sizes():
    major_cargo = roll_die() * 10
    minor_cargo = roll_die() * 5
    incidental_cargo = roll_die()
    return [major_cargo, minor_cargo, incidental_cargo]


def roll_x_dice(num_dice):
    summation = 0
    for _ in range(num_dice):
        summation += roll_die()
    return summation


def print_available_traffic(
    passenger_counts_dict, freight_counts_dict, cargo_size_arr, mail_exists
):
    passage_dict = {1: "High", 2: "Middle", 3: "Basic", 4: "Low"}
    freight_dict = {1: "Major", 2: "Minor", 3: "Incidental"}
    for key, item in passenger_counts_dict.items():
        num_passengers = roll_x_dice(item)
        print(f"{num_passengers} {passage_dict[key]} Passage passengers available")

    for key, item in freight_counts_dict.items():
        num_pieces_of_freight = roll_x_dice(item)
        print(
            f"{num_pieces_of_freight} pieces of {cargo_size_arr[key-1]} ton {freight_dict[key]} Freight available"
        )
    if mail_exists:
        num_mail_containers = roll_die()
        print(f"{num_mail_containers} five ton Mail containers available")
    return
