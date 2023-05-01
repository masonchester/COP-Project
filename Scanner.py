#element class is used to hold the token and the lexeme in 1 object.
class element:
    def __init__(self, token,lexeme,position):
        self.token = token
        self.lexeme = lexeme
        self.position = position

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
    else:
        return -1
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
def lex(nextString,the_position):
    while the_position < len(nextString):
        identity = getChar(nextString[the_position])
        #if the next character is a letter then we to parse through and build the lexeme. 
        if identity == 'LETTER':
            temp = ''
            while(the_position < len(nextString) and getChar(nextString[the_position]) != 'SPACE' and getChar(nextString[the_position]) != 'UNKNOWN'):
                if getChar(nextString[the_position]) == 'LETTER' or getChar(nextString[the_position]) == 'DIGIT':
                    temp += nextString[the_position]
                the_position += 1
            #when we are done we will declare it as an IDENT type meaning that it is an identifier.
            e1 = element('IDENT',temp,the_position)
            return e1
        # if the identity is of type DIGIT then we need to capture all the components of the number and put them into one lexeme. 
        elif identity == 'DIGIT':
           temp = ''
           while(the_position < len(nextString) and getChar(nextString[the_position]) != 'SPACE'):
                if(getChar(nextString[the_position]) == 'DIGIT'):
                    temp += nextString[the_position]
                the_position += 1
           e1 = element('INT_LIT', temp,the_position)
           return e1
        # if the character is of type unknown then we look it up in the lookup table to determine its token and lexeme.
        elif identity == 'UNKNOWN':
            nextToken = lookup(nextString[the_position])
            temp_position = the_position + 1
            e1 = element(str(nextToken),nextString[the_position],temp_position)
            return e1
        the_position += 1

#We declare some variables that we can use in the method.

the_position = 0
#we open the file and store every line to a list called the_text
the_file = open('C:/ConceptsProject/COP-Project/Example.txt','r')
#we read the file so we can 
the_text = the_file.read()
#scan through and keep the position of where we are in the file.
while the_position < len(the_text):
    #lex returns an object with the token and lexeme.
    result = lex(the_text,the_position)
    #we update position each time so the next call is not at the wrong position.
    the_position = result.position
    #if result.token is -1 we know its not a character we want.
    if result.token != '-1':
        print('next token is: ' + str(result.token) + " Next Lexeme is: " + str(result.lexeme))













