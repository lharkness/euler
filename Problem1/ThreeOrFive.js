MAX_VALUE = 1000
total = 0
for (i = 1; i < MAX_VALUE; i++) {
    if (i % 3 == 0 || i % 5 == 0) {
        total += i
    }
}
print(total)