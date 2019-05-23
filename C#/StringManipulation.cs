using System;
using System.Text;

namespace StringManipulation
{
	class Program
	{
		static void Main(string[] args)
		{
			//BasicStringFunctionality();
			//StringConcatenation();
			//StringEquality();
			//StringEqualitySpecifyingCompareRules();
			//FunWithStringBuilder();
			StringInterpolation();
		}


		static void StringConcatenation()
		{
			Console.WriteLine("=> String Concatenation");
			string s1 = "Programming the ";
			string s2 = "Something";
			string s3 = s1 + s2;
			Console.WriteLine(s3);
		}

		static void BasicStringFunctionality()
		{
			ConsoleColor prevColor = Console.BackgroundColor;
			ConsoleColor prevFColor = Console.ForegroundColor;

			Console.BackgroundColor = ConsoleColor.DarkCyan;
			Console.ForegroundColor = ConsoleColor.White;
			Console.WriteLine("=> Basic String functionality:");
			Console.BackgroundColor = prevColor;
			Console.ForegroundColor = prevFColor;
			string firstName = "Freddy";
			Console.WriteLine("Value of firstName: {0}", firstName);
			Console.WriteLine("firstName has {0} characters.", firstName.Length);
			Console.WriteLine("firstName in uppercase: {0}", firstName.ToUpper());
			Console.WriteLine("firstName in lowercase: {0}", firstName.ToLower());
			Console.WriteLine("firstName contains the letter y?: {0}",
			firstName.Contains("y"));
			Console.WriteLine("firstName after replace: {0}", firstName.Replace("dy", ""));
			Console.WriteLine();
			Console.ReadLine();
		}
		static void StringEquality()
		{
			Console.WriteLine("=> String equality:");
			string s1 = "Hello!";
			string s2 = "Yo!";
			Console.WriteLine("s1 = {0}", s1);
			Console.WriteLine("s2 = {0}", s2);
			Console.WriteLine();
			// Test these strings for equality.
			Console.WriteLine("s1 == s2: {0}", s1 == s2);
			Console.WriteLine("s1 == Hello!: {0}", s1 == "Hello!");
			Console.WriteLine("s1 == HELLO!: {0}", s1 == "HELLO!");
			Console.WriteLine("s1 == hello!: {0}", s1 == "hello!");
			Console.WriteLine("s1.Equals(s2): {0}", s1.Equals(s2));
			Console.WriteLine("Yo.Equals(s2): {0}", "Yo!".Equals(s2));
			Console.WriteLine();
		}
		static void StringEqualitySpecifyingCompareRules()
		{
			Console.WriteLine("=> String equality (Case Insensitive:");
			string s1 = "Hello!";
			string s2 = "HELLO!";
			Console.WriteLine("s1 = {0}", s1);
			Console.WriteLine("s2 = {0}", s2);
			Console.WriteLine();

			// Check the results of changing the default compare rules.
			Console.WriteLine("Default rules: s1={0},s2={1}s1.Equals(s2): {2}", s1, s2,
							 s1.Equals(s2));
			Console.WriteLine("Ignore case: s1.Equals(s2, StringComparison.OrdinalIgnoreCase): {0}",
							s1.Equals(s2, StringComparison.OrdinalIgnoreCase));
			Console.WriteLine("Ignore case, Invarariant Culture: s1.Equals(s2, StringComparison.InvariantCultureIgnoreCase): { 0}",
							s1.Equals(
								s2,
								StringComparison.InvariantCultureIgnoreCase));
			Console.WriteLine();
			Console.WriteLine("Default rules: s1={0},s2={1} s1.IndexOf(\"E\"): {2}", s1, s2,
								 s1.IndexOf("E"));
			Console.WriteLine("Ignore case: s1.IndexOf(\"E\", StringComparison.OrdinalIgnoreCase):{ 0}",
				s1.IndexOf("E", StringComparison.OrdinalIgnoreCase));
			Console.WriteLine("Ignore case, Invarariant Culture: s1.IndexOf(\"E\", StringComparison.InvariantCultureIgnoreCase): { 0}",
								s1.IndexOf("E", StringComparison.InvariantCultureIgnoreCase));
			Console.WriteLine();
		}

		static void FunWithStringBuilder()
		{
			Console.WriteLine("=> Using the StringBuilder:");
			StringBuilder sb = new StringBuilder("**** Fantastic Games ****");
			sb.Append("\n");
			sb.AppendLine("Half Life");
			sb.AppendLine("Morrowind");
			sb.AppendLine("Deus Ex" + "2");
			sb.AppendLine("System Shock ");
			Console.WriteLine(sb.ToString());
			sb.Replace("2", " Invisible War");
			Console.WriteLine(sb.ToString());
			Console.WriteLine("sb has {0} chars.", sb.Length);
			Console.WriteLine();
			Console.ReadLine();
		}
		static void StringInterpolation()
		{
			// Some local variables we will plug into our larger string
			int age = 4;
			string name = "Soren";
			// Using curly bracket syntax.
			string greeting = string.Format("Hello {0} you are {1} years old.", name, age);
			// Using string interpolation
			string greeting2 = $"\tHello {name} you are {age += 4} years old.";
			Console.WriteLine(greeting2);
		}
	}
}
