
let MAX_VALUE = 999
var total = 0 // var is mutable, let is immutable

for i in 1 ... MAX_VALUE {
    if (i % 3 == 0 || i % 5 == 0) {
        total += i
    }
}

print(total)
