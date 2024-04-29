import tkinter as tk
from data_loader import DataLoader
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
matplotlib.use("TkAgg")


class GraphController:
    """
    A class that manages graph-related operations.
    """

    def __init__(self) -> None:
        """
        Initializes the GraphController instance.
        """
        self.data_loader = DataLoader.get_instance()

    def get_data(self) -> pd.DataFrame:
        """
        Retrieves the raw data.
        :return: DataFrame containing the raw data.
        """
        return self.data_loader.data

    def get_data_columns(self) -> list[str]:
        """
        Retrieves the column names of the data.
        :return: List of column names.
        """
        return self.data_loader.data_columns

    def get_unique_categories(self) -> list[str]:
        """
        Retrieves unique categories from the data.
        :return: List of unique categories.
        """
        return self.data_loader.unique_categories

    def get_unique_genres(self) -> list[str]:
        """
        Retrieves unique genres from the data.
        :return: List of unique genres.
        """
        return self.data_loader.unique_genres

    def get_unique_tags(self) -> list[str]:
        """
        Retrieves unique tags from the data.
        :return: List of unique tags.
        """
        return self.data_loader.unique_tags

    def price_dist_graph(self, parent) -> tk.Widget:
        """
        Creates a price distribution histogram graph.
        :param parent: The parent tkinter widget where the graph will be embedded.
        """
        fig, ax = plt.subplots(figsize=(8, 6))

        ax.hist(np.log10(self.get_data()["Price"].replace(0, 0.1)), bins=20)
        ax.set_xlabel('Price')
        ax.set_ylabel('Frequency')
        ax.set_title('Price Distribution')
        xticks = ax.get_xticks()
        ax.set_xticks(xticks)
        xtick_labels = [10 ** tick if tick % 1 == 0 else "" for tick in xticks]
        ax.set_xticklabels(xtick_labels)

        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()

        return canvas.get_tk_widget()

    def price_dist_statistics(self) -> pd.Series:
        """
        Shows descriptive statistics of price distribution.
        """
        price_data = self.get_data()["Price"]
        statistics = price_data.describe()

        return statistics
