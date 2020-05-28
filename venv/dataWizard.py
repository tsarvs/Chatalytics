def parse_line(line):
    firstCharacter = line[0]

    if(firstCharacter == '['):
        header = line[0:line.index(']')+1]
        parse_header(header)

def parse_header(header):
    print(header)

def parse_file(file):
    for line in file:
        parse_line(line)

