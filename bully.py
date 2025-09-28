class Bully:
    st = []
    prio = []
    co = 0
    n = int(input("Enter number of elements: "))

    def getval(self):
        for i in range(0, self.n):
            print("Enter Status of the system", i + 1, "(1 for active, 0 for inactive):")
            self.st.append(int(input()))
            print("Enter Priority of the system:")
            self.prio.append(int(input()))

    def elect(self, ele):
        ele = ele - 1
        self.co = ele + 1
        for i in range(0, self.n):
            if self.prio[ele] < self.prio[i]:
                print("Election message is sent from", (ele + 1), "to", (i + 1))
                if self.st[i] == 1:
                    self.elect(i + 1)
        return self.co

    def startelect(self):
        ele = int(input("Which process will initiate election? "))
        print("Final coordinator is", self.elect(ele))


# Creating object and running methods
obj = Bully()
obj.getval()
obj.startelect()
