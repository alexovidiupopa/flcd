

class Parser:

    def __init__(self, grammar):
        self.grammar = grammar
        self.firstSet = {}
        self.followSet = {}
        self.generateFirst()
        self.generateFollow()

    def generateFirst(self):
        for nonterminal in self.grammar.N:
            self.firstSet[nonterminal] = self.first(nonterminal)

    def generateFollow(self):
        pass

    def first(self, x):
        if x in self.firstSet.keys():
            return self.firstSet[x]
        result = set()
        terminals = self.grammar.E
        productions = self.grammar.getProductionsFor(x)
        for prod in productions:
            dest = prod[1]
            for d in dest:
                if d == 'E' or d in terminals:
                    result.add(d)
                else:
                    result.update(self.first(d))
        return result

    def follow(self, x, y):
        pass
