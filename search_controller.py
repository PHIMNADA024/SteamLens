from data_loader import DataLoader
import pandas as pd


class SearchController:
    """
    Controller class responsible for handling search operations.
    """

    def __init__(self) -> None:
        """
        Initializes the SearchController instance.
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

    def get_sorting_attributes(self) -> list[str]:
        """
        Retrieves sorting attributes.
        :return: List of sorting attributes.
        """

        return self.data_loader.sorting_attributes

    def search_data(self, search_entry: str, selected_category: str, selected_genre: str,
                    selected_tag: str, selected_windows: int, selected_mac: int, selected_linux: int) -> pd.DataFrame:
        """
        Performs a search based on the provided parameters.
        :param search_entry: String to search for in the data.
        :param selected_category: Selected category for filtering.
        :param selected_genre: Selected genre for filtering.
        :param selected_tag: Selected tag for filtering.
        :param selected_windows: Flag indicating if Windows platform is selected.
        :param selected_mac: Flag indicating if Mac platform is selected.
        :param selected_linux: Flag indicating if Linux platform is selected.
        :return: DataFrame containing the search results.
        """
        search_name = self.get_data()["Name"].str.contains(search_entry, case=False, na=False, regex=False)
        search_dev = self.get_data()["Developers"].str.contains(search_entry, case=False, na=False, regex=False)
        search_pub = self.get_data()["Publishers"].str.contains(search_entry, case=False, na=False, regex=False)

        search_result = self.get_data()[search_name | search_dev | search_pub]
        search_result = search_result.loc[search_result["Linux"]] if selected_linux else search_result
        search_result = search_result.loc[search_result["Mac"]] if selected_mac else search_result
        search_result = search_result.loc[search_result["Windows"]] if selected_windows else search_result

        search_result = search_result[search_result["Categories"].str.contains(selected_category, na=False)] \
            if selected_category != "None" else search_result
        search_result = search_result[search_result["Genres"].str.contains(selected_genre, na=False)] \
            if selected_genre != "None" else search_result
        search_result = search_result[search_result["Tags"].str.contains(selected_tag, na=False)] \
            if selected_tag != "None" else search_result

        return search_result
