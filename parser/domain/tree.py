class Node:
    def __init__(self, value, child, rs):
        self.value = value
        self.child = child
        self.right_sibling = rs

    def __str__(self):
        return "({}, {}, {})".format(self.value, self.child, self.right_sibling)


class Tree:
    def __init__(self, grammar):
        self.root = None
        self.grammar = grammar
        self.crt = 1

    def build(self, ws):
        nonterminal, rhs = self.grammar.getProductionForIndex(int(ws[0]))
        self.root = Node(nonterminal, None, None)
        self.root.child = self._build_recursive(ws[1:], rhs)
        return self.root

    def _build_recursive(self, ws, rhs):
        if rhs == "" or ws == "":
            return None
        # ws = 1213....

        if rhs[0] in self.grammar.E:
            node = Node(rhs[0], None, None)
            node.right_sibling = self._build_recursive(ws, rhs[1:])
            print(node.value)
            return node
        elif rhs[0] in self.grammar.N:
            index = ws[0]
            nonterminal, cpy = self.grammar.getProductionForIndex(int(index))
            node = Node(rhs[0], None, None)
            node.child = self._build_recursive(ws[1:], cpy)
            node.right_sibling = self._build_recursive(ws, rhs[1:])
            print(node.value)
            return node
        else:
            print('E')
            return None

    def print_table(self):
        self._bfs(self.root)

    def _bfs(self, node, father_crt=None, left_sibling_crt=None):
        if node is None:
            return []
        print("{} | {} | {} | {}".format(self.crt, node.value, father_crt, left_sibling_crt))

        crt = self.crt
        self.crt += 1

        if left_sibling_crt is not None:
            return [[node.child, crt, None]] + self._bfs(node.right_sibling, father_crt, crt)
        else:
            children = [[node.child, crt, None]] + self._bfs(node.right_sibling, father_crt, crt)
            for child in children:
                self._bfs(*child)

    def __str__(self):
        string = ""
        node = self.root
        while node is not None:
            string += str(node)
            node = node.right_sibling
        return string
