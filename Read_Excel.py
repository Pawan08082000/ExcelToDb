import xlrd

PATH = "Book3.xlsx"
f = xlrd.open_workbook(PATH)  # It will open the Excel sheet from defined PATH.
f_read = f.sheet_by_index(0)


# for converting the Excel sheet data into matrix From.

def DataMatrix():
    List, fList = [], []
    for rows in range(0, f_read.nrows):
        for col in range(f_read.ncols):
            List.append(f_read.cell_value(rows, col))
        fList.append(List)
        List = []
    return fList


m = DataMatrix()


# typex(a) function returns column_name and data_type of Table
# typex(a) fun is used while creating a Table
def typex(a):
    v = type(m[1][a])
    if v == float:
        return str(m[0][a]) + " real"
    elif v == int:
        return str(m[0][a]) + " integer"
    else:
        return str(m[0][a]) + " text"
