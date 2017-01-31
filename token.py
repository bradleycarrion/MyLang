class Token(object):
    def __init__(self, tokentype, lexeme, line, column):
        self.tokentype = tokentype
        self.lexeme = lexeme
        self.line = line
        self.column = column

    def __str__(self):
        output = str(self.tokentype) + " '"
        output += str(self.lexeme) + "' "
        output += str(self.line) + ":" + str(self.column)
        return output
