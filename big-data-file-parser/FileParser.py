import pandas as pd
from abc import  ABCMeta,abstractmethod

class FileParserInterface(metaclass = ABCMeta):
    @abstractmethod
    def read(self, file_name):
        pass

    @abstractmethod
    def write(self, file_name, content):
        pass


class CSVParser(FileParserInterface):

    def read(self, file_name):
        return pd.read_csv(file_name)

    def write(self, file_name, content: list):
        data = pd.DataFrame(content)
        data.to_csv(file_name)
        print("Data successfully written in csv files")


class XLSXParser(FileParserInterface):

    def read(self, file_name):
        return pd.read_excel(file_name)

    def write(self, file_name, content: list):
        data = pd.DataFrame(content)
        data.to_excel(file_name)
        print("Data successfully written to xlsx")
