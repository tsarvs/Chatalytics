import re

def calculate_messages_per_author(messageDict):
    authorDict = {}

    for key, ((msg_date, msg_time),(msg_author, msg_text)) in messageDict.items():
        if msg_author in authorDict:
            authorDict[msg_author] += 1
        else:
            authorDict[msg_author] = 1

    for x in authorDict:
        print(x, authorDict[x])

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
        timestamp_split = msg_time.split(" ")

        time = timestamp_split[0].split(":")

        #by changing the time key, you can change how things are grouped in the dictionary

        #group by hour
        #time_key = time[0] + timestamp_split[1]

        #group by minute
        time_key = time[0] + ':' + time[1] + ' ' + timestamp_split[1]

        #group by second
        #time_key = time[0] + ':' + time[1] + ':' + time[2] + ' ' + timestamp_split[1]

        if time_key in timeFreqDict:
            timeFreqDict[time_key] += 1
        else:
            timeFreqDict[time_key] = 1

    for x in timeFreqDict:
        print(x, timeFreqDict[x])

def calculate_word_frequencies(messageDict):
    wordDict = {}

    numberRegex = re.compile("^\d+$")

    for key, ((msg_date, msg_time), (msg_author, msg_text)) in messageDict.items():
        message_split = msg_text.split(" ")

        for word in message_split:
            if ('.jpg' not in word) and ('.mp4' not in word) and ("http:" not in word) and ("http:" not in word):
                cleaned_word = re.sub('[^A-Za-z0-9\#]+', '', word).lower()

                if (numberRegex.match(cleaned_word) == None):
                    if cleaned_word in wordDict:
                        wordDict[cleaned_word] += 1
                    else:
                        wordDict[cleaned_word] = 1

    for x in wordDict:
        print(x + "\t" + str(wordDict[x]))

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
            timestamp_split = msg_time.split(" ")

            time = timestamp_split[0].split(":")

            #by changing the time key, you can change how things are grouped in the dictionary

            #group by hour
            time_key = time[0] + timestamp_split[1]

            #group by minute
            #ime_key = time[0] + ':' + time[1] + ' ' + timestamp_split[1]

            #group by second
            #time_key = time[0] + ':' + time[1] + ':' + time[2] + ' ' + timestamp_split[1]

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
