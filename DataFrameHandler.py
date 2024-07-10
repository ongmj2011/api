import pandas as pd
import datetime


class DataFrameHandler:
    """ A static class to handle reading and writing .csv data

    Attributes:
        OUTPUT_ID: used to track the ID of the output files if needed
    """

    OUTPUT_ID = 0

    @staticmethod
    def read_csv(file_path):
        """ Converts a .csv file into a Data frame using pandas.

        :param file_path: .csv file to be read.

        :return: A data frame with data from the .csv

        :raise: Exceptions if the data frame does not have a "Latitude" and a "Longitude" column
        """

        data_frame = pd.read_csv(file_path)
        #comment back when done with weather_data_processing 
        #if "Latitude" not in data_frame.columns:
        #    raise Exception("Latitude not present in this file")
        #if "Longitude" not in data_frame.columns:
        #    raise Exception("Longitude not present in this file")
        return data_frame

    @staticmethod
    def write_csv(data_frame):
        """Create a .csv file from a data frame.

        :param data_frame: A data frame to be convereted into .csv

        :return: A .csv file
        """

        csv = data_frame.to_csv(f"output/Output - {datetime.date.today()}.csv")
        DataFrameHandler.OUTPUT_ID += 1
        return csv

    @staticmethod
    def write_to_dataframe(data_frame, column_name, column_data):
        """Add additional columns to an existing data frame.

        :param data_frame: Data Frame for columns to be added to.
        :param column_name: String name for column.
        :param column_data: List of data for the column.

        :return: A data frame with added columns.
        """

        data_frame.loc[:, column_name] = column_data
        return data_frame