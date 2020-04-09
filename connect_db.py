import Read_Excel as ex


# It will take one argument table name and drop the table if it exists in excel.db file.
def drop_table(table):
    cursor.execute("DROP TABLE IF EXISTS {}".format(table))


# It will take one argument table name and create the table.
def create_table(table):
    rt = ""
    for i in range(0, ex.f_read.ncols):
        if i < ex.f_read.ncols - 1:
            rt += ex.typex(i) + ", "
        else:
            rt += ex.typex(i)
    Query1 = """CREATE TABLE {1}({0})""".format(rt, table)
    # print(Query1)
    cursor.execute(Query1)
    # print("created")
    con.commit()


# It will take one argument table name and insert the data into specified table.
def insert_data(table):
    for j in range(0, ex.f_read.nrows - 1):
        t = tuple([x for x in m[j]])
        Query2 = "INSERT INTO {1} VALUES {0}".format(t, table)
        cursor.execute(Query2)
    con.commit()
    # print("inserted")


# It will take one argument table name and will show data according to the sql query.
def show_data(table):
    Query3 = "SELECT TestCaseID FROM {}".format(table)
    cursor.execute(Query3)
    print(cursor.fetchall())


if __name__ == "__main__":
    import sqlite3
    con = sqlite3.connect("Excel.db")
    cursor = con.cursor()
    drop_table("ExcelSheet")
    create_table("ExcelSheet")
    m = ex.DataMatrix()
    del m[0]  # It will delete the first row of m.
    insert_data("ExcelSheet")
    show_data("ExcelSheet")
    con.close()  # it will close the database connection.

