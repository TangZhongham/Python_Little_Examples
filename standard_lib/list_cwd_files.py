import os
import glob


class OsInfo(object):
    def __init__(self):
        print("Scanning current directory...\n")
        cwd = os.getcwd()
        print('Current working directory is: ' + cwd)

    def show_files(self):
        search_files = glob.glob('*')
        if len(search_files) != 0:
            return '\n'.join(search_files)
        else:
            return '0'


if __name__ == '__main__':
    os = OsInfo()
    show_file = os.show_files()
    print('\nCurrent files and directorys: ' + 'show_file')

