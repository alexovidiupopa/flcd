class FiniteAutomata:

    def __init__(self, Q, E, q0, F, S):
        self.Q = Q
        self.E = E
        self.q0 = q0
        self.F = F
        self.S = S

    @staticmethod
    def getLine(line):
        # Only get what comes after the '='
        return line.strip().split(' ')[2:]

    @staticmethod
    def validate(Q, E, q0, F, S):
        pass

    @staticmethod
    def readFromFile(file_name):
        with open(file_name) as file:
            Q = FiniteAutomata.getLine(file.readline())
            E = FiniteAutomata.getLine(file.readline())
            q0 = FiniteAutomata.getLine(file.readline())[0]  # Only get the letter
            F = FiniteAutomata.getLine(file.readline())

            file.readline()  # S =

            # Get all transitions
            S = {}
            for line in file:
                src = line.strip().split('->')[0].strip().replace('(', '').replace(')', '').split(',')[0]
                route = line.strip().split('->')[0].strip().replace('(', '').replace(')', '').split(',')[1]
                dst = line.strip().split('->')[1].strip()

                if (src, route) in S.keys():
                    S[(src,route)].append(dst)
                else:
                    S[(src, route)] = [dst]

            return FiniteAutomata(Q, E, q0, F, S)

    def isDfa(self):
        for k in self.S.keys():
            if len(self.S[k])>1:
                return False
        return True

    def __str__(self):
        return "Q = { " + ', '.join(self.Q) + " }\n" \
                                              "E = { " + ', '.join(self.E) + " }\n" \
                                                                             "q0 = { " + self.q0 + " }\n" \
                                                                                                   "F = { " + ', '.join(
            self.F) + " }\n" \
                      "S = { " + str(self.S) + " } "
