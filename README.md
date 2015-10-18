# TicketMasterExercise
Ticket Master Interview prep eexercise answers

1. Longest Collatz sequence
The following iterative sequence is defined for the set of positive integers:
  n => n/2 (n is even)
  n => 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
  13 40 20 10 5 16 8 4 2 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
proved yet (search for the “Collatz Problem” if you're interested), it is thought that all starting numbers finish
at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.

Answer: 837799 using the collatz.py script

2. grep - Files, Folders and Regex
Write a program that replicates the functionality of "grep -r". It should take a regex and one or more files or
folders as a parameter, then print every line that matches the regex in every file found, recursing into folders.
You can easily test your program by checking that
grep -r [Regex] [Files...]
produces the same output as
python yourprogram [Regex] [Files...]

Notes:
Error conditions should be handled gracefully, printing informative messages where appropriate.
Answer: pythongrep.py
