import tkinter as tk
from home_menu import HomeMenu
from search_menu import SearchMenu


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
        menubar.config(menu=menu_choice)
        menu_frame.pack(fill=tk.X)

        title_frame = tk.Frame(self, background="#1B2838")
        title_frame.pack(fill=tk.X)
        title = tk.Label(title_frame, text="SteamLens", font=(self.font, 60, "bold"),
                         background="#1B2838", foreground="white")
        title.pack(fill=tk.X)

        self.home_menu = HomeMenu(self, self.font)
        self.home_menu.pack(**padding)

        self.search_menu = SearchMenu(self, self.font)

    def switch_to_search_menu(self) -> None:
        """
        Switches to the search menu.
        """
        self.winfo_children()[-2].pack_forget()
        self.search_menu.pack()

    def run(self) -> None:
        """
        Runs the SteamLensUI application.
        """
        self.mainloop()
