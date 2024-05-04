import tkinter as tk
from search_bar import SearchBar


class HomeMenu(tk.Frame):
    """
    A class representing the Home Menu frame.
    """

    def __init__(self, parent, font, **kwargs) -> None:
        """
        Initializes the HomeMenu frame.

        :param parent: The parent widget.
        :param font: The font to be used in the HomeMenu.
        """
        super().__init__(parent, **kwargs)
        self.config(background="#2A475E")
        self.parent = parent
        self.font = font
        self.search_entry = tk.StringVar()
        self.init_components()

    def init_components(self) -> None:
        """
        Initializes the components of the HomeMenu.
        """
        padding = {'padx': 15, 'pady': 10}
        option = {'font': (self.font, 20)}

        search_frame = tk.LabelFrame(self, text="Search", foreground="white", background="#2A475E", **option)
        search_frame.pack(pady=20)

        self.search_button = tk.Button(search_frame, text="Search", state=tk.DISABLED,
                                       command=self.handler_search_button, **option)
        self.search_button.pack(side=tk.RIGHT, **padding)

        self.search_bar = SearchBar(search_frame, option, self.search_entry, self.search_button, width=40)
        self.search_entry.set("Search game...")
        self.search_bar.bind("<KeyRelease>", self.key_release_search_bar)
        self.search_bar.bind("<Return>", self.handler_search_button)
        self.search_bar.pack(side=tk.LEFT, **padding)

        dashboard_frame = tk.LabelFrame(self, text="Dashboard", foreground="white", background="#2A475E", **option)
        dashboard_frame.pack(pady=20)

        insights_dash_button = tk.Button(dashboard_frame, text="Games Insights Dashboard",
                                         command=lambda: self.parent.change_to_menu(self.parent.dashboard_menu),
                                         **option)
        insights_dash_button.grid(row=0, column=0, sticky="nsew", **padding)

        prices_dis_button = tk.Button(dashboard_frame, text="Games Prices Distribution",
                                      command=lambda: self.parent.change_to_menu(self.parent.price_dist_menu),
                                      **option)
        prices_dis_button.grid(row=0, column=1, sticky="nsew", **padding)

        relationships_button = tk.Button(dashboard_frame, text="Games Relationships",
                                         command=lambda: self.parent.change_to_menu(self.parent.relationship_menu),
                                         **option)
        relationships_button.grid(row=1, column=0, sticky="nsew", **padding)

        released_year_button = tk.Button(dashboard_frame, text="Games released each year",
                                         command=lambda: self.parent.change_to_menu(self.parent.released_year_menu),
                                         **option)
        released_year_button.grid(row=1, column=1, sticky="nsew", **padding)

    def key_release_search_bar(self, *args) -> None:
        """
        Handles the key release event in the search bar.
        """
        if self.search_entry.get():
            self.search_button.config(foreground="black", state=tk.NORMAL)
        else:
            self.search_button.config(foreground="gray", state=tk.DISABLED)

    def handler_search_button(self, *args) -> None:
        """
        Handles the click event of the search button.
        """
        self.parent.search_menu.search_entry.set(self.search_entry.get())
        self.parent.search_menu.search()
        self.parent.change_to_menu(self.parent.search_menu)
