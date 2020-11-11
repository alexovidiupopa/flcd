from fa import FiniteAutomata

class Console:

    def __readFA(self):
        self.fa = FiniteAutomata.readFromFile('FA.in')

    def __displayAll(self):
        print(self.fa)

    def __displayStates(self):
        print(self.fa.Q)

    def __displayAlphabet(self):
        print(self.fa.E)

    def __displayTransitions(self):
        print(self.fa.S)

    def __displayFinalStates(self):
        print(self.fa.F)

    def __checkDFA(self):
        print(self.fa.isDfa())

    def __checkAccepted(self):
        seq = input()
        print(self.fa.isAccepted(seq))

    def __displayMenu(self):
        print("1.Read FA from file")
        print("2.Display FA")
        print("3.Display FA States")
        print("4.Display FA Alphabet")
        print("5.Display FA transitions")
        print("6.Display FA final states")
        print("7.Check DFA")
        print("8.Check accepted sequence")

    def run(self):
        cmds = {'1':self.__readFA,'2':self.__displayAll,'3':self.__displayStates,'4':self.__displayAlphabet,
                '5':self.__displayTransitions, '6':self.__displayFinalStates, '7':self.__checkDFA,
                '8':self.__checkAccepted}
        exit = False
        while not exit:
            self.__displayMenu()
            print(">>")
            cmd = input()
            if cmd in cmds.keys():
                cmds[cmd]()
            elif cmd=="exit":
                exit = True
            else:
                continue
