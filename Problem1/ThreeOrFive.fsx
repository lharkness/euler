open System
let MAX_VALUE = 999
let f = fun n -> (n % 3 = 0 || n % 5 = 0)
let s = seq {1 .. MAX_VALUE} |> Seq.filter f
Console.WriteLine("The sum is {0}", Seq.sum s)