steps = 0
x = input()
y = input()
dist = y-x
if dist%2 != 0:
    dist -= 1
    steps += 1
aux = 0
i = 1
while True:
    aux += i*(i+1)
    steps += 1
    if aux == dist:
        print steps, i
        break
    i += 1