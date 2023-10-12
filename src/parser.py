from Scanner import *
#parser class
class Parser():
    #constructor for parser
    def __init__(self, input_string):
        self.input_string = input_string
        self.current_token = get_next_token(self.input_string, True)
    #factor method for grammer
    def factor(self):
        token = self.current_token
        # check if the token is an integer or an identifier
        if token.token == 'INT_LIT':
            self.current_token = get_next_token(self.input_string, True)
            return int(token.lexeme)
        elif token.token == 'IDENT':
            self.current_token = get_next_token(self.input_string, True)
            return token.lexeme
        elif token.token == '24':
            self.current_token = get_next_token(self.input_string, True)
            results = self.expr()
            if self.current_token.token != '25':
                raise Exception('Missing closing parenthesis')
            self.current_token = get_next_token(self.input_string, True)
            return results
        else:
            raise Exception('Invalid factor')
    #term method for grammar
    def term(self):
        results = self.factor()
        while self.current_token.token in ['22', '23']:
            if self.current_token.token == '22':
                self.current_token = get_next_token(self.input_string, True)
                results *= self.factor()
            elif self.current_token.token == '23':
                self.current_token = get_next_token(self.input_string, True)
                results /= self.factor()
        return results
    #expr method for grammar
    def expr(self):
        results = self.term()

        while self.current_token.token in ['20', '21']:
            if self.current_token.token == '20':
                self.current_token = get_next_token(self.input_string, True)
                results += self.term()
            elif self.current_token.token == '21':
                self.current_token = get_next_token(self.input_string, True)
                results -= self.term()
        return results
    #assignment method for grammar
    def assignment(self):
        token = self.current_token
        if token.token != 'IDENT':
            raise Exception('Invalid assignment')
        variable = token.lexeme
        self.current_token = get_next_token(self.input_string, True)
        if self.current_token.token != '26':
            raise Exception('Missing equals sign in assignment')
        self.current_token = get_next_token(self.input_string, True)
        value = self.expr()
        return(variable,value)
    #statement method for grammar
    def statement(self):
        token = self.current_token
        if token.token == 'IDENT':
            return self.assignment()
        else:
            return self.expr()

    # parse method starts
    def parse(self):
        results = self.statement()
        the_variables.append(results)
        while self.current_token.lexeme == '\n' or self.current_token.lexeme != 'EOF':
            self.current_token = get_next_token(self.input_string, True)
            if self.current_token.token != 'EOF':
                results = self.statement()
                the_variables.append(results)
        # check if there are any tokens left
        if self.current_token.lexeme != 'EOF':
            raise Exception('Invalid syntax')
        return results
#run the parser 
the_file = open('C:\ConceptsProject\COP-Project\Example.txt')
the_text = the_file.read()
p = Parser(the_text)
the_variables = []
result = p.parse()
#print the results
for x in the_variables:
    print(x)