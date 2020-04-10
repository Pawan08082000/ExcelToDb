# ExcelToDb

Objective: To convert data from an excel sheet into a table in database. Code should be reusable.

################################
Hardware requirements:
    1. Min i3 8th generation processor
    2. 4GB Ram

Software requirements:
    1. python3.x
    2. xlrd module version 1.2.0
    3. PyCharm or any python IDE.
    4. OS like Windows7 or later/Linux/MacOS.

###############################

ExcelToDb folder have two .xlsx file, two python file, one database file and one text file.

Two Excel Sheets: For testing the code.
    1. NCC_2018.xlsx
    2. Book3.xlsx
Two python files:
    First is "Read_Excel.py" which will open the excel sheet in defined PATH and DataMatrix function
 will return a list which contains the whole excel sheet data.
    Second is "connect_db.py" which will connect the python file to Excel.db(Database file) file.
 connect_db.py have following functions:
        1. Drop_table(table)
        2. Create_table(table)
        3. insert_data(table)
        4. show_data(table)
One database file:
    1. Excel.db

################################

