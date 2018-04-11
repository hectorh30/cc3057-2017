import sys
from antlr4 import *
from HelloLexer import HelloLexer
from HelloParser import HelloParser
from HelloListener import HelloListener

# Este listener, que extiende a HelloListener, simplemente emite un mensaje cuando
# se visita la produccion R
class TestListener(HelloListener):
    def enterR(self, ctx):
        print('Entering R')

'''
Uso: python main.py example1.txt
'''
def main(argv):
    input = FileStream(argv[1])
    lexer = HelloLexer(input)
    stream = CommonTokenStream(lexer)
    parser = HelloParser(stream)

    # Note que 'r' se refiere a la produccion 'r' definida en la gramatica
    tree = parser.r()
    listener = TestListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main(sys.argv)
