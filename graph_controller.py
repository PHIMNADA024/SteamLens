import tkinter as tk
from data_loader import DataLoader
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
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
        self.selected_games = None

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

    def get_sorting_attributes(self) -> list[str]:
        """
        Retrieves sorting attributes.
        :return: List of sorting attributes.
        """
        return self.data_loader.sorting_attributes

    @staticmethod
    def get_categorical_data() -> list[str]:
        """
        Retrieves categorical data options.

        :return: List of categorical data options.
        """
        return ["Platform", "Categories", "Genres", "Tags"]

    def get_descriptive_statistics(self, attribute: str) -> pd.Series:
        """
        Shows descriptive statistics of an attribute.

        :param attribute: The attribute for which statistics are calculated.
        :return: Series containing descriptive statistics.
        """
        return self.get_data()[attribute].describe()

    def price_dist_graph(self, parent) -> tk.Widget:
        """
        Creates a price distribution histogram graph.

        :param parent: The parent tkinter widget where the graph will be embedded.
        :return: The Tkinter widget containing the price distribution histogram graph.
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

    def released_year_graph(self, parent) -> tk.Widget:
        """
        Creates a graph showing the number of games released each year based on top genres.

        :param parent: The parent tkinter widget where the graph will be embedded.
        :return: The Tkinter widget containing the released year graph.
        """

        data = self.get_data().copy()
        data["Genres"] = data["Genres"].copy().str.split(",").explode('Genres')
        data["Release Year"] = data["Release date"].str.slice(-4).astype('int')

        genre_counts = data.groupby(['Release Year', 'Genres']).size().unstack(fill_value=0)

        top_genres = genre_counts.sum().nlargest(5).index

        ax = genre_counts[top_genres].plot(figsize=(10, 6), marker='o', linestyle='-')

        # Set titles and labels
        ax.set_title('Number of games released each year based on top 5 genres')
        ax.set_xlabel('Release Year')
        ax.set_ylabel('Number of Games')
        years = range(data['Release Year'].min(), data['Release Year'].max() + 1)
        ax.set_xticks(years)
        xtick_labels = [year if year % 5 == 0 else "" for year in years]
        ax.set_xticklabels(xtick_labels, rotation=90)

        ax.grid()

        canvas = FigureCanvasTkAgg(ax.get_figure(), master=parent)
        canvas.draw()

        return canvas.get_tk_widget()

    def relationship_graph(self, parent, left_col, right_col) -> tk.Widget:
        """
        Creates a scatter plot to show the relationship between two columns.
        :param parent: The parent tkinter widget where the graph will be embedded.
        :param left_col: The name of the column to be plotted on the x-axis.
        :param right_col: The name of the column to be plotted on the y-axis.
        :return: The Tkinter widget containing the scatter plot.
        """
        fig = Figure(figsize=(8, 6))
        ax = fig.add_subplot(111)

        data = self.get_data()
        x_data = data[left_col]
        y_data = data[right_col]

        ax.scatter(x_data, y_data)
        ax.set_xlabel(left_col)
        ax.set_ylabel(right_col)

        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()

        return canvas.get_tk_widget()

    def dashboard_graph(self, parent, left_col, right_col, group_by_col) -> tk.Widget:
        """
        Creates a graph for the dashboard.

        :param parent: The parent tkinter widget where the graph will be embedded.
        :param left_col: The name of the column to be plotted on the x-axis.
        :param right_col: The name of the column to be plotted on the y-axis.
        :param group_by_col: The column by which the data will be grouped.
        :return: The Tkinter widget containing the dashboard graph.
        """
        if isinstance(self.selected_games, pd.DataFrame):
            data = self.selected_games.copy()
        else:
            data = self.get_data().copy()
        top_left_values = data[left_col].str.split(",").explode().value_counts().nlargest(5).index
        data[left_col] = data[left_col].apply(lambda x: [val for val in x.split(",") if val in top_left_values])

        fig = Figure(figsize=(10, 8))
        ax = fig.add_subplot(111)

        if group_by_col == "None" or left_col == group_by_col:
            data.explode(left_col).groupby(left_col)[right_col].mean().plot(kind="bar", ax=ax)
        else:
            top_values = data[group_by_col].str.split(",").explode().value_counts().nlargest(5).index
            data[group_by_col] = data[group_by_col].apply(lambda x: [val for val in x.split(",") if val in top_values])
            grouped_data = data.explode(left_col).explode(group_by_col).groupby([left_col, group_by_col])[
                right_col].mean().unstack()
            grouped_data.plot(kind="bar", ax=ax)

        ax.set_xticklabels(labels=top_left_values.to_list(), rotation=0)
        ax.set_xlabel(left_col)
        ax.set_ylabel(right_col)
        ax.legend()
        ax.grid()

        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.draw()

        return canvas.get_tk_widget()
