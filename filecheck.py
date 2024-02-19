

from pathlib import Path
import os
import shutil

##### My code has one user_inter face function that call three different functions (first_line,second_line,third_line)




def user_interface():    # Everything happen here like master_function
    ''' user_interface function call three function
    inside and it is main function of my code '''

    list_of_path1 = first_line_input()
    list_of_path2 = second_line_input(list_of_path1)
    third_input_line(list_of_path2)






#############----------------------------------functions that I use in my three functions ----------------------------------###########



def read_directories(P:'Path')->list: # This function is basically for 'D' input
    '''This function check for the directories
    print them and return them in list and also
    do the sort part in this function  '''

    directories_list =[]
    for directories in P.iterdir():
        directories_list.append(directories)
        if directories.is_file():
            print(directories)
    directories_list.sort()
    return directories_list



def read_directories_recursive(P: 'Path')->list: #This function is basically for 'R' input
    '''This function check for the directories if there are subdirectories show
    them by recursive function , print directories and return them in list. Also,
    do the sort part in ths function'''

    directories_list = []
    for directories in P.iterdir():
        if directories.is_file():
           directories_list.append(directories)
           print(directories)
    directories_list.sort()

    for directories in P.iterdir():
        if directories.is_dir() == True:
            new_dir_list =read_directories_recursive(directories)
            directories_list.extend(new_dir_list)

    return directories_list


def search_for_file(listPath:list,userInput:str)->list: #This function is for input  'N'
    '''This function is searching for file name with
    specific name and return them in list '''
    newList=[]
    for i in range(len(listPath)):
       if listPath[i].name == userInput:
           newList.append(listPath[i])
    for num in range(len(newList)):
        print(newList[num])

    return newList

def search_for_extension(listPath:list,userInput:str)->list: # This function is for input 'E'
    '''This function get list of path and take look at specific
    extension which is string input and return them in list'''
    newList=[]
    for i in range(len(listPath)):
       if listPath[i].suffix.strip('.') == userInput:
           newList.append(listPath[i])
           for num in range(len(newList)):
               print(newList[num])

    return newList


def check_inside_of_the_txt_file(listPath:list, userInput:str)->list: #This function is for input 'T'
    '''This function get list of path and string input if the file is
        text file then and that user input was in there then return list of file '''
    newList = []
    for i in range(len(listPath)):
        try:
            if userInput in listPath[i].read_text() :
                newList.append(listPath[i])
        except UnicodeDecodeError: #This error happen when the read text function doesn't work without the text file
            pass

    return newList


def compare_for_less_size(listPath:list, userInput:int)->list: #This function is for input '<'
    '''This function get  number and list of path ,compare size of each path
    and return list of the path which is less then that size'''
    newList = []
    for i in range(len(listPath)):
        if os.path.getsize(listPath[i]) < userInput:
            newList.append(listPath[i])
            for num in range(len(newList)):
                print(newList[num])
    return newList




def compare_for_more_size(listPath:list, userInput) -> list: # This function is for input '>'
    '''This function get  number and list of path ,compare size of each path
       and return list of the path which is more then that size'''
    newList = []
    for i in range(len(listPath)):
        if os.path.getsize(listPath[i]) > userInput:
            newList.append(listPath[i])
            for num in range(len(newList)):
                print(newList[num])
    return newList


def read_first_line_of_file(listPath:list)->str: #This part is for 'F' input
    '''This function read first line of
    the file if it is text file  '''


    for i in listPath:
        try:
            file_in_str = i.open('r')
            a = file_in_str.readline()
            print(a, end='')
            file_in_str.close()


        except:
            print('NOT TEXT')

    return str




def make_copy(listPath:list): #This part is for input 'D'
    '''This function make copy of the file
    in the same directories '''

    for i in range(len(listPath)):
        f_path = str(listPath[i])
        new_path = str(listPath[i]) + ".dup"
        print(shutil.copyfile(f_path,new_path))

def touch_function(listPath:list): #This part is for input 'T'
    '''This function is for touching file which means
    to modify its last modified timestamp'''
    for i in range(len(listPath)):
        f_path =listPath[i]
        f_path.touch()












######################______________________First_line,second_line,third_line____________#####################


def first_line_input()->list:
    '''This function is for the first line of the input
    handel the errors and return list '''
    while True:
        user_input = input()
        command = user_input[0:2].strip()
        if Path(user_input[2:].strip()).exists() == True :
            inputPath = Path(user_input[2:].strip())
            if command == 'D' :
                return read_directories(inputPath)
            elif command == 'R' :
                return read_directories_recursive(inputPath)
            else :
                print('ERROR')
        else :
            print('ERROR')



def second_line_input(pathList:list)->list:
    '''This function is for the second line of input take
    the list and  handel the errors and return list'''
    while True:
        user_input = input()
        command = user_input[0:2].strip()
        command2 = user_input[2:].strip()

        if command == 'N':
            if command2 != '':
                 return search_for_file(pathList, command2)
            else:
                print('ERROR')

        elif command == 'A':
            print(pathList)
            return pathList

        elif command == 'E':
            if command2 !='':
                print('E')
                return search_for_extension(pathList,command2)
            else:
                print('ERROR')

        elif command == 'T':
            if command2 != '':
                return check_inside_of_the_txt_file(pathList, command2)
            else:
                print('ERROR')

        elif command == '<':
            if command2 != '':
                try:
                    if type(int(command2)) == int:
                        number =int(command2)
                        return compare_for_less_size(pathList, number)
                except ValueError:
                    print('ERROR')
            else:
                print('ERROR')
        elif command == '>':
            if command2 != '':
                try:
                    if type(int(command2)) == int:
                        number = int(command2)
                        return compare_for_less_size(pathList, number)
                except ValueError:
                    print('ERROR')
            else:
                print('ERROR')
        else:
            print('ERROR')


def third_input_line(listPath:list)->None:
    '''This function is for third line of input
    get list of path and handel error '''

    while True:
        if listPath == []:
            break
        user_input = input()
        command = user_input[0:2].strip()


        if command == 'F':
            read_first_line_of_file(listPath)
            return

        elif command == 'D':
            make_copy(listPath)
            return


        elif command == 'T':
            touch_function(listPath)
            return
        else:
         print('ERROR')






##############________________________________First_line,second_line,third_line____________________###################



if __name__ == '__main__':
   user_interface()
