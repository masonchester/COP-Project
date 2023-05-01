from Scanner import *

class Parser():

    def __init__(self, input_string):
        self.input_string = input_string
        self.current_token = get_next_token(self.input_string, True)
    
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
    
    def statement(self):
        token = self.current_token
        if token.token == 'IDENT':
            return self.assignment()
        else:
            return self.expr()

    # parse the entire input string
    def parse(self):
        results = self.statement()

        # check if there are any tokens left
        if self.current_token.token != -1:
            raise Exception('Invalid syntax')

        return results

p = Parser('x = 3 * (4 + 5)')

result = p.parse()

print(result)