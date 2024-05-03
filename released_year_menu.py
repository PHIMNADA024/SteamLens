import tkinter as tk
from graph_controller import GraphController


class ReleasedYearMenu(tk.Frame):
    """
    A class representing the released year menu frame.
    """

    def __init__(self, parent, font, **kwargs) -> None:
        """
        Initializes the ReleasedYearMenu frame.

        :param parent: The parent widget.
        :param font: The font to be used in the ReleasedYearMenu.
        """
        super().__init__(parent, **kwargs)
        self.config(background="#2A475E")
        self.parent = parent
        self.font = font
        self.graph_controller = GraphController()
        self.init_components()

    def init_components(self) -> None:
        """
        Initializes the components of the ReleasedYearMenu.
        """
        padding = {'padx': 15, 'pady': 10}
        option = {'font': (self.font, 26)}
        game_release_label = tk.Label(self, text="Games released each year", foreground="white",
                                      background="#2A475E", **option)
        game_release_label.pack(**padding)

        graph_widget = self.graph_controller.released_year_graph(self)
        graph_widget.pack(fill=tk.BOTH, expand=True, **padding)
