import re

#regex for checking if theres a timestamp at the beginning of a string
regexString_Timestamp = "^\[(\d){1,2}\/(\d){1,2}\/(\d){2,4}\,\s(\d){1,2}\:(\d){2}\:(\d){2}\]"
timestampRegex = re.compile(regexString_Timestamp)

regexString_CreatedGroup = "^(.)*created(\s)this(\s)group"
createdGroupRegex = re.compile(regexString_CreatedGroup)

messageAboutEncyption = "Messages and calls are end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read or listen to them."

messageDict = {}

def parse_timestamp(line):
    data = line.split(" ")

    timestamp = []

    message_date = data[0][1:-1]
    message_time = data[1][0:-1]

    timestamp = [message_date, message_time]

    return timestamp

def parse_createdGroupMessage():
    #TODO: split messages up by message type
    print()


def parse_message(line):
    #initialize local data
    author = ""
    textMessage = ""
    message = [author, textMessage]

    data = line.split(" ")

    #go through the split data and get the authors name
    i = 2
    while((':' not in author) and (i < len(data))):
        concatString = " " + data[i]
        author += concatString
        i+=1

    author = author[1:].replace(':', '')

    #if true then the message parse is a line where someone changed the header
    if (" changed the subject to " in author):
        textMessage = author
        author = 'System Notification - Changed Subject'
    elif ("changed this group's icon" in author):
        textMessage = author
        author = 'System Notification - Changed Icon'
    elif (" changed the group description" in author):
        textMessage = author
        author = 'System Notification - Changed Description'
    elif (" left" in author):
        textMessage = author
        author = 'System Notification - User Left'
    elif (" added" in author):
        textMessage = author
        author = 'System Notification - User Added'
    elif (" removed" in author):
        textMessage = author
        author = 'System Notification - User Removed'
    elif (" deleted" in author):
        textMessage = author
        author = 'System Notification - Message Deleted'
    elif (" created this group" in author):
        textMessage = author
        author = 'System Notification - Created Group'
    elif (messageAboutEncyption in line):
        textMessage = messageAboutEncyption
        author = 'System Notification - Encyption Message'
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
        #clean line of bad characters before evaluating the regex
        cleaned_line = str(line.encode('ascii', 'ignore'))[2:-3]

        if (timestampRegex.match(cleaned_line)):
            #print("Message:", i)
            parse_line(i, cleaned_line)
            i += 1
        else:
            messageDict.get(i-1)[1][1] += line
