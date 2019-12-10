
program = []

with open('5.dat') as f:
    program = list(map(int, f.readline().split(',')))

class Intcode:
    def __init__(self, program):
        self.program = program
        self.pointer = 0

    def inc(self, amt):
        self.pointer += amt

    def read(self):
        instruction = str(self.program[self.pointer]).zfill(5)
        self.opcode = instruction[-2:]
        self.param_modes = list(reversed(list(map(int, instruction[:-2]))))
        self.params = [0,0,0]
        for i in range(1, 4):
            self.params[i-1] = self.program[self.pointer + i] if self.param_modes[i-1] == 0 else self.pointer + i

    def add(self):
        self.program[self.params[2]] = self.program[self.params[0]] + self.program[self.params[1]]

    def mul(self):
        self.program[self.params[2]] = self.program[self.params[0]] * self.program[self.params[1]]

    def user_input(self):
        self.program[self.params[0]] = int(input('User Input: '))
    
    def output(self):
        print(self.program[self.params[0]])

    def jumpiftrue(self):
        if self.program[self.params[0]] != 0:
            self.pointer = self.program[self.params[1]]
        else:
            self.inc(3)

    def jumpiffalse(self):
        if self.program[self.params[0]] == 0:
            self.pointer = self.program[self.params[1]]
        else:
            self.inc(3)

    def lt(self):
        if self.program[self.params[0]] < self.program[self.params[1]]:
            self.program[self.params[2]] = 1
        else:
            self.program[self.params[2]] = 0

    def eq(self):
        if self.program[self.params[0]] == self.program[self.params[1]]:
            self.program[self.params[2]] = 1
        else:
            self.program[self.params[2]] = 0

    def halt(self):
        pass
        #print(self.program[0])

    def run(self):
        while True:
            self.read()
            if self.opcode == '01':
                self.add()
                self.inc(4)
            elif self.opcode == '02':
                self.mul()
                self.inc(4)
            elif self.opcode == '03':
                self.user_input()
                self.inc(2)
            elif self.opcode == '04':
                self.output()
                self.inc(2)
            elif self.opcode == '05':
                self.jumpiftrue()
            elif self.opcode == '06':
                self.jumpiffalse()
            elif self.opcode == '07':
                self.lt()
                self.inc(4)
            elif self.opcode == '08':
                self.eq()
                self.inc(4)
            elif self.opcode == '99':
                self.halt()
                break


Intcode(program + [0,0,0]).run()