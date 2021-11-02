import os
from typing import List, Optional, Union
import pandas as pd


class CacheDF:
    """
    Writes dataframes to disk as parquet files as a way of "cahing"

    Attributes:
        cache_dir (str): relative path to directory to store cached df's parquet files

    Methods:
        cache(df, uuid): writes a dataframe to disk as a parquet file
        read(uuid): reads a parquet file from disk and returns the dataframe
        uncache(uuid): deletes a parquet file from disk
        clear(): deletes all parquet files from disk
        is_cached(uuid): checks if a parquet file exists on disk
    """

    def __init__(self, cache_dir: str):
        """
        Initializes the CacheDF object

        Args:
            cache_dir (str): relative path to directory to store cached df's parquet files
        """
        self.cache_dir = cache_dir
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def cache(self, df: pd.DataFrame, uuid: str):
        """
        Writes a dataframe to disk as a parquet file

        Args:
            df (pandas.DataFrame): dataframe to write to disk
            uuid (str): Unique identifier for the dataframe used to name the parquet file
        """
        df.to_parquet(os.path.join(self.cache_dir, uuid + ".parquet"))

    def read(self, uuid: str, columns: Optional[List[str]]=None) -> Union[pd.DataFrame, FileNotFoundError]:
        """
        Reads a parquet file from disk and returns the dataframe

        Args:
            uuid (str): Unique identifier for the dataframe used to name the parquet file
            columns (Optional[List[str]]): list of columns to read from the dataframe (default: None: read all columns)
        Returns:
            pandas.DataFrame: dataframe read from disk
        
        Raises:
            FileNotFoundError: if the file does not exist on disk
        """
        if not self.is_cached(uuid):
            raise FileNotFoundError(f"{uuid} not found in cache directory")

        if columns is None:
            return pd.read_parquet(os.path.join(self.cache_dir, uuid + ".parquet"))
        else:
            return pd.read_parquet(os.path.join(self.cache_dir, uuid + ".parquet"), columns=columns)

    def uncache(self, uuid: str):
        """
        Deletes a parquet file from disk

        Args:
            uuid (str): Unique identifier for the dataframe used to name the parquet file
        """
        if self.is_cached(uuid):
            os.remove(os.path.join(self.cache_dir, uuid + ".parquet"))

    def clear(self: str):
        """
        Deletes all parquet files from disk
        """
        for file in os.listdir(self.cache_dir):
            os.remove(os.path.join(self.cache_dir, file))

    def is_cached(self, uuid: str) -> bool:
        """
        Checks if a parquet file exists on disk

        Args:
            uuid (str): Unique identifier for the dataframe used to name the parquet file

        Returns:
            bool: True if the file exists on disk, False otherwise
        """
        return os.path.exists(os.path.join(self.cache_dir, uuid + ".parquet"))
