import tkinter as tk
from tkinter import ttk
from threading import Thread
from graph_controller import GraphController


class DashboardMenu(tk.Frame):
    """
    DashboardMenu represents the menu interface for the dashboard.
    """

    def __init__(self, parent, font, **kwargs) -> None:
        """
        Initializes the DashboardMenu frame.

        :param parent: The parent widget.
        :param font: The font to be used in the DashboardMenu.
        """
        super().__init__(parent, **kwargs)
        self.config(background="#2A475E")
        self.parent = parent
        self.font = font
        self.graph_controller = GraphController()
        self.column_left_selected = tk.StringVar()
        self.column_left_selected.set("Platform")
        self.column_right_selected = tk.StringVar()
        self.column_right_selected.set("Price")
        self.group_by_selected = tk.StringVar()
        self.group_by_selected.set("None")
        self.init_components()

    def init_components(self) -> None:
        """
        Initializes components of the DashboardMenu.
        """
        padding = {'padx': 15, 'pady': 10}
        option = {'font': (self.font, 20)}

        choice_frame = tk.Frame(self, background="#2A475E")
        choice_frame.pack(**padding)

        column_left_option = ttk.Combobox(choice_frame, state="readonly", width=15,
                                          textvariable=self.column_left_selected,
                                          **option)
        column_left_option['values'] = self.graph_controller.get_categorical_data()
        column_left_option.bind("<<ComboboxSelected>>", self.update_graph)
        column_left_option.grid(row=0, column=0, **padding)
        versus_label = tk.Label(choice_frame, text="versus", foreground="white", background="#2A475E", **option)
        versus_label.grid(row=0, column=1, **padding)

        column_right_option = ttk.Combobox(choice_frame, state="readonly", width=15,
                                           textvariable=self.column_right_selected, **option)
        column_right_option['values'] = self.graph_controller.get_sorting_attributes()[1:]
        column_right_option.bind("<<ComboboxSelected>>", self.update_graph)
        column_right_option.grid(row=0, column=2, **padding)

        group_by_label = tk.Label(choice_frame, text="group by", foreground="white", background="#2A475E", **option)
        group_by_label.grid(row=0, column=3, **padding)

        group_by_option = ttk.Combobox(choice_frame, state="readonly", width=15, textvariable=self.group_by_selected,
                                       **option)
        group_by_option['values'] = ["None"] + self.graph_controller.get_categorical_data()
        group_by_option.bind("<<ComboboxSelected>>", self.update_graph)
        group_by_option.grid(row=0, column=4, **padding)

        reset_button = tk.Button(choice_frame, text="Reset to all games", command=self.reset_dataframe, **option)
        reset_button.grid(row=0, column=5, sticky="ew", **padding)

        self.loading_label = tk.Label(self, text="Loading...", foreground="white", background="#2A475E", **option)


        self.graph_widget = self.graph_controller.dashboard_graph(self, self.column_left_selected.get(),
                                                                  self.column_right_selected.get(),
                                                                  self.group_by_selected.get())
        self.graph_widget.pack(**padding)

    def reset_dataframe(self, *args) -> None:
        """
        Resets the selected games DataFrame to None and updates the graph.
        """
        self.graph_controller.selected_games = None
        self.update_graph()

    def update_graph(self, *args) -> None:
        """
        Updates the graph based on user selections.
        """
        padding = {'padx': 15, 'pady': 10}
        if self.graph_widget:
            self.graph_widget.destroy()

        self.update_thread = Thread(target=self.update_graph_async)
        self.update_thread.start()
        self.check_update_graph()
        self.loading_label.pack(**padding)

    def check_update_graph(self) -> None:
        """
        Check if the update thread is still alive.
        """
        if self.update_thread.is_alive():
            self.after(10, self.check_update_graph)
        else:
            self.loading_label.pack_forget()
            self.graph_widget.pack()

    def update_graph_async(self) -> None:
        """
        Updates the graph asynchronously.
        """
        self.graph_widget = self.graph_controller.dashboard_graph(self, self.column_left_selected.get(),
                                                                  self.column_right_selected.get(),
                                                                  self.group_by_selected.get())
        self.check_update_graph()
