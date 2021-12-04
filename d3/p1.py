with open("input1.txt") as f:
    data = [ x.strip() for x in f.readlines()]

values = [0 for _ in range(len(data[0]))]
for row in data:
    for idx,element in enumerate(row):
        values[idx]=values[idx]+int(element)
gamma_build = ''
epsilon_build = ''
for element in values:
    value = 1 if element > len(data)/2 else 0
    gamma_build+=str(value)

    value = 1 if element < len(data)/2 else 0
    epsilon_build+=str(value)
gamma = int(gamma_build, 2)
epsilon = int(epsilon_build, 2)

print(gamma, epsilon, gamma * epsilon)
