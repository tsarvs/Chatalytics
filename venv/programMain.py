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

        messageDict = dataWizard.messageDict

        #calculations on said data structures
        #statWizard.calculate_messages_per_author(messageDict)
        #statWizard.calculate_messages_per_day(messageDict)
        #statWizard.calculate_messages_per_time(messageDict)
        #statWizard.calculate_word_frequencies(messageDict)
        #statWizard.calculate_char_frequencies(messageDict)

        #user = 'Nic Holt'
        #statWizard.calculate_user_daily_frequencies(user, messageDict)
        #statWizard.calculate_user_time_frequencies(user, messageDict)
        #statWizard.calculate_user_word_frequencies(user,messageDict)
    except FileNotFoundError:
        print(ERROR_MESSAGE_FILE_NOT_FOUND)
    finally:
        f.close()


main()