#don't do this
from time import time

document = '''Finally, we wish to comment on several approaches for composing large strings. As
an academic exercise, assume that we have a large string named document, and our
goal is to produce a new string, letters, that contains only the alphabetic characters
of the original string (e.g., with spaces, numbers, and punctuation removed). It may
be tempting to compose a result through repeated concatenation, as follows
Constructing that new string
would require time proportional to its length. If the final result has n characters, the
series of concatenations would take time proportional to the familiar sum 1+ 2+
3+···+n, and therefore O(n2) time.
The experiments of Code Fragment 5.1 and 5.2, at the beginning of Section 5.3,
provide empirical evidence that Python’s list class is using a form of dynamic arrays
for its storage. Yet, a careful examination of the intermediate array capacities (see
Exercises R-5.2 and C-5.13) suggests that Python is not using a pure geometric
progression, nor is it using an arithmetic progression.
With that said, it is clear that Python’s implementation of the append method
exhibits amortized constant-time behavior. We can demonstrate this fact experimentally. A single append operation typically executes so quickly that it would be
difficult for us to accurately measure the time elapsed at that granularity, although
we should notice some of the more expensive operations in which a resize is performed. We can get a more accurate measure of the amortized cost per operation
by performing a series of n append operations on an initially empty list and determining the average cost of each. A function to perform that experiment is given in
Code Fragment 5.4.'''

document = document*100
letters = ''

start = time( )
for c in document:
    if c.isalpha():
        letters += c

end = time( )

process_time = end-start
print(process_time)

start = time( )
temp = []
for c in document:
    if c.isalpha():
        temp.append(c)

letters = ''.join(temp)

end = time( )

process_time = end-start
print(process_time)

#We can further improve the performance by using list comprehension
start = time( )
letters = ''.join([c for c in document if c.isalpha()])
end = time( )

process_time = end-start
print(process_time)

#We can further improve the performance by using generator comprehension
#By using the generator we use less memory but the takes longer
start = time( )
letters = ''.join(c for c in document if c.isalpha())
end = time( )

process_time = end-start
print(process_time)
