def convert(test):
    moth = {
        '.-' : 'a',
        '-...' : 'b',
        '-.-.' : 'c',
        '-..' : 'd',
        "." : 'e',
        '..-.' : 'f',
        '--.' : 'g',
        '....' : 'h',
        '..' : 'i',
        '.---' : 'j',
        '-.-' : 'k',
        '.-..' : 'l',
        '--' : 'm',
        '-.' : 'n',
        '---' : 'o',
        '.--.' : 'p',
        '--.-' : 'q',
        '.-.' : 'r',
        '...' : 's',
        '-' : 't',
        '..-' : 'u',
        '...-' : 'v',
        '.--' : 'w',
        '-..-' : 'x',
        '-.--' : 'y',
        '--..' : 'z'
    }
    """
    temp = ""
    result = ""
    cnt = 0
    for s in test:
        if s == " " and cnt == 0:
            result += moth[temp]
            temp = ""
            cnt += 1
        elif s == " " and cnt == 1:
            result += " "
        else:
            temp += s
            cnt = 0
    result += moth[temp]
    print result
    """

    result = []
    for words in test.split("  "):
        for word in words.split(" "):
            result.append(moth[word])
        result.append(" ")

    print "".join(result)

test = ".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"

convert(test)
