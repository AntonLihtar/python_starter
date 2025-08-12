bob1 = dict(job='dev', age=40, name='Bob')
print(bob1)

value = bob1.get('x', 'x not')
value2 = bob1['x'] if 'x' in bob1 else 5
# print(value)
# print(value2)
ob = [
    {'a': 2, 'b': 'e'},
    {'a': 1, 'b': 'd'},
    {'a': 3, 'b': 'a'},
]

print(sorted(ob, key=lambda x: x['a']))
