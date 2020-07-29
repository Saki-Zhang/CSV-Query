# -*- coding: utf-8 -*-

# Created by Zuoqi Zhang on 7/12/20.


class CSVQuerySolver:
    def __init__(self, datasets):
        """ initialize the CSV query solver with datasets

        :param datasets: dictinary of datasets (key: csv file, value: table)
        :type datasets: dict
        """
        self.operators = ['FROM', 'SELECT', 'TAKE', 'ORDERBY', 'JOIN', 'COUNTBY']
        self.datasets = datasets

    def parse(self, query):
        """ parse the query string word by word and return the output table

        :param query: query string entered by user
        :type query: str
        :rtype: Table
        """
        # remove zero-width spaces in the query string, especially when copied from the .pdf file
        # split the query string into a list of keywords by space
        query = query.replace('\u200b', '').strip()
        kwrds = query.split(' ')

        # the first two elements of a valid input should be ['FROM', 'xxx.csv']
        if len(kwrds) == 0 or kwrds[0].upper() != 'FROM':
            raise Exception("Invalid query: your query should start with \"FROM xxx.csv\"\nCommands: {}".format(kwrds))

        assert kwrds[1] in self.datasets, "File name {} is not found".format(kwrds[1])

        # FROM xxx.csv
        table_name = kwrds[1]
        table = self.datasets[table_name].copy()  # get the table from datasets and create a copy

        i = 2  # start from index 2

        while i < len(kwrds):
            if kwrds[i].upper() == 'FROM':  # FROM should only appear at the start of the query string
                raise Exception("Unexpected keyword FROM is found at position {}\nCommands: {}".format(i, kwrds))
            elif kwrds[i].upper() == 'JOIN':  # JOIN xxx.csv COLUMN_NAME
                try:
                    arg1 = kwrds[i + 1]  # xxx.csv
                    arg2 = kwrds[i + 2]  # COLUMN_NAME
                    i += 2

                    assert arg1 in self.datasets, "File name {} not found".format(arg1)
                    assert arg2 not in self.operators, "Missing column name for JOIN operation"
                except:
                    raise Exception(
                        "The JOIN cmd should take exactly two inputs: CSV file, column name\nCommands: {}".format(
                            kwrds))

                t = self.datasets[arg1]
                c_name = arg2
                table.join(table=t, col_name=c_name)
            elif kwrds[i].upper() == 'SELECT':  # SELECT COLUMN_NAME1[,COLUMN_NAME2,COLUMN_NAME3,...]
                try:
                    arg1 = kwrds[i + 1]  # COLUMN_NAME1[,COLUMN_NAME2,COLUMN_NAME3,...]
                    i += 1

                    assert arg1 not in self.operators
                except:
                    raise Exception(
                        "The SELECT cmd should take exactly one input: column names\nCommands: {}".format(kwrds))

                c_names = arg1.split(',')
                table.select(col_names=c_names)
            elif kwrds[i].upper() == 'TAKE':  # TAKE LIMIT
                try:
                    arg1 = kwrds[i + 1]  # LIMIT
                    i += 1

                    assert arg1 not in self.operators
                except:
                    raise Exception("The TAKE cmd should take exactly one input: limit\nCommands: {}".format(kwrds))

                try:
                    limit = int(arg1)
                except ValueError:
                    raise Exception("Invalid number {} is provided".format(arg1))
                table.take(num_rows=limit)
            elif kwrds[i].upper() == 'ORDERBY':  # ORDERBY COLUMN_NAME
                try:
                    arg1 = kwrds[i + 1]  # COLUMN_NAME
                    i += 1

                    assert arg1 not in self.operators
                except:
                    raise Exception(
                        "The ORDERBY cmd should take exactly one input: column name\nCommands: {}".format(kwrds))

                c_name = arg1
                table.order_by(col_name=c_name)
            elif kwrds[i].upper() == 'COUNTBY':  # COUNTBY COLUMN_NAME
                try:
                    arg1 = kwrds[i + 1]  # COLUMN_NAME
                    i += 1

                    assert arg1 not in self.operators
                except:
                    raise Exception(
                        "The COUNTBY cmd should take exactly one input: column name\nCommands: {}".format(kwrds))

                c_name = arg1
                table.count_by(col_name=c_name)
            else:
                raise Exception(
                    "Unexpected keyword {} is found at position {}\nCommands: {}".format(kwrds[i], i, kwrds))

            i += 1

        return table

    def execute(self, query):
        """ parse the query string and print the result

        :param query: query string entered by user
        :type query: str
        """
        table = self.parse(query)
        table.print()
