# 8.1
e2f = dict(dog='chien',cat='chat',walrus='morse')
print(e2f)

# 8.2
print(e2f['walrus'])

# 8.3
f2e = {v:k for k,v in e2f.items()}
print(f2e)

# 8.4
print(f2e.get('chien'))

# 8.5
print(e2f.keys())

# 8.6
life = dict(animals=dict(cats='Henri',octopi='Grumpy',emus='Lucy'),plants=dict(),other=dict())
print(life)

# 8.7
print(life.keys())

# 8.8
print(life['animals'].keys())

# 8.9
print(life['animals']['cats'])

# 8.10
squares = {i: i**2 for i in range(10)}
print(squares)