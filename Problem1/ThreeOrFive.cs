using System;

/*
 * Implements the brute force solution 
 *
 */
public class ThreeOrFive 
{
    private static int MAX_VALUE = 1000;

    static void Main(string[] args)
    {
        int total = 0;

        for (int i = 0; i < MAX_VALUE; i++) 
        {
            if (i % 3 == 0 || i % 5 == 0) 
            {
                total += i;
            }
        }

        Console.WriteLine(total);

    }   

}