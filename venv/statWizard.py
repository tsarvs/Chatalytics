def calculate_timestamp_frequency_days(timestampDict):
    if(len(timestampDict) <= 0):
        return

    for key in timestampDict:
        #print(str(key) + "," + str(timestampDict[key]))
        print(str(timestampDict[key]))