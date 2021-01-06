# regular expressions cheatsheet

## library needed
```code
import re
```
## methods
```code
re.search(regex, sentence)
# returns the first occurance of the regex expression
re.match(regex, sentence)
# tells us if the sentence has the regex expression at the starting of the string
re.findal( regex, sentence)
# finds all ooccurances
re.sub(initial,final, sentence)
# returns the sentence after replceing all things that meet the initial regex wth the final string
```

## cheat sheet
<b>type 1</b>
'.' is for any one character besides he newline character

<b>type 2</b>

'*' matches any string that contains 0 or more occurrences of the character that occurred right before it. example, 'ab\*' matches a,ab,abbbb, and abbbbbbbbbbb

'+' does the same thing as * but for 1 or more occurrences

'?' does the same as * but for 0 or 1 occurrences

<b>greedy</b>
if you try to match ab* with abbbbbb, it will match with abbbbbb, say  you want it to match with a, then you use ab*?

if you used 'ab+?', then you get ab

if you use 'ab??' then you get a

<b>type 3</b>

{n}

ab{3} will look for abbb

ezpz

for range, 

{n,m}

can be made non-greedy

<b>type 4</b>

'^'
whatever you put after this, should be at the starting of the string, if it is to be matched

 '$' , whatever is before this, should be in the ending of the string, if it is to be matched

<b>type 5</b>

Now we look at character sets.

'[abc]' will match with a string if it has a,b, or c 

'[a-z] for any character from a to z

'[0-9]' for any character from 0 to 9

'[A-Z] for any character from A to Z

'[A-Za-z] for any character from a to z or A to Z

putting a ^ at the starting in the character set acts like a complement, i.e. [^abc] will match with a string not containing a or b or c

to know if a string contains "?" the re is "/?"

