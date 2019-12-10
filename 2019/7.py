from itertools import permutations
from collections import deque

program = []

with open('7.dat') as f:
    program = list(map(int, f.readline().split(',')))

class Intcode:
    def __init__(self, program):
        self.program = program + [0,0,0]
        self.pointer = 0
        self.has_halted = False

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
        self.has_halted = True
        #print(self.program[0])

    def run(self, ins, outs):
        output = ''
        while True:
            self.read()
            if self.opcode == '01':
                self.add()
                self.inc(4)
            elif self.opcode == '02':
                self.mul()
                self.inc(4)
            elif self.opcode == '03':
                self.program[self.params[0]] = ins.popleft()
                self.inc(2)
            elif self.opcode == '04':
                outs.append(self.program[self.params[0]])
                self.inc(2)
                return
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
                return output

# phase_values = [0,1,2,3,4]

# maximum = 0
# for p1,p2,p3,p4,p5 in permutations(phase_values):
#     a = deque()
#     A = Intcode(program).run(deque([p1,0]), a)
#     b = deque()
#     a.appendleft(p2)
#     B = Intcode(program).run(a , b)
#     c = deque()
#     b.appendleft(p3)
#     C = Intcode(program).run(b, c)
#     d = deque()
#     c.appendleft(p4)
#     D = Intcode(program).run(c, d)
#     e = deque()
#     d.appendleft(p5)
#     E = Intcode(program).run(d, e)
#     final = e.pop()
#     if final > maximum:
#         maximum = final
# print(maximum)

phase_values = [9,8,7,6,5]
maximum = 0
for p1,p2,p3,p4,p5 in permutations(phase_values):
    A = Intcode(program)
    B = Intcode(program)
    C = Intcode(program)
    D = Intcode(program)
    E = Intcode(program)
    a = deque([p1, 0])
    b = deque([p2])
    c = deque([p3])
    d = deque([p4])
    e = deque([p5])

    while not E.has_halted:
        A.run(a, b)
        B.run(b, c)
        C.run(c, d)
        D.run(d, e)
        E.run(e, a)
    final = a.pop()
    if final > maximum:
        maximum = final
print(maximum)
