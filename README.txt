CSV Query - a small command-line for querying CSV files

# Instructions
1. Please make sure all the .py code files are at the same directory as the assignment-data folder which contains the three .csv data files.
2. Move to the working directory and run one of the following commands:
	1) python main.py - enter the interactive shell
	2) python test_table.py -v - run unit tests for each command
	3) python test_solver.py -v - run system integrated tests for various queries
3. This is an interactive command-line program which continues reading input from user. Acceptable input types are:
	1) query string - return query result instantly
	2) q - quit

# Assumptions
1. A valid query string must start with "FROM xxx.csv" which loads at least one table.
2. Though the command keywords are case-insensitive, csv file names and column names are case-sensitive.
3. For the JOIN command, the behavior of INNER JOIN in MySQL is applied.

# Commands
1. FROM command - The FROM command loads a CSV dataset from disk and prints its contents to standard output, preserving the same column ordering as the file.
2. SELECT command - The SELECT command lets you pick particular columns from the loaded dataset and display only those.
3. TAKE command - The TAKE command lets you limit the amount of output to display.
4. ORDERBY command - The ORDERBY command lets you sort the dataset by a single numeric column (and only numeric columns) in descending order.
5. JOIN command - The JOIN command allows the user to combine two .csv datasets based on a common column. Multiple JOIN calls are also allowed.
6. COUNTBY command - The COUNTBY command takes a single column name, and reduces the dataset to only two columns: the specified column after COUNTBY, and a count column.

# Examples
>> FROM city.csv ORDERBY CityPop TAKE 7 SELECT CityName,CityPop
CityName,CityPop
Mumbai_(Bombay),10500000
Seoul,9981619
Sâ€žo_Paulo,9968485
Shanghai,9696300
Jakarta,9604900
Karachi,9269265
Istanbul,8787958
7 row(s) in set

>> FROM city.csv JOIN country.csv CountryCode JOIN language.csv CountryCode TAKE 25
CityID,CityName,CountryCode,CityPop,CountryName,Continent,CountryPop,Capital,Language
1,Kabul,AFG,1780000,Afghanistan,Asia,22720000,1,Balochi
1,Kabul,AFG,1780000,Afghanistan,Asia,22720000,1,Dari
1,Kabul,AFG,1780000,Afghanistan,Asia,22720000,1,Pashto
1,Kabul,AFG,1780000,Afghanistan,Asia,22720000,1,Turkmenian
1,Kabul,AFG,1780000,Afghanistan,Asia,22720000,1,Uzbek
2,Qandahar,AFG,237500,Afghanistan,Asia,22720000,1,Balochi
2,Qandahar,AFG,237500,Afghanistan,Asia,22720000,1,Dari
2,Qandahar,AFG,237500,Afghanistan,Asia,22720000,1,Pashto
2,Qandahar,AFG,237500,Afghanistan,Asia,22720000,1,Turkmenian
2,Qandahar,AFG,237500,Afghanistan,Asia,22720000,1,Uzbek
3,Herat,AFG,186800,Afghanistan,Asia,22720000,1,Balochi
3,Herat,AFG,186800,Afghanistan,Asia,22720000,1,Dari
3,Herat,AFG,186800,Afghanistan,Asia,22720000,1,Pashto
3,Herat,AFG,186800,Afghanistan,Asia,22720000,1,Turkmenian
3,Herat,AFG,186800,Afghanistan,Asia,22720000,1,Uzbek
4,Mazar-e-Sharif,AFG,127800,Afghanistan,Asia,22720000,1,Balochi
4,Mazar-e-Sharif,AFG,127800,Afghanistan,Asia,22720000,1,Dari
4,Mazar-e-Sharif,AFG,127800,Afghanistan,Asia,22720000,1,Pashto
4,Mazar-e-Sharif,AFG,127800,Afghanistan,Asia,22720000,1,Turkmenian
4,Mazar-e-Sharif,AFG,127800,Afghanistan,Asia,22720000,1,Uzbek
5,Amsterdam,NLD,731200,Netherlands,Europe,15864000,5,Arabic
5,Amsterdam,NLD,731200,Netherlands,Europe,15864000,5,Dutch
5,Amsterdam,NLD,731200,Netherlands,Europe,15864000,5,Fries
5,Amsterdam,NLD,731200,Netherlands,Europe,15864000,5,Turkish
6,Rotterdam,NLD,593321,Netherlands,Europe,15864000,5,Arabic
25 row(s) in set

>> FROM city.csv JOIN language.csv CountryCode COUNTBY Language ORDERBY count TAKE 10
Language,count
Chinese,1083
German,885
Spanish,881
Italian,857
English,823
Japanese,774
Portuguese,629
Korean,608
Polish,557
French,467
10 row(s) in set
