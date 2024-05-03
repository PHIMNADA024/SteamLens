import tkinter as tk
from graph_controller import GraphController


class PriceDistMenu(tk.Frame):
    """
    A class representing a frame for displaying the price distribution graph and descriptive statistics.
    """

    def __init__(self, parent, font, **kwargs) -> None:
        """
        Initializes the SearchMenu frame.

        :param parent: The parent widget.
        :param font: The font to be used in the PriceDistMenu.
        """
        super().__init__(parent, **kwargs)
        self.config(background="#2A475E")
        self.parent = parent
        self.font = font
        self.graph_controller = GraphController()
        self.init_components()

    def init_components(self) -> None:
        """
        Initializes the UI components of the price distribution menu.
        """
        self.init_graph_frame()
        self.init_stat_frame()

    def init_graph_frame(self) -> None:
        """
        Initializes the frame for displaying the price distribution graph.
        """
        padding = {'padx': 15, 'pady': 10}
        option = {'font': (self.font, 26)}

        self.graph_frame = tk.Frame(self, background="#2A475E")
        self.graph_frame.pack(side=tk.LEFT, **padding)

        price_label = tk.Label(self.graph_frame, text="Price of Game in Steam", foreground="white",
                               background="#2A475E", **option)
        price_label.pack(**padding)

        graph_widget = self.graph_controller.price_dist_graph(self.graph_frame)
        graph_widget.pack(fill=tk.BOTH, expand=True)

    def init_stat_frame(self) -> None:
        """
        Initializes the frame for displaying descriptive statistics.
        """
        padding = {'padx': 15, 'pady': 10}
        option = {'font': (self.font, 26)}

        self.stat_frame = tk.Frame(self, background="#2A475E")
        self.stat_frame.pack(side=tk.RIGHT, padx=30)

        stat_label = tk.Label(self.stat_frame, text="Descriptive Statistics", foreground="white",
                               background="#2A475E", **option)
        stat_label.pack(**padding)

        descriptive_stats_label = tk.Label(self.stat_frame, text=self.get_descriptive_stats_text(), foreground="white",
                                           background="#2A475E", font=(self.font, 22), justify=tk.LEFT)
        descriptive_stats_label.pack(**padding)

    def get_descriptive_stats_text(self) -> str:
        """
        Retrieves the descriptive statistics text.

        :returns: The descriptive statistics text.
        """
        price_stats = self.graph_controller.get_descriptive_statistics("Price")
        descriptive_stats = (
            f"Count: {price_stats['count']}\n"
            f"Mean: {price_stats['mean']:.2f}\n"
            f"Std Deviation: {price_stats['std']:.2f}\n"
            f"Minimum: {price_stats['min']:.2f}\n"
            f"25th Percentile: {price_stats['25%']:.2f}\n"
            f"Median: {price_stats['50%']:.2f}\n"
            f"75th Percentile: {price_stats['75%']:.2f}\n"
            f"Maximum: {price_stats['max']:.2f}\n"
        )
        return descriptive_stats
