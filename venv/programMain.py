import os
import fileWizard
import dataWizard


CHAT_TEXT_FILE = "D:\Tom\Documents\WhatsApp\_chat.txt"
ERROR_MESSAGE_FILE_NOT_FOUND = "Error: File does not exist"


def test():
    try:
        f = fileWizard.open_read_file(CHAT_TEXT_FILE)

        dataWizard.parse_file(f)
    except FileNotFoundError:
        print(ERROR_MESSAGE_FILE_NOT_FOUND)
    finally:
        f.close()

def main():
    test()


main()