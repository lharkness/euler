
raw_numbers = []
differences = []

for i in range(88):
    if (i % 3 == 0 or i % 5 == 0) and i != 0:
        raw_numbers.append(i)

for i in range(0, len(raw_numbers) - 2):
    differences.append(raw_numbers[i + 1] - raw_numbers[i])

print(raw_numbers)
print(differences)
