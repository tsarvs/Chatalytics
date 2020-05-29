import os
import fileWizard
import dataWizard
import statWizard
import numpy


#put your own file path here for the meantime
CHAT_TEXT_FILE = ""

ERROR_MESSAGE_FILE_NOT_FOUND = "Error: File not found"


def main():
    try:
        #open file
        f = fileWizard.open_read_file(CHAT_TEXT_FILE)

        #read through every line, creating data structures
        dataWizard.parse_file(f)

        #calculations on said data structures
        print(dataWizard.messageDict.get(422))
    except FileNotFoundError:
        print(ERROR_MESSAGE_FILE_NOT_FOUND)
    finally:
        f.close()


main()