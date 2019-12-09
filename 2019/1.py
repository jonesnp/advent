

count = 0

def fuel_req(module):
    return (int(module) // 3) - 2

with open('1.dat') as f:
    for module in f.readlines():
        count += fuel_req(module)

print(count)

total_fuel = 0

with open('1.dat') as f:
    for module in f.readlines():
        add_fuel = fuel_req(module)
        while(add_fuel > 0):
            total_fuel += add_fuel
            add_fuel = fuel_req(add_fuel)
        count += total_fuel

print(total_fuel)