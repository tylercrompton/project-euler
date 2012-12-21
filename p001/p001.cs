using System;

namespace p001
{
    public class Program
    {
        public static uint p001(uint max)
        {
            uint i = 0,
                total = 0;

            while (i < max)
            {
                if (i + 15 < max)
                    total += i * 7 + 60;
                else if (i + 12 < max)
                    total += i * 6 + 45;
                else if (i + 10 < max)
                    total += i * 5 + 33;
                else if (i + 9 < max)
                    total += i * 4 + 23;
                else if (i + 6 < max)
                    total += i * 3 + 14;
                else if (i + 5 < max)
                    total += i * 2 + 8;
                else if (i + 3 < max)
                    return total + i + 3;
                i += 15;
            }

            return total;
        }

        static void Main(string[] args)
        {
            if (args.Length == 1)
            {
                Console.WriteLine(p001(Convert.ToUInt32(args[0])));
            }
            else
            {
                Console.Error.WriteLine("Usage: p001 <integer>");
                Environment.Exit(1);
            }
        }
    }
}