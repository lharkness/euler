MAX_VALUE = 1000
global total = 0
for i = 1 : MAX_VALUE
    if (i % 3 == 0 || i % 5 == 0)
        global total += i
    end
end
println(total)