import tkinter as tk


class SearchBar(tk.Entry):
    """
    Custom search bar widget.
    """

    def __init__(self, parent, option, search_entry: tk.StringVar, search_button: tk.Button, width: int) -> None:
        """
        Initializes the SearchBar widget.

        :param parent: The parent widget.
        :param option: A dictionary containing font settings for configuring the SearchBar.
        :param search_entry: The StringVar variable for the search entry.
        :param search_button: The search button associated with the SearchBar.
        :param width: The width of the SearchBar.
        """
        super().__init__(parent, textvariable=search_entry, foreground="gray", width=width, **option)
        self.parent = parent
        self.search_entry = search_entry
        self.search_button = search_button
        self.bind("<FocusIn>", self.focusin_search_entry)
        self.bind("<Leave>", self.focusout_search_entry)

    def focusin_search_entry(self, *args) -> None:
        """
        Handles the focus in event for the search entry.
        """
        if self.search_entry.get() == "Search game...":
            self.search_entry.set("")
            self.config(foreground="black")

    def focusout_search_entry(self, *args) -> None:
        """
        Handles the focus out event for the search entry.
        """
        self.parent.focus_set()
        if self.search_entry.get() == "":
            self.search_entry.set("Search game...")
            self.config(foreground="gray")
