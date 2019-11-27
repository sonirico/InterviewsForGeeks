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

It just works. And yeah, there is a for loop to iterate over the whole
payload *again*. I was pretty aware of that issue. So much, that in
fact I verbally stated to the interviewer that I could have made it
in `O(n + 1)` by employing a double-ended-linked list instead of the
actual `O(n + n)`, which still performs well as both `n + 1` and `n + n`
are still within `O(n)` complexity.

Anyway, just after that statement, I spotted some kind of surprise in the
interviewer's face. "I have him/her in my pocket", I thought. However,
the response I expected was much different:

> Why would you need a double-ended-linked list? The algorithm could have
  just been better performant by adding a simple list into play. There is
  no need por two pointers at all.

"Well" - I thought. "This problem quite resembles a MRU cache. In the moment
an element or a character has appeared again, it should go out completetly".
That implies implementing the remove operation on the _ddl_, so both _next_
and _previous_ pointers must exist so as not raise complexity to O(n) again,
as linked lists with only a pointer to the next item would require iteration to
find the last element pointing to the currently-being-deleted node in order to
perform deletion and then re-linkage.

From there on, and let's say, for the sake of the rest of the
interview, I chose to remain quiet. Just to hide the frustation of being
unable to fully explain my idea. So I was just nodding and hearing to his/her
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
    for char in unique_chars:  # <-- Iterate only over non-repeated chars
        if ocurrences[char] == 1:
            return char
    return ""
```

Which drops the complexity from `O(n + n)` to `O(n + k)`, being `k`
lower than `n`, or equals in the worst case scenario.

The thing is, that hearing from a senior with such self-confidence
that no double-ended-list like structure was ever needed, left me
wondering whether I was right or not. As soon as I got home, I implemented
my solution successfully, which you can find along this readme. I have not
benchmarked it yet, but my intuition says that would work better for larger
payloads, at least in regards to memory footprint.

By reading my solution, you might probably say that "Oh hell, so much code
for such a ridiculus task". The "just add a list" implementation is far more
readable and easy to understand. To which I respond: "Well, getting the best
performance out of things does not have to", although I agree with the
readability is a major point I take into account when either submitting
PRs or handling code reviews.
