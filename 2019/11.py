import time


with open('11.dat') as f:
    program = dict(enumerate(list(map(int, f.readline().split(',')))))

class Intcode:
    def __init__(self, program):
        self.program = program
        self.pointer = 0
        self.blocked_for_input = False
        self.has_halted = False
        self.relative_base = 0;

    def inc(self, amt):
        self.pointer += amt

    def read(self):
        instruction = str(self.program[self.pointer]).zfill(5)
        self.opcode = instruction[-2:]
        self.param_modes = list(reversed(list(map(int, instruction[:-2]))))
        self.params = [0,0,0]
        for i in range(1, 4):
            if self.param_modes[i-1] == 0:
                self.params[i-1] = self.get(self.pointer + i)
            elif self.param_modes[i-1] == 1 :
                self.params[i-1] = self.pointer + i
            elif self.param_modes[i-1] == 2:
                self.params[i-1] = self.get(self.pointer + i) + self.relative_base 

    def add(self):
        self.program[self.params[2]] = self.get(self.params[0]) + self.get(self.params[1])

    def mul(self):
        self.program[self.params[2]] = self.get(self.params[0]) * self.get(self.params[1])
    
    def get(self, ref):
        if ref not in self.program:
            self.program[ref] = 0
        return self.program[ref]

    def jumpiftrue(self):
        if self.get(self.params[0]) != 0:
            self.pointer = self.get(self.params[1])
        else:
            self.inc(3)

    def jumpiffalse(self):
        if self.get(self.params[0]) == 0:
            self.pointer = self.get(self.params[1])
        else:
            self.inc(3)

    def lt(self):
        if self.get(self.params[0]) < self.get(self.params[1]):
            self.program[self.params[2]] = 1
        else:
            self.program[self.params[2]] = 0

    def eq(self):
        if self.get(self.params[0]) == self.get(self.params[1]):
            self.program[self.params[2]] = 1
        else:
            self.program[self.params[2]] = 0
        
    def adjust_base(self):
        self.relative_base += self.get(self.params[0])

    def halt(self):
        self.has_halted = True

    def run(self, param = None):
        self.blocked_for_input = False
        while not self.has_halted:
            self.read()
            if self.opcode == '01':
                self.add()
                self.inc(4)
            elif self.opcode == '02':
                self.mul()
                self.inc(4)
            elif self.opcode == '03':
                if param != None:
                    self.program[self.params[0]] = param
                    param = None
                    self.inc(2)
                else:
                    self.blocked_for_input = True
                    return
            elif self.opcode == '04':
                print(self.params[0])
                output = self.get(self.params[0])
                self.inc(2)
                return output
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
            elif self.opcode == '09':
                self.adjust_base()
                self.inc(2)
            elif self.opcode == '99':
                self.halt()


A = Intcode(program)

param = 0
while not A.has_halted:
    print(A.run(param))
    if A.blocked_for_input:
        param = 1