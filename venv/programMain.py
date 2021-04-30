import os
import fileWizard
import dataWizard
import statWizard
import numpy


#put your own file path here for the meantime
CHAT_TEXT_DIRECTORY = "D:\Tom\Desktop\Chatalytics 2021\Backup Text Files\\"

ERROR_MESSAGE_FILE_NOT_FOUND = "Error: File not found"


def main():
    fileName = "main_chat.txt"

    try:
        #step 1: open file
        f = fileWizard.open_read_file(str(CHAT_TEXT_DIRECTORY+fileName))

        #step 2: read through every line, creating data structures
        dataWizard.parse_file(f)

        messageDict = dataWizard.messageDict

        #step 3: calculations on said data structures

        #print("Messages Per Author:\n")
        #statWizard.calculate_messages_per_author(messageDict)

        #print("\nMessages Per Day:\n")
        #statWizard.calculate_messages_per_day(messageDict)

        #print("\nMesages Per Time:\n")
        #statWizard.calculate_messages_per_time(messageDict)

        #print("\nWord Frequencies:\n")
        #statWizard.calculate_word_frequencies(messageDict)

        #print("\nSingle Word Frequency:\n")
        #searchWord = "fuck"
        #statWizard.calculate_single_word_frequency(messageDict, searchWord)

        #print("\nCharacter Frequencies:\n")
        #statWizard.calculate_char_frequencies(messageDict)

        user = 'Xavier'
        #statWizard.calculate_user_daily_frequencies(user, messageDict)
        statWizard.calculate_user_time_frequencies(user, messageDict)
        #statWizard.calculate_user_word_frequencies(user,messageDict)

        #statWizard.calculate_messages_per_author_per_day(messageDict)
    except FileNotFoundError:
        print(ERROR_MESSAGE_FILE_NOT_FOUND)
    finally:
        #step 4: close file
        f.close()


main()