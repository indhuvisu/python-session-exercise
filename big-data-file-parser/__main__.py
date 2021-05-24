from FileParser import CSVParser, XLSXParser


# This method will create Parser object based on the file selected by user
def __get_parser(filename):
    if ".csv" in filename:
        print("Returning CSV Parser")
        return CSVParser()
    elif ".xlsx" in filename:
        print("Returning XLSX Parser")
        return XLSXParser()

    raise Exception(
        "UnSupported file type.File extension currently we support are .csv/.xlsx.Please provide valid file")


def main():
    filename = input("Enter FileName : ")
    operation = input("Choose operation read/write ? ")
    parser = __get_parser(filename)
    if operation == "write":
        parser.write(filename, [["30C", "day1"], ["40C", "day2"]])
    else:
        data = parser.read(filename)
        print(data)


# Driver code
if __name__ == '__main__':
    main()
