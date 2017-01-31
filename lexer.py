from token import Token
from error import Error
import tokentypes

class Lexer(object):

    def __init__(self, input_stream):
        self.line = 1
        self.column = 0
        self.input_stream = input_stream

    def __peek(self):
        pos = self.input_stream.tell()
        symbol = self.input_stream.read(1)
        self.input_stream.seek(pos)
        return symbol

    def __read(self):
        return self.input_stream.read(1)

    def next_token(self):
        symbol = self.__read()
        self.column += 1

        # first check if EOS
        if (self.__peek() == ""):
            token = Token(tokentypes.EOS, "", self.line, self.column)


        while symbol.isspace():
            symbol = self.__read()
            self.column += 1

        # get single characters
        if (symbol == ";"):
            token = Token(tokentypes.SEMICOLON, symbol, self.line, self.column)
            self.line += 1
        elif (symbol == "+"):
            token = Token(tokentypes.PLUS, symbol, self.line, self.column)
        elif (symbol == "-"):
            token = Token(tokentypes.MINUS, symbol, self.line, self.column)
        elif (symbol == "*"):
            token = Token(tokentypes.MULTIPLY, symbol, self.line, self.column)
        elif (symbol == "/"):
            token = Token(tokentypes.DIVIDE, symbol, self.line, self.column)
        elif (symbol == "("):
            token = Token(tokentypes.LPAREN, symbol, self.line, self.column)
        elif (symbol == ")"):
            token = Token(tokentypes.RPAREN, symbol, self.line, self.column)

        elif (symbol == ">"):   # get comparators
            if (self.__peek() != "="):
                token = Token(tokentypes.GREATER_THAN, symbol, self.line, self.column)
            else:
                token = Token(tokentypes.GREATER_THAN_EQUAL, ">=", self.line, self.column)
                self.__read()
                self.column += 1
        elif (symbol == "<"):
            if (self.__peek() != "="):
                token = Token(tokentypes.LESS_THAN, symbol, self.line, self.column)
            else:
                token = Token(tokentypes.LESS_THAN_EQUAL, "<=", self.line, self.column)
                self.__read()
                self.column += 1
        elif (symbol == "="):
            if (self.__peek() != "="):
                token = Token(tokentypes.ASSIGN, symbol, self.line, self.column)
            else:
                token = Token(tokentypes.EQUAL, "==", self.line, self.column)
                self.__read()
                self.column += 1
        elif (symbol == "!"):
            if (self.__peek() != "="):
                token = Token(tokentypes.NOT, symbol, self.line, self.column)
            else:
                token = Token(tokentypes.NOT_EQUAL, "!=", self.line, self.column)
                self.__read()
                self.column += 1

        elif (symbol.isalpha()):    # get identifiers
            cstring = symbol
            go = True
            while go:
                if (self.__peek().isalpha() or self.__peek().isdigit()):
                    symbol = self.__read()
                    cstring += symbol
                    self.column += 1
                else:
                    go = False

            # check reserved words
            if (cstring == "and"):
                token = Token(tokentypes.AND, cstring, self.line, self.column)
            elif (cstring == "or"):
                token = Token(tokentypes.OR, cstring, self.line, self.column)
            elif (cstring == "while"):
                token = Token(tokentypes.WHILE, cstring, self.line, self.column)
            elif (cstring == "do"):
                token = Token(tokentypes.DO, cstring, self.line, self.column)
            elif (cstring == "then"):
                token = Token(tokentypes.THEN, cstring, self.line, self.column)
            elif (cstring == "end"):
                token = Token(tokentypes.END, cstring, self.line, self.column)
            elif (cstring == "print"):
                token = Token(tokentypes.PRINT, cstring, self.line, self.column)
            elif (cstring == "println"):
                token = Token(tokentypes.PRINTLN, cstring, self.line, self.column)
            elif (cstring == "true"):
                token = Token(tokentypes.TRUE, cstring, self.line, self.column)
            elif (cstring == "false"):
                token = Token(tokentypes.FALSE, cstring, self.line, self.column)
            elif (cstring == "if"):
                token = Token(tokentypes.IF, cstring, self.line, self.column)
            elif (cstring == "else"):
                token = Token(tokentypes.ELSE, cstring, self.line, self.column)
            elif (cstring == "elseif"):
                token = Token(tokentypes.ELSEIF, cstring, self.line, self.column)
            else:
                token = Token(tokentypes.ID, cstring, self.line, self.column)

        elif (symbol == '"'): # get string type
            cstring = ""
            symbol = self.__read()
            self.column += 1

            while (symbol != '"'):
                cstring += symbol
                symbol = self.__read()
                self.column += 1
            token = Token(tokentypes.STRING, cstring, self.line, self.column)

        elif (symbol.isalpha()): # get number type
            number = symbol
            has_decimal = False
            while (self.__peek().isdigit()):
                symbol = self.__read()
                number += symbol
                self.column += 1
            token = Token(tokentypes.INT, number, self.line, self.column)

        else:
            token = Token(tokentypes.EOS, "", self.line, self.column)

        return token
