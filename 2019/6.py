import collections

Orbit = collections.namedtuple('orbit', 'parent child')


orbits = []
with open('6.dat') as f:
    for parent, child in map(lambda x: x.strip().split(')'), f.readlines()):
        orbits.append(Orbit(parent, child))

def get_children(parent, collection):
    children = list(filter(lambda x: x.parent == parent, orbits))
    total_children = {}
    if not children:
        return {}
    else:
        for child in children:
            total_children.update({child.child: get_children(child.child, orbits)})
    return total_children

def path_to_com(item, map):
    path = []
    if item in map.keys():
        path.append(item)
    else:
        for key, value in map.items():
            path = path + path_to_com(item, value)
            if path:
                path.insert(0, key)
                break
    return path


orbit_map = {}

current = ['COM']
x = 0
orbit_map = {'COM': get_children('COM', orbits)}

san = path_to_com('SAN', orbit_map)
you = path_to_com('YOU', orbit_map)

common = 'COM'
for i in reversed(san):
    if i in you:
        common = i
        break

san_length = len(san[san.index(common):]) -2
you_length = len(you[you.index(common):]) -2

print('Distance: ', san_length + you_length)


count = 0
level = 1
values = orbit_map.values()
while values:
    new_map = {}
    for i in values:
        count += level * len(i.keys())
        new_map.update(i) 
    orbit_map = new_map
    values = orbit_map.values()
    level += 1
print(count)
