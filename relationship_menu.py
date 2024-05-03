import tkinter as tk
from tkinter import ttk
from graph_controller import GraphController


class RelationshipMenu(tk.Frame):
    """
    A class representing the relationship menu for displaying the relationship between two columns.
    """

    def __init__(self, parent, font, **kwargs) -> None:
        """
        Initializes the RelationshipMenu frame.

        :param parent: The parent widget.
        :param font: The font to be used in the RelationshipMenu.
        """
        super().__init__(parent, **kwargs)
        self.config(background="#2A475E")
        self.parent = parent
        self.font = font
        self.graph_controller = GraphController()
        self.column_left_selected = tk.StringVar()
        self.column_left_selected.set("Price")
        self.column_right_selected = tk.StringVar()
        self.column_right_selected.set("User score")
        self.init_components()

    def init_components(self) -> None:
        """
        Initializes the components of the RelationshipMenu.
        """
        padding = {'padx': 15, 'pady': 10}
        option = {'font': (self.font, 20)}
        relationship_frame = tk.Frame(self, background="#2A475E")
        relationship_frame.pack(**padding)
        relationship_label = tk.Label(relationship_frame, text="Relationship between", foreground="white",
                                      background="#2A475E", **option)
        relationship_label.grid(row=0, column=0, **padding)
        column_left_option = ttk.Combobox(relationship_frame, state="readonly", textvariable=self.column_left_selected,
                                          **option)
        column_left_option['values'] = self.graph_controller.get_sorting_attributes()[1:]
        column_left_option.bind("<<ComboboxSelected>>", self.update_attributes)
        column_left_option.grid(row=0, column=1, **padding)
        and_label = tk.Label(relationship_frame, text="and", foreground="white", background="#2A475E", **option)
        and_label.grid(row=0, column=2, **padding)

        column_right_option = ttk.Combobox(relationship_frame, state="readonly",
                                           textvariable=self.column_right_selected, **option)
        column_right_option['values'] = self.graph_controller.get_sorting_attributes()[1:]
        column_right_option.bind("<<ComboboxSelected>>", self.update_attributes)
        column_right_option.grid(row=0, column=3, **padding)

        self.graph_widget = self.graph_controller.relationship_graph(self, self.column_left_selected.get(),
                                                                     self.column_right_selected.get())
        self.graph_widget.pack(side=tk.LEFT, **padding)

        self.stat_frame = tk.Frame(self, background="#2A475E")
        self.stat_frame.pack(side=tk.RIGHT, padx=30)

        stat_label = tk.Label(self.stat_frame, text="Descriptive Statistics", foreground="white",
                              background="#2A475E", **option)
        stat_label.pack(**padding)

        self.descriptive_stats_label = tk.Label(self.stat_frame, text=self.get_descriptive_stats_text(),
                                                foreground="white",
                                                background="#2A475E", font=(self.font, 18), justify=tk.LEFT)
        self.descriptive_stats_label.pack(**padding)

    def update_attributes(self, *args) -> None:
        """
        Updates the selected attributes and updates the graph and descriptive statistics label.
        """
        padding = {'padx': 15, 'pady': 10}
        if self.graph_widget:
            self.graph_widget.destroy()
        self.graph_widget = self.graph_controller.relationship_graph(self, self.column_left_selected.get(),
                                                                     self.column_right_selected.get())
        self.graph_widget.pack(**padding)

        if self.descriptive_stats_label:
            self.descriptive_stats_label.destroy()
        self.descriptive_stats_label = tk.Label(self.stat_frame, text=self.get_descriptive_stats_text(),
                                                foreground="white",
                                                background="#2A475E", font=(self.font, 18), justify=tk.LEFT)
        self.descriptive_stats_label.pack(**padding)

    def get_descriptive_stats_text(self) -> str:
        """
        Retrieves the descriptive statistics text.

        :returns: The descriptive statistics text.
        """
        x_statistics = self.graph_controller.get_descriptive_statistics(self.column_left_selected.get())
        y_statistics = self.graph_controller.get_descriptive_statistics(self.column_right_selected.get())
        descriptive_stats = (
            f"{self.column_left_selected.get()} Summary Statistics\n"
            f"Count: {x_statistics['count']}\n"
            f"Mean: {x_statistics['mean']:.2f}\n"
            f"Std Deviation: {x_statistics['std']:.2f}\n"
            f"Minimum: {x_statistics['min']:.2f}\n"
            f"25th Percentile: {x_statistics['25%']:.2f}\n"
            f"Median: {x_statistics['50%']:.2f}\n"
            f"75th Percentile: {x_statistics['75%']:.2f}\n"
            f"Maximum: {x_statistics['max']:.2f}\n\n"

            f"{self.column_right_selected.get()} Summary Statistics\n"
            f"Count: {y_statistics['count']}\n"
            f"Mean: {y_statistics['mean']:.2f}\n"
            f"Std Deviation: {y_statistics['std']:.2f}\n"
            f"Minimum: {y_statistics['min']:.2f}\n"
            f"25th Percentile: {y_statistics['25%']:.2f}\n"
            f"Median: {y_statistics['50%']:.2f}\n"
            f"75th Percentile: {y_statistics['75%']:.2f}\n"
            f"Maximum: {y_statistics['max']:.2f}\n"
        )
        return descriptive_stats
