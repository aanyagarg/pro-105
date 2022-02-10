
data = [60,61,65,63,98,99,90,95,91,96]


n = len(data)
sum = 0

for i in data:
    sum = sum+i

mean = sum / n

new_data = []

for num in data:
    a = int(num) - mean
    a = a**2

    new_data.append(a)

sum2 = 0

for i in new_data:
    sum = sum + i

res = sum / (n-1)

std = math.sqrt(res)

print("Std Dev - " , std)