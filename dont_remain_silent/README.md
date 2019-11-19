### A tale about algorithm complexity

Once upon a time on a normal day I attended to a job interview where
I was presented the following problem:

> Write a function whose input consist of a stream of characters. The
  function should return the first non-repeating character. 

E.g:

```python
In [1]: fn("GeeksForGeeks")
Out[1]: "F"

In [1]: fn("GGGGGGGGGG")
Out[1]: None

In [1]: fn("1234567890")
Out[1]: "1"
```

I was given pen and some paper to complete it. Needless to day, under
those circumstances, and interviewee would focus of achieving an "it
works above all things" implementation to show both problem solving
capacity in a reasonable time as well as some degree of algorithm
complexity knowledge by skipping library usage.

So, I run through it and made a function like the following:

```python
def fn(payload: str) -> str:
	ocurrences = {}
	for char in payload:
		if char in ocurrences:
			ocurrences[char] += 1
		else:
			ocurrences[char] = 1
	for char in payload:
		if ocurrences[char] == 1:
			return char
	return ""
```

It just works. Yeah, there is a for loop to iterate over the whole 
payload *again*. I was pretty aware of that issue. So much, that in
fact I verbally stated to the interviewer that I could have made it
in `O(n + 1)` by employing a double-ended-linked list instead of the actual
`O(n + n)` (which still performs well as both `n + 1` and `n + n` are 
within `O(n)` complexity).

Just after that statement, I spotted some kind of surprise in the
interviewer's face. "I have him/her in my pocket", I thought. However,
the response I expected was much different:

> Why would you need a double-ended-linked list? The algorithm could have
  just been better performant by adding a simple list into play.
  
"Well" - I thought. "As a hashmap capable of storing and deleting
stuff, specially for the deleting feature, some pointer to previous
elements are expected so as to reorder list nodes". 

From there on, and let's say, for the sake of the rest of the
interview, I chose to remain quiet, just nodding and hearing to his/her
explanation of the best implementation, which I bet it was like:

```python
def fn(payload: str) -> str:
	ocurrences = {}
	unique_chars = [] # <-- Introduce a list
	for char in payload:
		if char in ocurrences:
			ocurrences[char] += 1
		else:
			ocurrences[char] = 1
			unique_chars.append(char)  # <-- Append unique chars only
	for char in unique_chars:
		if ocurrences[char] == 1:
			return char
	return ""
```

Which drops the complexity from `O(n + n)` to `O(n + k)`, being `k`
lower or equals than `n`.

The thing is, that hearing from a senior with such self-confidence
that no double-ended-list like structure was ever needed, left me
wondering whether I was right or not. I guess I was, demostration
included along this readme. By reading it, you might probably say
that "Oh hell, so much code for such a ridiculus task". The "just add
a list" implementation is far more readable and easy to understand. To
which I respond: "Well, getting the best performance out of things does
not have to", although I agree with the readability is a major point
I take into account when either submitting PRs or handling code reviews.
