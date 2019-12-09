
with open('2.dat') as f:
    program = list(map(lambda x: int(x), f.read().split(',')))


def execute(program):
    pointer = 0
    while True: 
        if program[pointer] == 99:
            return program[0]
        elif program[pointer] == 1:
            program[program[pointer+3]] = program[program[pointer+1]] + program[program[pointer+2]]
        elif program[pointer] == 2:
            program[program[pointer+3]] = program[program[pointer+1]] * program[program[pointer+2]]
        pointer += 4

for x in range(0,100): 
    for y in range(0,100):
        test = program.copy()
        test[1] = x
        test[2] = y
        if execute(test) == 19690720:
            print(x,y)


