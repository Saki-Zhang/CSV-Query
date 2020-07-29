# -*- coding: utf-8 -*-

# Created by Zuoqi Zhang on 7/14/20.

from unittest import TestCase, main
from table import Table
from solver import CSVQuerySolver


class TestCSVQuerySolver(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = ['city.csv', 'country.csv', 'language.csv']
        cls.datasets = {}

        for file_name in cls.files:
            file_path = './assignment-data/' + file_name
            table = Table(file_path)
            cls.datasets[file_name] = table

        cls.solver = CSVQuerySolver(cls.datasets)

    def test_parse_1(self):
        query = "FROM city.csv ORDERBY CityPop TAKE 3 SELECT CityName,CityPop"
        result = self.solver.parse(query)

        output = [
            {
                'CityName': 'Mumbai_(Bombay)',
                'CityPop': '10500000'
            },
            {
                'CityName': 'Seoul',
                'CityPop': '9981619'
            },
            {
                'CityName': 'Sâ€žo_Paulo',
                'CityPop': '9968485'
            }
        ]

        assert result.columns == ['CityName', 'CityPop']
        assert result.records == output

    def test_parse_2(self):
        query = "FROM city.csv JOIN language.csv CountryCode SELECT CityID,CityName,CountryCode,Language TAKE 3"
        result = self.solver.parse(query)

        output = [
            {
                'CityID': '1',
                'CityName': 'Kabul',
                'CountryCode': 'AFG',
                'Language': 'Balochi'
            },
            {
                'CityID': '1',
                'CityName': 'Kabul',
                'CountryCode': 'AFG',
                'Language': 'Dari'
            },
            {
                'CityID': '1',
                'CityName': 'Kabul',
                'CountryCode': 'AFG',
                'Language': 'Pashto'
            }
        ]

        assert result.columns == ['CityID', 'CityName', 'CountryCode', 'Language']
        assert result.records == output


if __name__ == '__main__':
    main()
