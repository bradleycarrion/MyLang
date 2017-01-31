#!/usr/bin/python2
# -*- coding: utf-8 -*-
import sys
from lexer import Lexer
from error import Error
import tokentypes

class Program(object):

    def __init__(self, filename):
        self.filename = filename
        self.tokens = self.__tokenize()

    def __tokenize(self):
        # empty list to contain token items
        tokens = []

        try:
            # attempt to open the source code for reading
            file_stream = open(self.filename, "r")

            the_lexer = Lexer(file_stream)
            curr_token = the_lexer.next_token()

            # get next token until EOS token appears
            while curr_token.tokentype != tokentypes.EOS:
                tokens.append(curr_token)
                curr_token = the_lexer.next_token()
        except IOError as e:
            print "error: unable to open file '" + filename + "’"
            sys.exit(1)
        except Error as e:
            print e
            sys.exit(1)

        return tokens

    def print_tokens(self):
        output = "# THE TOKENS IN '" + str(self.filename) + "' ARE: \n"
        for i in xrange(len(self.tokens)):
            output += str(self.tokens[i]) + "\n"

        #output += str(self.tokens[-1]) + "\n"

        print output
