import re

timestampRegex = re.compile("^\[(\d){1,2}\/(\d){1,2}\/(\d){2,4}\,(.)*$")
timestampDict = {}

def parse_timestamp(line):
    data = line.split(" ")

    timestamp = []

    if(timestampRegex.match(data[0])):

        message_date = data[0][1:-1]
        message_time = [data[1], data[2].replace(']', ' ')]

        timestamp = [message_date, message_time]
    else:
        timestamp = ["Warning", "Not end of message"]

    return timestamp

#TODO: setup fxn
def parse_author(line):
    data = line.split(" ")

#TOSO: setup fxn
def parse_message(line):
    data = line.split(" ")

def add_timestamp_to_dict(timestamp):
    if (timestamp[0] not in ('Warning', None)):
        key = timestamp[0]

        if timestamp[0] in timestampDict:
            timestampDict[key] += 1
        else:
            timestampDict[key] = 1

def parse_line(line):
    #split up line into data types
    timestamp = parse_timestamp(line)

    #add to data structures
    add_timestamp_to_dict(timestamp)

def parse_file(file):
    i = 1

    for line in file:
        if (timestampRegex.match(line)):
            parse_line(line)
        else:
            i = i
