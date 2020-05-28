FILE_ENCODING = 'utf-8'
FILE_READING_MODE = 'r'

def open_read_file(fileName):
    f = open(fileName, encoding=FILE_ENCODING, mode=FILE_READING_MODE)

    return f



