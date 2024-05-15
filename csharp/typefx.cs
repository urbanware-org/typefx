/// <summary>
/// Print the input text "machine like" with a static delay (in milliseconds)
/// </summary>
public static void TypeFxStatic(string text, int delay)
{
	if (text == String.Empty)
	{
		throw new ArgumentException("Text must not be empty");
	}

	if (delay <= 0)
	{
		throw new ArgumentException("Delay must be greater than 0");
	}

	foreach (char c in text)
	{
		Console.Write(c);
		System.Threading.Thread.Sleep(delay);
	}
}

/// <summary>
/// Print the input text "typewriter like" with a dynamic delay (in milliseconds)
/// </summary>
public static void TypeFxDynamic(string text, int delay_min, int delay_max)
{
	if (text == String.Empty)
	{
		throw new ArgumentException("Text must not be empty");
	}

	if (delay_min <= 0)
	{
		throw new ArgumentException("Minimum delay must be greater than 0");
	}

	if (delay_max <= delay_min)
	{
		throw new ArgumentException(
			$"Maximum delay (got {delay_max}) must be greater than the minimum delay (got {delay_min})"
		);
	}

	Random random = new Random();
	foreach (char c in text)
	{
		int delay = random.Next(delay_min, delay_max);
		Console.Write(c);
		System.Threading.Thread.Sleep(delay);
	}
}
