from itertools import permutations
from collections import deque

program = []

with open('9.dat') as f:
    program = dict(enumerate(list(map(int, f.readline().split(',')))))

class Intcode:
    def __init__(self, program):
        self.program = program
        self.pointer = 0
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

    def run(self):
        while not self.has_halted:
            self.read()
            if self.opcode == '01':
                self.add()
                self.inc(4)
            elif self.opcode == '02':
                self.mul()
                self.inc(4)
            elif self.opcode == '03':
                self.program[self.params[0]] = int(input('Input: '))
                self.inc(2)
            elif self.opcode == '04':
                print(self.get(self.params[0]), end=' ')
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
            elif self.opcode == '09':
                self.adjust_base()
                self.inc(2)
            elif self.opcode == '99':
                self.halt()


#A = Intcode(dict(enumerate([109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99])))
A = Intcode(program)


A.run()