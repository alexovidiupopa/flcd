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
            elif cmd == "8":
                self.evaluatePif()
            elif cmd == "9":
                self.evaluateG1()
            elif cmd == "10":
                self.evaluateG2()

    def readGrammar(self):
        self.grammar = Grammar.fromFile('g1.txt')
        print("Read grammar")

    def readG1(self):
        self.g1 = Grammar.fromFile('g1.txt')
        print('Read g1')

    def readG2(self):
        self.g2 = Grammar.fromFile('g2.txt')
        print('Read g2')

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

    def readSequence(self, fname):
        sequence=""
        with open(fname,'r') as fin:
            for line in fin.readlines():
                sequence+=line.strip() + " "
        return sequence.strip()

    def evaluateSequence(self):
        result = self.parser.evaluateSequence("int")
        if result is None:
            print("Sequence not accepted")
        else:
            print(result)
        t = Tree(self.grammar)
        t.build(result)
        t.print_table()

    def evaluatePif(self):
        seq = self.readSequence('pif.txt')
        result = self.parser.evaluateSequence(seq)
        if result is None:
            print("Sequence not accepted")
        else:
            print(result)
        t = Tree(self.grammar)
        t.build(result)
        t.print_table()

    def evaluateG1(self):
        self.readG1()
        self.p1 = Parser(self.g1)
        print(self.p1.firstSet)
        print(self.p1.followSet)
        for k in self.p1.table.keys():
            print(k, '->', self.p1.table[k])
        result = self.p1.evaluateSequence(self.readSequence('seq.txt'))
        if result is None:
            print("Sequence not accepted")
        else:
            print(result)
        t = Tree(self.g1)
        t.build(result)
        t.print_table()
        pass

    def evaluateG2(self):
        self.readG2()
        self.p2 = Parser(self.g2)
        print(self.p2.firstSet)
        print(self.p2.followSet)
        for k in self.p2.table.keys():
            print(k, '->', self.p2.table[k])
        result = self.p2.evaluateSequence(self.readSequence('pif.txt'))
        if result is None:
            print("Sequence not accepted")
        else:
            print(result)
            t = Tree(self.g2)
            t.build(result)
            t.print_table()
