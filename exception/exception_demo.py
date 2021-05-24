"""This module demonstrates examples for python exception handling
Take Away:
#1 Usage of Assert,raise
#2 Usage of Try, except,else,finally
"""
import platform


def check_is_linux():
    # print( platform.system())
    assert("linux" in platform.system()), "This script expect the linux platform fro the execution"

def check_is_non_negative(num):
    if num >= 0:
        pass
    else:
        """Raising custom exceptions based on conditions"""
        raise Exception("Negative num")

def read_file(divider_num):
    input_file = None
    output_file = None
    try:
        #check_is_linux()
        input_file = open("MyFile.txt", "r+")
        num = int(input_file.readline())
        check_is_non_negative(divider_num)
        num = num / divider_num #raise zero deivision error if input is 0
    except AssertionError as Exception:
        print("Os compatibility pblm")
    except ZeroDivisionError as Exception:
        print("Logical cliche")
    else:
        """On a successful try execution ie without exception 
        control flow will reach here"""

        print("File has been read and calculations done successfully..copying the result in result.txt")
        output_file = open("result.txt","w")
        output_file.write(str(num))
    finally:
        """All clean up activities will come under finally block, 
        and no matter what happened on try except or else, finally block will 
        always get executed as final stage"""
        if input_file is not None:
            print("Input stream is still open closing anyway at final stage")
            input_file.close()
        if output_file is not None:
            output_file.close()
        print("Cleanup like closing files are done")


if __name__ == '__main__':
    # check_is_linux()
    read_file(int(input("Enter divider value ")))
