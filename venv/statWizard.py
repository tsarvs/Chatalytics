import re
import pandas

regexString_Number = "^\d+$"
numberRegex = re.compile(regexString_Number)

#good for getting usage timelines of the chat based off of it's users
def calculate_messages_per_author_per_day(messageDict):
    #key for authorDict will be on 1. author and 2. time
    authorDict = {}

    for key, ((msg_date, msg_time),(msg_author, msg_text)) in messageDict.items():

        time_key = msg_date

        if ("System Notification" not in msg_author) \
                and (" created group " not in msg_author) \
                and (" joined using this group's invite link" not in msg_author) \
                and ("now an admin" not in msg_author):
            if (msg_author,time_key) in authorDict:
                authorDict[msg_author,time_key] += 1
            else:
                authorDict[msg_author,time_key] = 1

    for (x,y) in authorDict:
        print(str(x) + '\t' + str(y) + '\t' + str(authorDict[x,y]))

def calculate_messages_per_author(messageDict):
    authorDict = {}

    for key, ((msg_date, msg_time),(msg_author, msg_text)) in messageDict.items():
        if("System Notification" not in msg_author)\
                and (" created group " not in msg_author)\
                and (" joined using this group's invite link" not in msg_author)\
                and ("now an admin" not in msg_author):
            if msg_author in authorDict:
                authorDict[msg_author] += 1
            else:
                authorDict[msg_author] = 1

    for x in authorDict:
        print(str(x) + '\t' + str(authorDict[x]))

def calculate_messages_per_day(messageDict):
    dailyFreqDict = {}

    for key, ((msg_date, msg_time), (msg_author, msg_text)) in messageDict.items():
        if msg_date in dailyFreqDict:
            dailyFreqDict[msg_date] += 1
        else:
            dailyFreqDict[msg_date] = 1

    for x in dailyFreqDict:
        print(x, dailyFreqDict[x])

def calculate_messages_per_time(messageDict):
    timeFreqDict = {}

    for key, ((msg_date, msg_time), (msg_author, msg_text)) in messageDict.items():
        time = msg_time.split(":")

        #by changing the time key, you can change how things are grouped in the dictionary

        #group by hour
        time_key = time[0]

        #group by minute
        #time_key = time[0] + ':' + time[1]

        #group by second
        #time_key = time[0] + ':' + time[1] + ':' + time[2]

        if time_key in timeFreqDict:
            timeFreqDict[time_key] += 1
        else:
            timeFreqDict[time_key] = 1

    for x in timeFreqDict:
        print(str(x) + '\t' + str(timeFreqDict[x]))

def calculate_word_frequencies(messageDict):
    wordDict = {}

    for key, ((msg_date, msg_time), (msg_author, msg_text)) in messageDict.items():
        message_split = msg_text.split(" ")

        for word in message_split:
            if ('.jpg' not in word) and ('.mp4' not in word) and ("https:" not in word) and ("http:" not in word):
                cleaned_word = re.sub('[^A-Za-z0-9(\.)\#]+', '', word).lower()

                if (numberRegex.match(cleaned_word) == None):
                    if cleaned_word in wordDict:
                        wordDict[cleaned_word] += 1
                    else:
                        wordDict[cleaned_word] = 1

    for x in wordDict:
        print(x + "\t" + str(wordDict[x]))

def calculate_single_word_frequency(messageDict, searchWord):
    wordDict = {}

    for key, ((msg_date, msg_time), (msg_author, msg_text)) in messageDict.items():
        #wordDict should be made up of two keys, one on time and another on word. From there the behavior of the word will keep tally of its usage.

        key_time = msg_date
        #key_time = (msg_date, msg_time)

        message_split = msg_text.split(" ")

        for word in message_split:
            if ('.jpg' not in word) and ('.mp4' not in word) and ("https:" not in word) and ("http:" not in word):
                cleaned_word = re.sub('[^A-Za-z0-9(\.)\#]+', '', word).lower()

                if (searchWord in cleaned_word):
                    key = (cleaned_word, key_time)

                    if (numberRegex.match(cleaned_word) == None):
                        if key in wordDict:
                            wordDict[key] += 1
                        else:
                            wordDict[key] = 1

    for (word_key, time_key) in wordDict:
        print(str(word_key) + "\t" + str(time_key) + "\t" + str(wordDict[(word_key, time_key)]))

def calculate_char_frequencies(messageDict):
    charDict = {}

    for key, ((msg_date, msg_time), (msg_author, msg_text)) in messageDict.items():
        for character in msg_text:
            if character in charDict:
                charDict[character] += 1
            else:
                charDict[character] = 1

    for x in charDict:
        print(x + '\t' + str(charDict[x]))

def calculate_user_daily_frequencies(userName, messageDict):
    dailyFreqDict = {}

    for key, ((msg_date, msg_time), (msg_author, msg_text)) in messageDict.items():
        if msg_author == userName:
            if msg_date in dailyFreqDict:
                dailyFreqDict[msg_date] += 1
            else:
                dailyFreqDict[msg_date] = 1

    for x in dailyFreqDict:
        print(x + "\t" + str(dailyFreqDict[x]))

def calculate_user_time_frequencies(userName, messageDict):
    timeFreqDict = {}

    for key, ((msg_date, msg_time), (msg_author, msg_text)) in messageDict.items():
        if(userName == msg_author):
            timestamp_split = msg_time.split(":")

            #by changing the time key, you can change how things are grouped in the dictionary

            #group by hour
            time_key = timestamp_split[0]

            #group by minute
            #ime_key = timestamp_split[0] + ':' + timestamp_split[1]

            #group by second
            #time_key = timestamp_split[0] + ':' + timestamp_split[1] + ':' + timestamp_split[2]

            if time_key in timeFreqDict:
                timeFreqDict[time_key] += 1
            else:
                timeFreqDict[time_key] = 1

    for x in timeFreqDict:
        print(x + "\t" + str(timeFreqDict[x]))

def calculate_user_word_frequencies(userName, messageDict):
    wordDict = {}

    numberRegex = re.compile("^\d+$")

    for key, ((msg_date, msg_time), (msg_author, msg_text)) in messageDict.items():
        if(userName == msg_author):
            message_split = msg_text.split(" ")

            for word in message_split:
                if ('.jpg' not in word) and ('.mp4' not in word) and ("http" not in word) and ("http" not in word):
                    cleaned_word = re.sub('[^A-Za-z0-9\#]+', '', word).lower()

                    if (numberRegex.match(cleaned_word) == None):
                        if cleaned_word in wordDict:
                            wordDict[cleaned_word] += 1
                        else:
                            wordDict[cleaned_word] = 1

    for x in wordDict:
        print(x + "\t" + str(wordDict[x]))

