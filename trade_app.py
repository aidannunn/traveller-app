from pathlib import Path
from UWPCalc.PlanetAPI import PlanetAPI
from ship_stats_reader import ShipStats

from gui import TradeGUI

if __name__ == "__main__":
    planet_api_obj = PlanetAPI()
    ship_stats_obj = ShipStats()
    home_dir = Path(__file__).parent
    icon_path = home_dir.joinpath("ship-logo.ico")
    gui = TradeGUI(icon_path, planet_api_obj, ship_stats_obj)
    gui.run_gui()