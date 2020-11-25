from domain.grammar import Grammar
from domain.parser import Parser
from domain.tree import Tree


class UI:

    def __init__(self):
        self.grammar = None
        self.parser = None

    def run(self):
        while True:
            print(">>")
            cmd = input()
            if cmd == "1":
                self.readGrammar()
            elif cmd == "2":
                self.printNonTerminals()
            elif cmd == "3":
                self.printTerminals()
            elif cmd == "4":
                self.printProductions()
            elif cmd == "5":
                self.printProductionsForNonTerminal()
            elif cmd == "6":
                self.printParser()
            elif cmd == "7":
                self.evaluateSequence()

    def readGrammar(self):
        self.grammar = Grammar.fromFile('g1.txt')
        print("Read grammar")

    def printNonTerminals(self):
        print(self.grammar.N)

    def printTerminals(self):
        print(self.grammar.E)

    def printProductions(self):
        print(self.grammar.P)

    def printProductionsForNonTerminal(self):
        print(">>Nonterminal:")
        nonterm = input()
        print(self.grammar.getProductionsFor(nonterm))

    def printParser(self):
        self.parser = Parser(self.grammar)
        print(self.parser.firstSet)
        print(self.parser.followSet)
        for k in self.parser.table.keys():
            print(k, '->', self.parser.table[k])

    def evaluateSequence(self):
        result = self.parser.evaluateSequence("(i)+i")
        if result is None:
            print("Sequence not accepted")
        else:
            print(result)
        t = Tree(self.grammar)
        t.build(result)
        t.print_table()
