from trade_tables import process_uwp_file


if __name__ == "__main__":
    input_file = "hex_codes.txt"  # Input file containing hex codes
    output_file = "planets.json"  # Output JSON file

    process_uwp_file(input_file, output_file)
