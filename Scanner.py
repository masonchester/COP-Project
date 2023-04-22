#element class is used to hold the token and the lexeme in 1 object.
class element:
    def __init__(self, token,lexeme):
        self.token = token
        self.lexeme = lexeme

#lookup is used to check for arithmetic operators, and other statement operators.
def lookup(the_character):
    if the_character == '+':
        next_token = 20
    elif the_character == '-':
       next_token = 21
    elif the_character == '*':
        next_token = 22
    elif the_character == '/':
        next_token = 23
    elif the_character == '(':
        next_token = 24
    elif the_character == ')':
        next_token = 25
    elif the_character == '=':
        next_token = 26
    elif the_character == ':':
        next_token = 27
    elif the_character == '"':
        next_token = 28
    elif the_character == ',':
        next_token = 29
    elif 'EOF':
        next_token = -1
    else:
        return -1;
    return next_token
#getChar is used to identify what class the next character is.
def getChar(nextChar):
    if nextChar.isalpha():
         return 'LETTER'
    elif nextChar.isdigit():
        return 'DIGIT'
    elif nextChar == ' ':
        return 'SPACE'
    #if it is unknown then we will look it up in the table. 
    else:
        return 'UNKNOWN'
#lex is the main part of the scanner. It uses the other methods to help generate the next token and next lexeme. 
def lex(nextString):
    x = 0
    nextString = nextString.strip()
    while x < len(nextString):
        identity = getChar(nextString[x])
        #if the next character is a letter then we to parse through and build the lexeme. 
        if identity == 'LETTER':
            temp = ''
            temp2 = ''
            while(x < len(nextString) and getChar(nextString[x]) != 'SPACE'):
                if getChar(nextString[x]) == 'LETTER' or getChar(nextString[x]) == 'DIGIT':
                    temp += nextString[x]
                elif lookup(nextString[x]) != -1:
                    temp2 += nextString[x]
                    break
                x += 1
            #when we are done we will declare it as an IDENT type meaning that it is an identifier.
            e1 = element('IDENT',temp)
            element_list.append(e1)
            #the next if statement is for the situation where we have a trailing character like a ) or :.
            if (temp2 != ''):
                #we can capture this element instead of loosing it with this logic. 
                nextToken = lookup(temp2)
                e1 = element(str(nextToken), temp2)
                element_list.append(e1)
        # if the identity is of type DIGIT then we need to capture all the components of the number and put them into one lexeme. 
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
           #again the next if statement is for the situation where we have a trailing character like a ) or :.
           if(temp2 != ''):
               nextToken = lookup(temp2)
               e1 = element(str(nextToken), temp2)
               element_list.append(e1)
        # if the character is of type unknown then we look it up in the lookup table to determine its token and lexeme.
        elif identity == 'UNKNOWN':
            nextToken = lookup(nextString[x])
            e1 = element(str(nextToken),nextString[x])
            element_list.append(e1)
        x += 1

#We declare some variables that we can use in the method.
charClass = 0
lexeme = []
token_list = []
element_list = []
token = 0
next_token = 0
#we open the file and store every line to a list called the_text
the_file = open('C:/ConceptsProject/COP-Project/Example.txt','r')
the_text = the_file.readlines()
#now we can iterate through the list with a for loop calling lex on each element in the list.
for c in the_text:
    lex(c)
#now we can print tokens and the lexemes as needed. 
for c in element_list:
    print("Next token is: " + str(c.token) + " Next Lexeme is: " + str(c.lexeme))









