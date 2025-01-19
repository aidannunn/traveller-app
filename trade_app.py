from pathlib import Path


from UWPCalc.PlanetAPI import PlanetAPI

from gui import TradeGUI

if __name__ == "__main__":
    planet_api_obj = PlanetAPI()
    home_dir = Path(__file__).parent
    icon_path = home_dir.joinpath("ship-logo.ico")
    gui = TradeGUI(icon_path, planet_api_obj)
    gui.run_gui()
