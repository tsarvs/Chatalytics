import re

timestampRegex = re.compile("^\[(\d){1,2}\/(\d){1,2}\/(\d){2,4}\,\s(\d){1,2}\:(\d){2}\:(\d){2}\s(P|A)M\](.)*$")#regex for checking if theres a timestamp at the beginning of a string
messageDict = {}

def parse_timestamp(line):
    data = line.split(" ")

    timestamp = []

    message_date = data[0][1:-1]
    message_time = data[1] + ' ' + data[2].replace(']', ' ')

    timestamp = [message_date, message_time]

    return timestamp

def parse_message(line):
    data = line.split(" ")

    message = []

    author = data[3]

    textMessage = ""

    i = 4
    while((':' not in author) and (i < len(data))):
        concatString = " " + data[i]
        author += concatString
        i+=1

    author = author.replace(':', '')

    #if true then the message parse is a line where someone changed the header
    if ("changed the subject to " in author)\
            or ("changed this group's icon" in author)\
            or (" left" in author)\
            or (" was added" in author)\
            or (" removed" in author)\
            or (" added " in author)\
            or (" changed the group description" in author)\
            or (" deleted " in author)\
            or ("Beefachunga!" in author):
        textMessage = author
        author = 'System Notification'
    else:
        while(i < len(data)):
            textMessage += data[i] + " "
            i+=1

        textMessage = textMessage[:-1]

    message = [author, textMessage]

    return message


def parse_line(messageNumber, line):
    #split up line into data types
    timestamp = parse_timestamp(line)

    textMessage = parse_message(line)

    #add to data structures
    messageDict[messageNumber] = [timestamp, textMessage]

def parse_file(file):
    i = 0

    for line in file:
        if (timestampRegex.match(line)):
            print("Message:", i)
            parse_line(i, line)
            i += 1
        else:
            messageDict.get(i-1)[1][1] += line