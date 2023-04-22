#element class is used to hold the token and the lexeme in 1 object.
class element:
    def __init__(self, token,lexeme):
        self.token = token
        self.lexeme = lexeme

#lookup is used to check for arithmetic operators and
def lookup(the_character):
    if the_character == '(':
        nextToken = 25
    elif the_character == ')':
        nextToken = 26
    elif the_character == '+':
        nextToken = 21
    elif the_character == '-':
        nextToken = 22
    elif the_character == '*':
        nextToken = 23
    elif the_character == '/':
        nextToken = 24
    elif 'EOF':
        nextToken = -1
    else:
        return -1;
    return nextToken

def getChar(nextChar):
    if nextChar != 'EOF':
        if nextChar.isalpha():
            return 'LETTER'
        elif nextChar.isdigit():
            return 'DIGIT'
        elif nextChar == ' ':
            return 'SPACE'
        else:
            return 'UNKNOWN'
    else:
        return 'EOF'

def lex(nextString):
    x = 0
    while x < len(nextString):
        identity = getChar(nextString[x])
        if identity == 'LETTER':
            temp = ''
            temp2 = ''
            while(x < len(nextString) and getChar(nextString[x]) != 'SPACE'):
                if getChar(nextString[x]) == 'LETTER' or getChar(nextString[x]) == 'DIGIT':
                    temp += nextString[x]
                elif lookup(nextString[x]) != -1:
                    temp2 += nextString[x]
                x += 1
            e1 = element('IDENT',temp)
            element_list.append(e1)
            if (temp2 != ''):
                nextToken = lookup(temp2)
                e1 = element(str(nextToken), temp2)
                element_list.append(e1)
        elif identity == 'DIGIT':
           temp = ''
           temp2 = ''
           while(x < len(nextString) and getChar(nextString[x]) != 'SPACE'):
                if(getChar(nextString[x]) == 'DIGIT'):
                    temp += nextString[x]
                elif(lookup(nextString[x]) != -1):
                    temp2 += nextString[x]
                x += 1
           e1 = element('INT_LIT', temp)
           element_list.append(e1)
           if(temp2 != ''):
               nextToken = lookup(temp2)
               e1 = element(str(nextToken), temp2)
               element_list.append(e1)
        elif identity == 'UNKNOWN':
            nextToken = lookup(nextString[x])
            e1 = element(str(nextToken),nextString[x])
            element_list.append(e1)
        x += 1

#Main
charClass = 0
lexeme = []
token_list = []
element_list = []
token = 0
next_token = 0
#a1 = element('fake',0)
#element_list.append(a1)
line = "(sum + 47) / total"

lex(line)
for c in element_list:
    print("Next token is: " + str(c.token) + " Next Lexeme is " + str(c.lexeme))









