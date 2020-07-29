# -*- coding: utf-8 -*-

# Created by Zuoqi Zhang on 7/14/20.

from unittest import TestCase, main
from table import Table


class TestTable(TestCase):
    def test_select(self):
        table = Table("./assignment-data/city.csv")
        col_names = ['CityName', 'CityPop']
        table.select(col_names)

        assert table.columns == col_names
        assert list(table.records[0].keys()) == col_names

    def test_take(self):
        table = Table("./assignment-data/city.csv")
        num_rows = 10
        table.take(num_rows)

        assert len(table.records) <= num_rows

    def test_join(self):
        table = Table("./assignment-data/city.csv")
        table2 = Table("./assignment-data/country.csv")
        col_name = 'CountryCode'
        table.join(table2, col_name)

        output = {
            'CityID': '1',
            'CityName': 'Kabul',
            'CountryCode': 'AFG',
            'CityPop': '1780000',
            'CountryName': 'Afghanistan',
            'Continent': 'Asia',
            'CountryPop': '22720000',
            'Capital': '1'
        }

        assert table.columns.count(col_name) == 1
        assert table.records[0] == output

    def test_order_by(self):
        table = Table("./assignment-data/city.csv")
        col_name = 'CityPop'
        table.order_by(col_name)

        output = {
            'CityID': '1024',
            'CityName': 'Mumbai_(Bombay)',
            'CountryCode': 'IND',
            'CityPop': '10500000'
        }

        assert table.records[0] == output

    def test_count_by(self):
        table = Table("./assignment-data/language.csv")
        col_name = 'Language'
        table.count_by(col_name)

        output = {
            'Language': 'English',
            'count': '60'
        }

        assert table.columns == [col_name, 'count']
        assert output in table.records


if __name__ == '__main__':
    main()
