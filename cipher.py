# Shift a letter by the designated amount, regardless of case
def shiftLetter(c,shift):
    code = ord(c)
    pad = ord(shift)-65
    if (code>=65) and (code<=90):
        code = (code-pad-39)%26+65
    elif (code>=97) and (code<=122):
        code = (code-pad-71)%26+97
    return chr(code)

# Shift all characters in a message by the designated amount, regardless of case
def shiftMessage(message,shift):
    seq = list(message)
    pad = list(shift)
    padcounter = 0
    for i in range(0,len(message)):
        if seq[i].isalpha():
            seq[i] = shiftLetter(seq[i],pad[padcounter])
            padcounter += 1
    return "".join(seq)

# Shift all characters by 3 places right
def encipher(message):
    return shiftMessage(message, pad2)


# Shift all characters by 3 places left
def decipher(message):
    return shiftMessage(message,pad2)

# Open pad file and read
pad = open("pad.txt", "r")
pad2 = pad.read()

# Open quotation file and read
msg = open("cquote.txt", "r")
msg2 = msg.read()

# Open deciphered.txt file and save results
file2 = open("deciphered.txt", "w")
file2.write(encipher(msg2))
file2.close()
