import pandas as pd
from threading import Thread


class DataLoader:
    """
    A singleton class for loading and preprocessing data from a file.
    """

    _instance = None

    def __new__(cls, data_file) -> 'DataLoader':
        """
        Creates a singleton instance of the DataLoader class if it doesn't already exist.

        :param data_file: Path to the data file.
        :return: DataLoader instance
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self, data_file) -> None:
        """
        Initializes the DataLoader instance.

        :param data_file: Path to the data file.
        """
        if self.__initialized:
            return
        self.__initialized = True
        self.data_thread = Thread(target=lambda: self.load_data(data_file))
        self.data_thread.start()
        self.data_thread.join()
        self.data_categories = self.__data["Categories"].copy().str.split(",").explode('Categories').unique()
        self.data_genres = self.__data["Genres"].copy().str.split(",").explode('Genres').unique()
        self.data_tags = self.__data["Tags"].copy().str.split(",").explode('Tags').unique()
        self.__sorting_attributes = ["None", "Price", "Metacritic score", "User score",
                                     "Positive", "Negative", "Recommendations"]
        self.preprocess_data()

    @classmethod
    def get_instance(cls) -> 'DataLoader':
        """
        Retrieves the singleton instance of the DataLoader class.

        :return: DataLoader instance
        """
        return cls._instance

    @property
    def data(self) -> pd.DataFrame:
        """
        Retrieves the loaded data.

        :return: DataFrame containing the loaded data.
        """
        return self.__data

    @property
    def data_columns(self) -> list[str]:
        """
        Retrieves the columns of the loaded data.

        :return: List of column names.
        """
        return self.data.columns.to_list()

    @property
    def unique_categories(self) -> list[str]:
        """
        Retrieves unique categories from the loaded data.

        :return: List of unique category names.
        """
        return ["None"] + list(self.data_categories)

    @property
    def unique_genres(self) -> list[str]:
        """
        Retrieves unique genres from the loaded data.

        :return: List of unique genre names.
        """
        return ["None"] + list(self.data_genres)

    @property
    def unique_tags(self) -> list[str]:
        """
        Retrieves unique tags from the loaded data.

        :return: List of unique tag names.
        """
        return ["None"] + list(self.data_tags)

    @property
    def sorting_attributes(self) -> list[str]:
        """
        Retrieves sorting attributes.

        :return: List of sorting attributes.
        """
        return self.__sorting_attributes

    def load_data(self, data_file: str) -> None:
        """
        Loads data from the specified file.

        :param data_file: Path to the data file.
        """
        try:
            if data_file[-3:] == "csv":
                self.__data = pd.read_csv(data_file)
            else:
                self.__data = pd.DataFrame()
        except FileNotFoundError:
            print(f"Error: {data_file} not found.")
            self.__data = pd.DataFrame()

    def preprocess_data(self) -> None:
        """
        Preprocesses the loaded data.
        """
        self.__data = self.__data.drop(columns=['Score rank', 'Reviews', 'Metacritic url', 'Notes'])
        self.__data = self.__data.dropna(subset=['Name'])
        self.__data[['About the game', 'Website', 'Support url', 'Support email', 'Screenshots', 'Movies']] = \
            (self.__data[['About the game', 'Website', 'Support url', 'Support email', 'Screenshots', 'Movies']].fillna
                ("Information not available"))
        self.__data[['Developers', 'Publishers', 'Categories', 'Genres', 'Tags']] = \
            (self.__data[['Developers', 'Publishers', 'Categories', 'Genres', 'Tags']].fillna("Unknown"))
