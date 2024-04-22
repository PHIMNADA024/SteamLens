from steamlens_ui import SteamLensUI
from data_loader import DataLoader

DATA_FILE = "games.csv"


if __name__ == '__main__':
    data_loader = DataLoader(DATA_FILE).get_instance()
    ui = SteamLensUI()
    ui.run()
