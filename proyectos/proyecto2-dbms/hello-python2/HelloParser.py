# Generated from .\Hello.g4 by ANTLR 4.7.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
from antlr4.error.ErrorListener import ErrorListener
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\5\b\4\2\t\2\3\2\3\2\3\2\3\2\2\2\3\2\2\2\2\6\2\4\3\2")
        buf.write(u"\2\2\4\5\7\3\2\2\5\6\7\4\2\2\6\3\3\2\2\2\2")
        return buf.getvalue()

class ParserException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class ParserExceptionErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ParserException("line " + str(line) + ":" + str(column) + " " + msg)

class HelloParser (Parser):
    grammarFileName = "Hello.g4"
    atn = ATNDeserializer().deserialize(serializedATN())
    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]
    sharedContextCache = PredictionContextCache()
    literalNames = [ u"<INVALID>", u"'hello'" ]
    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"ID", u"WS" ]
    RULE_r = 0
    ruleNames =  [ u"r" ]
    EOF = Token.EOF
    T__0=1
    ID=2
    WS=3

    def __init__(self, input, output=sys.stdout):
        super(HelloParser, self).__init__(input, output=output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

        self.removeErrorListeners()
        self.addErrorListener(ParserExceptionErrorListener())

    class RContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(HelloParser.RContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HelloParser.ID, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_r

        def enterRule(self, listener):
            if hasattr(listener, "enterR"):
                listener.enterR(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitR"):
                listener.exitR(self)

    def r(self):
        localctx = HelloParser.RContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_r)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(HelloParser.T__0)
            self.state = 3
            self.match(HelloParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
