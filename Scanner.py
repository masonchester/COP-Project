the_position = 0
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
def lex(nextString):
    global the_position
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
           while(the_position < len(nextString) and getChar(nextString[the_position]) != 'SPACE' and getChar(nextString[the_position]) != 'UNKNOWN'):
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
#get next token is used by the parser to call lex and get the next part of the statement.
def get_next_token(the_text,move_position):
#we use the global position variable so anytime the get_next_token method is called it automatically keeps track of our
# position in the file. 
    global the_position
    # if the length of the text is equal to the positon we are done and will hit the else statement.
    if len(the_text) != the_position:
        #otherwise we check if move position is false this essentilly allows us to peek the next token without updating the position variable.
        if move_position == False:
            temp = the_position
            result = lex(the_text)
            the_position = the_position = temp
            return result
        #if move position is true then we will update the position and return the resulting element that contains the token and lexeme
        result = lex(the_text)
        the_position = result.position
        return result
    #when the else statement is hit we return an element with EOF for both attributes telling the parser there is nothing left to parse.
    else:
        result = element('EOF', 'EOF',the_position)
        return result







