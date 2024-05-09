import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from search_controller import SearchController
from search_bar import SearchBar
from threading import Thread


class SearchMenu(tk.Frame):
    """
    A class represents the search menu frame for searching and displaying game data.
    """

    def __init__(self, parent, font, **kwargs) -> None:
        """
        Initializes the SearchMenu frame.

        :param parent: The parent widget.
        :param font: The font to be used in the SearchMenu.
        """
        super().__init__(parent, **kwargs)
        self.config(background="#2A475E")
        self.font = font
        self.parent = parent
        self.search_entry = tk.StringVar()
        self.category_selected = tk.StringVar()
        self.category_selected.set("None")
        self.genre_selected = tk.StringVar()
        self.genre_selected.set("None")
        self.tag_selected = tk.StringVar()
        self.tag_selected.set("None")
        self.sorted_attribute_selected = tk.StringVar()
        self.sorted_attribute_selected.set("None")
        self.windows_selected = tk.IntVar()
        self.mac_selected = tk.IntVar()
        self.linux_selected = tk.IntVar()
        self.descending_selected = tk.IntVar()
        self.search_entry.set("Search game...")
        self.search_controller = SearchController()
        self.init_components()

    def init_components(self) -> None:
        """
        Initializes the components of the SearchMenu.
        """
        padding = {'padx': 15, 'pady': 2}
        option = {'font': (self.font, 10)}
        self.search_frame_option(option, padding)
        self.games_library_table_option(option, padding)
        self.selected_games_table_option(option, padding)
        self.insight_button = tk.Button(self, text="Compare", font=(self.font, 12), command=self.compare_games)
        self.insight_button.bind("<Return>", self.compare_games)
        self.insight_button.pack(pady=10)

    def search_frame_option(self, option, padding) -> None:
        """
        Configures the search frame and its components.

        :param option: Dictionary containing font settings for widget configuration.
        :param padding: Dictionary containing padding values.
        """
        search_frame = tk.LabelFrame(self, text="Search", foreground="white", background="#2A475E", **option)
        search_frame.pack(pady=10, ipady=10)

        self.search_button = tk.Button(search_frame, text="Search", command=self.search, **option)
        self.search_button.grid(row=0, column=3, sticky="ew", **padding)

        self.search_bar = SearchBar(search_frame, option, self.search_entry, self.search_button, width=35)
        self.search_bar.bind("<Return>", self.search)
        self.search_bar.grid(row=0, column=0, columnspan=3, sticky="nsew", **padding)
        self.search_entry.trace_add("write", self.check_enable_search)

        available_platform = tk.Label(search_frame, text="Available platform",
                                      foreground="white", background="#2A475E", **option)
        available_platform.grid(row=1, column=0, sticky="w", **padding)

        categories_label = tk.Label(search_frame, text="Categories",
                                    foreground="white", background="#2A475E", **option)
        categories_label.grid(row=1, column=1, **padding)
        self.category_selected.trace_add("write", self.check_enable_search)

        categories_option = ttk.Combobox(search_frame, state="readonly", textvariable=self.category_selected, **option)
        categories_option['values'] = self.search_controller.get_unique_categories()
        categories_option.grid(row=2, column=1, **padding)

        genres_label = tk.Label(search_frame, text="Genres",
                                foreground="white", background="#2A475E", **option)
        genres_label.grid(row=1, column=2, **padding)

        genres_option = ttk.Combobox(search_frame, state="readonly", textvariable=self.genre_selected, **option)
        genres_option['values'] = self.search_controller.get_unique_genres()
        genres_option.grid(row=2, column=2, **padding)
        self.genre_selected.trace_add("write", self.check_enable_search)

        tags_label = tk.Label(search_frame, text="Tags",
                              foreground="white", background="#2A475E", **option)
        tags_label.grid(row=1, column=3, **padding)

        tags_option = ttk.Combobox(search_frame, state="readonly", textvariable=self.tag_selected, **option)
        tags_option['values'] = self.search_controller.get_unique_tags()
        tags_option.grid(row=2, column=3, **padding)
        self.tag_selected.trace_add("write", self.check_enable_search)

        self.windows_checkbutton = tk.Checkbutton(search_frame, text="Windows", variable=self.windows_selected,
                                                  background="#2A475E", activebackground="#2A475E",
                                                  foreground="white", activeforeground="white",
                                                  selectcolor="black", **option)
        self.windows_checkbutton.grid(row=2, column=0, sticky="w", padx=10)
        self.windows_selected.trace_add("write", self.check_enable_search)

        self.mac_checkbutton = tk.Checkbutton(search_frame, text="Mac", variable=self.mac_selected,
                                              background="#2A475E", activebackground="#2A475E",
                                              foreground="white", activeforeground="white",
                                              selectcolor="black", **option)
        self.mac_checkbutton.grid(row=3, column=0, sticky="w", padx=10)
        self.mac_selected.trace_add("write", self.check_enable_search)

        self.linux_checkbutton = tk.Checkbutton(search_frame, text="Linux", variable=self.linux_selected,
                                                background="#2A475E", activebackground="#2A475E",
                                                foreground="white", activeforeground="white",
                                                selectcolor="black", **option)
        self.linux_checkbutton.grid(row=4, column=0, sticky="w", padx=10)
        self.linux_selected.trace_add("write", self.check_enable_search)

        sort_by_label = tk.Label(search_frame, text="Sorted by", foreground="white", background="#2A475E", **option)
        sort_by_label.grid(row=4, column=1, sticky="e", padx=15)

        self.sorted_option = ttk.Combobox(search_frame, state="readonly",
                                          textvariable=self.sorted_attribute_selected, **option)
        self.sorted_option['values'] = self.search_controller.get_sorting_attributes()
        self.sorted_option.current(0)
        self.sorted_option.grid(row=4, column=2, padx=15)
        self.sorted_option.bind("<<ComboboxSelected>>", self.check_enable_search)

        self.descending_checkbutton = tk.Checkbutton(search_frame, text="Descending order",
                                                     variable=self.descending_selected, state=tk.DISABLED,
                                                     background="#2A475E", activebackground="#2A475E",
                                                     foreground="white", activeforeground="white",
                                                     selectcolor="black", **option)
        self.descending_checkbutton.grid(row=4, column=3, sticky="w", padx=10)

        self.descending_selected.trace_add("write", self.check_enable_search)
        self.sorted_option.bind("<<ComboboxSelected>>", self.toggle_descending_state)
        self.sorted_attribute_selected.trace_add("write", self.check_enable_search)

    def toggle_descending_state(self, *args) -> None:
        """
        Toggles the state of the descending order checkbutton based on the selected sorting attribute.
        """
        if self.sorted_attribute_selected.get() == "None":
            self.descending_checkbutton.config(state=tk.DISABLED)
        else:
            self.descending_checkbutton.config(state=tk.NORMAL)

    def compare_games(self) -> None:
        """
        Compares the selected games.
        """
        selected_games = [self.selected_games_table.item(item)['values']
                          for item in self.selected_games_table.get_children()]
        if not selected_games:
            messagebox.showwarning("Warning", "You must select any game to compare them.")
            return

        selected_games_df = pd.DataFrame(selected_games, columns=self.search_controller.get_data_columns())
        for column in self.search_controller.get_sorting_attributes()[1:]:
            selected_games_df[column] = selected_games_df[column].astype(float)
        self.parent.dashboard_menu.graph_controller.selected_games = selected_games_df
        self.parent.dashboard_menu.update_graph()
        self.parent.change_to_menu(self.parent.dashboard_menu)

    def check_enable_search(self, *args) -> None:
        """
        Checks if the search button should be enabled based on the selected criteria.
        """
        if (self.search_entry.get() and self.search_entry.get() != "Search game..." or self.windows_selected.get() or
                self.mac_selected.get() or self.linux_selected.get() or self.category_selected.get() != "None" or
                self.genre_selected.get() != "None" or self.tag_selected.get() != "None" or
                self.sorted_attribute_selected.get() != "None"):
            self.search_button.config(foreground="black", state=tk.NORMAL)
        else:
            self.search_button.config(foreground="gray", state=tk.DISABLED)

    def games_library_table_option(self, option, padding) -> None:
        """
        Configures the game library table and its components.

        :param option: Dictionary containing font settings for widget configuration.
        :param padding: Dictionary containing padding values.
        """
        library_text = tk.Label(self, text="Game library", foreground="white", background="#2A475E", **option)
        library_text.pack(ipady=10, **padding)

        self.games_library_table = ttk.Treeview(self, columns=self.search_controller.get_data_columns(),
                                                selectmode="browse", show="headings", height=5)
        for column in self.search_controller.get_data_columns():
            self.games_library_table.column(column, width=80)
            self.games_library_table.heading(column, text=column)

        self.games_library_table.bind("<Double-Button-1>", func=self.insert_selected_game)
        self.games_library_table.pack(padx=40)

        library_scrollbar = ttk.Scrollbar(self, orient="horizontal", command=self.games_library_table.xview)
        library_scrollbar.pack(fill=tk.BOTH, expand=True, padx=40)

        self.games_library_table.config(xscrollcommand=library_scrollbar.set)

    def selected_games_table_option(self, option, padding) -> None:
        """
        Configures the selected games table and its components.

        :param option: Dictionary containing font settings for widget configuration.
        :param padding: Dictionary containing padding values.
        :return: None
        """

        selected_games_text = tk.Label(self, text="Selected Games", foreground="white", background="#2A475E", **option)
        selected_games_text.pack(ipady=10, **padding)

        self.selected_games_table = ttk.Treeview(self, columns=self.search_controller.get_data_columns(),
                                                 selectmode="browse", show="headings", height=5)

        for column in self.search_controller.get_data_columns():
            self.selected_games_table.column(column, width=80)
            self.selected_games_table.heading(column, text=column)

        self.selected_games_table.bind("<Double-Button-1>", func=self.deselect_game)
        self.selected_games_table.pack(padx=40)

        self.selected_games_scrollbar = ttk.Scrollbar(self, orient="horizontal",
                                                      command=self.selected_games_table.xview)
        self.selected_games_scrollbar.pack(fill=tk.BOTH, expand=True, padx=40)

        self.selected_games_table.config(xscrollcommand=self.selected_games_scrollbar.set)

    def insert_search_result(self, search_results) -> None:
        """
        Inserts search results into the game library table.

        :param search_results: List of search results.
        """
        self.games_library_table.delete(*self.games_library_table.get_children())
        [self.games_library_table.insert('', 'end', iid=result[0], values=result)
         for result in search_results]

    def search(self, *args) -> None:
        """
        Executes the search operation based on user inputs.
        """
        if self.search_entry.get() == "Search game...":
            search_entry = ""
        else:
            search_entry = self.search_entry.get()
            self.search_bar.config(foreground="black")
        search_result = self.search_controller.search_data(
            search_entry,
            self.category_selected.get(),
            self.genre_selected.get(),
            self.tag_selected.get(),
            self.windows_selected.get(),
            self.mac_selected.get(),
            self.linux_selected.get(),
        )

        if self.sorted_attribute_selected.get() == "None":
            sorting_thread = Thread(target=lambda: self.insert_search_result(search_result.to_numpy().tolist()[:100]))
            sorting_thread.start()
        else:
            if self.descending_selected.get():
                sorting_thread = Thread(target=lambda: self.insert_search_result(
                    search_result.sort_values(self.sorted_attribute_selected.get(), ascending=False).
                    to_numpy().tolist()[:100]
                ))
                sorting_thread.start()
            else:
                sorting_thread = Thread(target=lambda: self.insert_search_result(
                    search_result.sort_values(self.sorted_attribute_selected.get()).
                    to_numpy().tolist()[:100]
                ))
                sorting_thread.start()

    def insert_selected_game(self, *args) -> None:
        """
        Inserts the selected game into the selected games table.
        """
        selected_game = self.games_library_table.item(self.games_library_table.focus())['values']
        if self.check_duplicate(selected_game):
            messagebox.showwarning("Warning", "You cannot select the same game twice.")
        else:
            self.selected_games_table.insert('', 'end', values=selected_game)

    def deselect_game(self, *args) -> None:
        """
        Remove the selected game from the selected games table
        """

        try:
            self.selected_games_table.delete(self.selected_games_table.selection()[0])
        except IndexError:
            pass

    def check_duplicate(self, selected_game) -> bool:
        """
        Checks if the selected game is already present in the selected games table.

        :param selected_game: The selected game.
        :return: True if the game is already present, False otherwise.
        """
        selected_game_title = selected_game[0]
        for child in self.selected_games_table.get_children():
            values = self.selected_games_table.item(child)['values']
            if values and values[0] == selected_game_title:
                return True
        return False
