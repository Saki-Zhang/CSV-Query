# -*- coding: utf-8 -*-

# Created by Zuoqi Zhang on 7/12/20.

import csv
import json


class Table:
    def __init__(self, file_path=None):
        """ initialize a table from a csv file

        :param file_path: path to the csv file
        :type file_path: str
        """
        if file_path is None:
            self.columns = []
            self.records = []

            return

        with open(file_path) as csv_file:
            reader = csv.DictReader(csv_file)
            header = reader.fieldnames
            data = []

            for row in reader:
                data.append(row)
            data = json.dumps(data)
            data = json.loads(data)

        self.columns = header
        self.records = data

    def select(self, col_names=None):
        """ pick particular columns from the loaded dataset and display only those

        :param col_names: list of column names to select
        :type col_names: list
        """
        if col_names is None or col_names == []:
            return

        for col_name in col_names:
            assert col_name in self.columns, "Column {} is not found in table".format(col_name)

        records = []

        for record in self.records:
            r = record.copy()  # create a new copy to avoid modifying the original record
            for col_name in self.columns:
                if col_name not in col_names:
                    r.pop(col_name, None)  # drop the columns that will not be displayed
            records.append(r)  # append new record into result

        self.records = records
        self.columns = col_names

    def take(self, num_rows):
        """ limit the amount of output to display

        :param num_rows: number of records to display
        :type num_rows: int
        """
        assert num_rows >= 0, "Invalid number {} is provided".format(num_rows)

        self.records = self.records[:num_rows]  # keep the first num_rows records in result

    def join(self, table, col_name):
        """ combine with another table based on a common column

        :param table: table to join with
        :type table: Table
        :param col_name: name of the common column to join on
        :type col_name: str
        """
        assert col_name in self.columns, "Column {} is not found in table".format(col_name)
        assert col_name in table.columns, "Column {} is not found in table".format(col_name)

        records = []

        for r1 in self.records:
            for r2 in table.records:
                if r1[col_name] == r2[col_name]:
                    r = r1.copy()  # create a new copy to avoid modifying the original r1
                    r.update(r2)  # merge two dicts r and r2 without duplicate key
                    records.append(r)  # append new record into result

        self.records = records

        for col in table.columns:
            if col != col_name:
                self.columns.append(col)  # add new column names except the common column

    def order_by(self, col_name):
        """ sort the dataset by a single numeric column in descending order

        :param col_name: name of the numeric column to sort by
        :type col_name: str
        """
        assert col_name in self.columns, "Column {} is not found in table".format(col_name)

        # use a lambda expression to define the sorting rule (need to convert the value type from str to int)
        # set reverse to true for descending order
        try:
            self.records = sorted(self.records, key=lambda i: int(i[col_name]), reverse=True)
        except ValueError:
            raise Exception("Selected column {} is not numeric".format(col_name))

    def count_by(self, col_name, count='count'):
        """ count the number of times values of the specified column appear in the dataset

        :param col_name: name of the column to count by
        :type col_name: str
        :param count: name of the new count column
        :type count: str
        """
        assert col_name in self.columns, "Column {} is not found in table".format(col_name)

        hashmap = {}  # use a hashmap to store the number of appearances for each unique value

        for record in self.records:
            val = record[col_name]
            if val not in hashmap:
                hashmap[val] = 0
            hashmap[val] += 1  # increment the number of appearances by 1

        records = []  # add each value and its number of appearances into result

        for k, v in hashmap.items():
            record = {
                col_name: k,  # value
                count: str(v)  # number of appearances of the value
            }
            records.append(record)

        self.records = records
        self.columns = [col_name, count]  # result will only have two columns: the specified column and a count column

    def print(self):
        if len(self.columns) == 0 and len(self.records) == 0:
            print("0 row(s) in set")
            return

        # print column names (header)
        print(','.join(self.columns))

        # print each record row by row (data)
        for record in self.records:
            row = []
            for col in self.columns:
                row.append(record[col])
            print(','.join(row))

        print("{} row(s) in set".format(len(self.records)))

    def copy(self):
        # this method is to return a new copy of table
        # in order to avoid modifying the orignial one
        table = Table()
        table.columns = self.columns.copy()
        table.records = self.records.copy()

        return table
