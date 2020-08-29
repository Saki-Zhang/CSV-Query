# -*- coding: utf-8 -*-

# Created by Zuoqi Zhang on 7/12/20.

from table import Table
from solver import CSVQuerySolver

if __name__ == '__main__':
    files = ['city.csv', 'country.csv', 'language.csv']
    datasets = {}  # key: csv file, value: table

    for file_name in files:
        file_path = './assignment-data/' + file_name
        table = Table(file_path)
        datasets[file_name] = table

    solver = CSVQuerySolver(datasets)

    print(">> Please enter your query string, enter 'q' to quit...\n")

    while True:
        query = str(input('>> '))  # wait for user to enter a query string

        if query == 'q':  # quit
            break
        else:
            try:
                solver.execute(query)
            except Exception as e:
                print(e)

        print()
