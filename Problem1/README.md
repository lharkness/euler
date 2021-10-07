This problem asks us to determine whether a given number is a multiple of 3 or 5.  To distill the results of this problem down to a single answer we are asked to sum up all such numbers in a range (strictly below 1000)

The brute force method for this question is to simply implement the algorithm as stated:

```
for each i in the range
    if i is a multiple of 3 or 5
        add i to the total
```

There's not a lot of room for optimizations here.  My optimization toolbox is pretty limited:

1. Try not to look at the entire search space
2. Try not to repeat steps

For (1) two ideas come to mind.  The first saves almost no time - you can start at 3.  But what if you just count to generate, rather than look at every number?

```
for i = 3; i < MAX_VALUE; i = i + 3 
    total = total + i

for i = 5: i < MAX_VALUE; i = i + 5
    if i is not a multiple of 3 {
        total = total + i

```

the first algorithm will spin through the entire range, performing an if for each element and a sum for each hit.  The second algorithm will consider 1/3 of the range, performing a sum for each element, and then consider 1/5 of the range, performing an if for each element and a sum for each element that is not a multiple of 3.

Numbers in the range that are multiples of both 3 and 5 are considered twice, which seems wasteful.  Instead of summing we could add them to a set and that would de-duplicate, but that seems less efficient but let's look at it:

```
for i = 3; i < MAX_VALUE; i = i + 3 
    numberSet.add(i)

for i = 5: i < MAX_VALUE; i = i + 5
    if i is not a multiple of 3 {
        numberSet.add(i)

total = sumOf(numberSet)
```

Here we are spinning through 1/3 & 1/5 the range, which seems optimal except we are considering multiples of 3 and 5 twice.  For each one we are adding this to a set, which is O(n).  Then we are spinning through all the numbers and adding them to a total, which seems optimal.

I bet there's some math trick to eliminate considering the multiples of 3 and 5 twice.  Let's look at the numbers we want:

3 5 6 9 10 12 15 18 20 21 24 25 27 30

First-order differences give us:

2 1 3 1 2 3 3 2 1 3 1 2 3

Nothing is jumping out at me, but we could keep going.  Let's write some code to investigate.  This code will look like:

```
for i in range
    if i is multiple of 3 or 5
        add i to a list

for i less than list size - 2 increment by 2
    add list[i + 1] - list[i] to another list

output list
output another list
```

Perhaps that will give us a clue for a pattern.

And indeed it does.  The first 88 first order differences are:

[2, 1, 3, 1, 2, 3, 3, 2, 1, 3, 1, 2, 3, 3, 2, 1, 3, 1, 2, 3, 3, 2, 1, 3, 1, 2, 3, 3, 2, 1, 3, 1, 2, 3, 3, 2, 1, 3, 1]

which is just 2,1,3,1,2,3,3 repeating.

So the code to generate the sum would look like this:

```
differences = [2,1,3,1,2,3,3]
number = 3
total = 0
index = -1
MAX_VALUE = 1000

while number < MAX_VALUE:
    total = total + number
    index = (index + 1) % len(differences)
    number = number + differences[index]

print(total)
```

This code does three sums and a mod operation per number in the range.  This seems better.

I do wonder why 2,1,3,1,2,3,3 though.

Looking at space complexity I like this approach better as well.  The brute force algorithm uses constant space, that middle thing uses a couple sets, so we get to O(n).  The last one uses a small array, so back to O(1).

Another way to look at this problem is through the functional lens.  Rather than iterate over some numbers and calculate a total what if we defined a function that we could stream numbers into?  Something like:

```
range -> filter(i : i mod 3 == 0 || i mod 5 == 0) -> sum
```

or perhaps a recursive function such as

```
ThreeOrFive (x, total) ->
    if x >= MAX_VALUE
        return total
    else if (x mod 3 == 0 || x mod 5 == 0)
        return ThreeOrFive(x + 1, total + x)
    else
        return ThreeOrFive(x + 1, total)
```


It wouldn't surprise me if there were a way to directly calculate it from MAX_VALUE

And thanks to Chris Mueller, I see that there is.

Chris posts:

> Deduce the following identity:
> 1+2+...+n = (n/2)(n+1)

> From which it follows that:
> 
> (the above question for numbers less than 10)
> 3(1+2+3) + 5(1) = 23
> 
> (less than 100)
> 3(1+2+...+33) + 5(1+2+...+19)
> 
> (less than 1000)
> 3(1+2+...+333) + 5(1+2+...+199) = 3 (333/2)(334) + 5(199/2)(200) = 266,333
