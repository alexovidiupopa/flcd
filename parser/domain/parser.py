from copy import deepcopy


class Parser:

    def __init__(self, grammar):
        self.grammar = grammar
        self.firstSet = {i: set() for i in self.grammar.N}
        self.followSet = {i: set() for i in self.grammar.N}
        self.table = {}
        self.generateFirst()
        self.generateFollow()
        self.generateTable()

    def innerLoop(self, initialSet, items, additionalSet):
        copySet = initialSet
        for i in range(len(items)):
            if self.grammar.isNonTerminal(items[i]):
                copySet = copySet.union(entry for entry in self.firstSet[items[i]] if entry != 'E')
                if 'E' in self.firstSet[items[i]]:
                    if i < len(items) - 1:
                        continue
                    copySet = copySet.union(additionalSet)
                    break
                else:
                    break
            else:
                copySet = copySet.union({items[i]})
                break

        return copySet

    def generateFirst(self):
        isSetChanged = False
        for key, value in self.grammar.P.items():
            for v in value:
                v = self.grammar.splitRhs(v[0])
                copySet = self.firstSet[key]
                copySet = copySet.union(self.innerLoop(copySet, v, ['E']))

                if len(self.firstSet[key]) != len(copySet):
                    self.firstSet[key] = copySet
                    isSetChanged = True

        while isSetChanged:
            isSetChanged = False
            for key, value in self.grammar.P.items():
                for v in value:
                    v = self.grammar.splitRhs(v[0])
                    copySet = self.firstSet[key]
                    copySet = copySet.union(self.innerLoop(copySet, v, ['E']))

                    if len(self.firstSet[key]) != len(copySet):
                        self.firstSet[key] = copySet
                        isSetChanged = True

    def generateFollow(self):
        self.followSet[self.grammar.S].add('E')
        isSetChanged = False
        for key, value in self.grammar.P.items():
            for v in value:
                v = self.grammar.splitRhs(v[0])
                for i in range(len(v)):
                    if not self.grammar.isNonTerminal(v[i]):
                        continue
                    copySet = self.followSet[v[i]]
                    if i < len(v) - 1:
                        copySet = copySet.union(self.innerLoop(copySet, v[i + 1:], self.followSet[key]))
                    else:
                        copySet = copySet.union(self.followSet[key])

                    if len(self.followSet[v[i]]) != len(copySet):
                        self.followSet[v[i]] = copySet
                        isSetChanged = True
        while isSetChanged:
            isSetChanged = False
            for key, value in self.grammar.P.items():
                for v in value:
                    v = self.grammar.splitRhs(v[0])
                    for i in range(len(v)):
                        if not self.grammar.isNonTerminal(v[i]):
                            continue
                        copySet = self.followSet[v[i]]
                        if i < len(v) - 1:
                            copySet = copySet.union(self.innerLoop(copySet, v[i + 1:], self.followSet[key]))
                        else:
                            copySet = copySet.union(self.followSet[key])

                        if len(self.followSet[v[i]]) != len(copySet):
                            self.followSet[v[i]] = copySet
                            isSetChanged = True

    def generateTable(self):
        nonterminals = self.grammar.N
        terminals = self.grammar.E

        for key, value in self.grammar.P.items():
            # value = (rhs, count)
            rowSymbol = key
            for v in value:
                rule = self.grammar.splitRhs(v[0])
                index = v[1]
                for columnSymbol in terminals + ['E']:
                    pair = (rowSymbol, columnSymbol)
                    if rule[0] == columnSymbol and columnSymbol != 'E':
                        self.table[pair] = v
                    elif rule[0] in nonterminals and columnSymbol in self.firstSet[rule[0]]:
                        if pair not in self.table.keys():
                            self.table[pair] = v
                        else:
                            print(pair)
                            print("Grammar is not LL(1).")
                            assert False
                    else:
                        if rule[0] == 'E':
                            for b in self.followSet[rowSymbol]:
                                if b == 'E':
                                    b = '$'
                                self.table[(rowSymbol, b)] = v
                        else:
                            firsts = set()
                            for symbol in self.grammar.P[rowSymbol]:
                                if symbol in nonterminals:
                                    firsts = firsts.union(self.firstSet[symbol])
                            if 'E' in firsts:
                                for b in self.firstSet[rowSymbol]:
                                    if b == 'E':
                                        b = '$'
                                    if (rowSymbol, b) not in self.table.keys():
                                        self.table[(rowSymbol, b)] = v
        for t in terminals:
            self.table[(t, t)] = ('pop', -1)
        self.table[('$', '$')] = ('acc', -1)

    def evaluateSequence(self, sequence):
        w = self.grammar.splitRhs(sequence)
        stack = [self.grammar.S, '$']
        output = ""
        while stack[0] != '$' and w:
            print(w, stack)
            if w[0] == stack[0]:
                w = w[1:]
                stack.pop(0)
            else:
                x = w[0]
                a = stack[0]
                if (a, x) not in self.table.keys():
                    return None
                else:
                    stack.pop(0)
                    rhs, index = self.table[(a, x)]
                    rhs = self.grammar.splitRhs(rhs)
                    for i in range(len(rhs) - 1, -1, -1):
                        if rhs[i]!='E':
                            stack.insert(0, rhs[i])
                    output += str(index)
            print(output)
        if stack[0] == '$':
            return None
        elif not w:
            while stack[0] != '$':
                a = stack[0]
                if (a, '$') in self.table.keys():
                    output += str(self.table[(a, '$')][1])
                stack.pop(0)
            return output
