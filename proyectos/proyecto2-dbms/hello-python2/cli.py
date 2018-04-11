import sys
from antlr4 import *
from HelloLexer import HelloLexer, LexerException
from HelloParser import HelloParser, ParserException

def parse(text):
    lexer = HelloLexer(InputStream(text))
    stream = CommonTokenStream(lexer)
    parser = HelloParser(stream)
    tree = parser.r()

'''
Uso: python cli.py

De acuerdo con la gramática definida en Hello.g4, las únicas consturcciones válidas
son aquellas que inician con la palabra 'hello' y son seguidas por identificadores
en minúsculas o espacios en blanco. Cualquier otra construcción deberá levantar una
LexerException o ParserException.
'''
def main(argv):
    while True:
        try:
            text = raw_input("> ")

            if (text == 'exit'):
                sys.exit()

            parse(text);
            print "Valid"

        except LexerException as e:
            print "Got a lexer exception:", e.value

        except ParserException as e:
            print "Got a parser exception:", e.value

        except EOFError as e:
            print "Bye"
            sys.exit()

        except Exception as e:
            print "Got exception: ", e

if __name__ == '__main__':
    main(sys.argv)
