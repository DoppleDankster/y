#!/usr/bin/env python3

"""
name_a_celeb.py: pick a random user title for each doto celebrity

returns a JSON payload with each Celebrity as a key and the title as value
"""

__author__ = "DoppleDankser"
__version__ = "1.0.0"
__email__ = "davidmedioni@protonmail.com"

import sys
from os import path
from random import choice
from pprint import pprint
from pandas import DataFrame
from pandas.errors import ParserError
import pandas as pd


def validate_filepath(filepath):
    if path.exists(filepath):
        return True
    print(f"File {filepath} not found")
    return False


def run():
    filepath = sys.argv[1]
    if not validate_filepath(filepath):
        return
    dataframe = Dataframe(filepath)
    randomizer = Randomizer(dataframe=dataframe)
    randomizer.roll_for_each_celeb()
    pprint(randomizer.report)
    return randomizer.report


class Dataframe:
    def __init__(self, filepath):
        self.dataframe = Dataframe.load_csv(filepath)

    @staticmethod
    def load_csv(filepath: str) -> DataFrame:
        try:
            df = pd.read_csv(filepath)
            df.fillna("n/a", inplace=True)
            return df
        except ParserError:
            print(f"File {filepath} is not a valid CSV")
            sys.exit(1)

    def get_celebrities(self):
        return list(self.dataframe.columns)

    def get_titles_for_celebrity(self, celebrity: str) -> list:
        return self.dataframe[celebrity].tolist()

    def pick_random_celebrity(self) -> str:
        return choice(self.get_celebrities())

    def remove_user_votes(self, index: int) -> None:
        self.dataframe = self.dataframe.drop([index])

    def remove_celebrity(self, celebrity: str) -> None:
        self.dataframe = self.dataframe.drop(columns=celebrity, axis=1)

    def pick_random_title(self, celebrity: str) -> str:
        title_list = self.get_titles_for_celebrity(celebrity)
        sanitized_list = Dataframe.sanitize_title_list(title_list)
        if sanitized_list == []:
            return "n/a"
        return choice(sanitized_list)

    @staticmethod
    def sanitize_title_list(title_list):
        return [title for title in title_list if title != "n/a"]

    def get_title_row(self, title: str) -> int:
        """
        Return the index of the row containing a given title
        """
        cell = self.dataframe[self.dataframe.eq(title).any(1)]
        return cell.index.tolist()[0]


class Randomizer:
    def __init__(self, dataframe: Dataframe):
        self.data = dataframe
        self.report = {}

    def roll(self) -> (str, str):
        celebrity = self.data.pick_random_celebrity()
        title = self.data.pick_random_title(celebrity)
        return (celebrity, title)

    def purge_dataframe(self, celebrity, title):
        if title != "n/a":
            title_index = self.data.get_title_row(title)
            self.data.remove_user_votes(title_index)
        self.data.remove_celebrity(celebrity)

    def roll_for_each_celeb(self):
        """
        Roll a new title for each celebrity
        """

        celebrities = self.data.get_celebrities()
        for _ in celebrities:
            celebrity, title = self.roll()
            self.purge_dataframe(celebrity, title)
            self.report[celebrity] = title


if __name__ == "__main__":
    run()
