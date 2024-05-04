import tkinter as tk
from home_menu import HomeMenu
from search_menu import SearchMenu
from price_dist_menu import PriceDistMenu
from released_year_menu import ReleasedYearMenu
from relationship_menu import RelationshipMenu
from dashboard_menu import DashboardMenu


class SteamLensUI(tk.Tk):
    """
    Graphical user interface for the SteamLens application.
    """

    def __init__(self) -> None:
        """
        Initializes the SteamLensUI instance.
        """
        super().__init__()
        self.title("SteamLens")
        self.config(background="#2A475E")
        self.geometry("1280x720")
        self.font = "Segoe UI"

        self.home_menu = HomeMenu(self, self.font)
        self.search_menu = SearchMenu(self, self.font)
        self.price_dist_menu = PriceDistMenu(self, self.font)
        self.released_year_menu = ReleasedYearMenu(self, self.font)
        self.relationship_menu = RelationshipMenu(self, self.font)
        self.dashboard_menu = DashboardMenu(self, self.font)

        self.menus = [self.home_menu, self.search_menu, self.price_dist_menu, self.released_year_menu,
                      self.relationship_menu, self.dashboard_menu]

        self.init_components()

    def init_components(self) -> None:
        """
        Initializes the components of the SteamLensUI.
        """
        padding = {'padx': 20, 'pady': 20}

        menu_frame = tk.Frame(self, background="#171A21")
        menubar = tk.Menubutton(menu_frame, text="Menu", font=(self.font, 18))
        menubar.pack(side=tk.LEFT)
        menu_choice = tk.Menu(menubar)
        menu_choice.add_command(label="Home",
                                command=lambda: self.change_to_menu(self.home_menu))
        menu_choice.add_separator()
        menu_choice.add_command(label="Search",
                                command=lambda: self.change_to_menu(self.search_menu))
        menu_choice.add_command(label="Prices Distribution",
                                command=lambda: self.change_to_menu(self.price_dist_menu))
        menu_choice.add_command(label="Release Year",
                                command=lambda: self.change_to_menu(self.released_year_menu))
        menu_choice.add_command(label="Relationship",
                                command=lambda: self.change_to_menu(self.relationship_menu))
        menu_choice.add_command(label="Games Insights Dashboard",
                                command=lambda: self.change_to_menu(self.dashboard_menu))
        menu_choice.add_separator()
        menu_choice.add_command(label="Quit", command=self.quit)
        menubar.config(menu=menu_choice)
        menu_frame.pack(fill=tk.X)

        title_frame = tk.Frame(self, background="#1B2838")
        title_frame.pack(fill=tk.X)
        title = tk.Label(title_frame, text="SteamLens", font=(self.font, 60, "bold"),
                         background="#1B2838", foreground="white")
        title.pack(fill=tk.X)

        self.home_menu.pack(**padding)

    def change_to_menu(self, new_menu):
        padding = {'padx': 20, 'pady': 20}

        for menu in self.menus:
            if menu != new_menu:
                menu.pack_forget()

        new_menu.pack(**padding)

    def run(self) -> None:
        """
        Runs the SteamLensUI application.
        """
        self.mainloop()
