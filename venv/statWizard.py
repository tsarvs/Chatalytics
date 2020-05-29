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
        print(x)

    for x in dailyFreqDict:
        print(dailyFreqDict[x])