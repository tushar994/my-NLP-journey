# Overview

## order to read in
- Phonetic hashing
- edit_distance
- spell-corrector

## Phonetic hashing
It is basically like a hash function for words.

It basically generates a code for all words that mean the same thing

One such algorithm is the soundex algorithm
It assigns a four letter code to each word, and words with the same code are considered the same.<br>
<br>
Then the first letter of the code is the first letter.<br>
The way it does this is is, first it removes all the letters that are vowels,h,y,or w.<br>
The rest of the consonents are mapped as follows<br>
b,f,p,v => 1<br>
c,g,j,,k,q,s,x,z => 2<br>
l => 3<br>
m,n => 4<br>
r => 5<br>

Then, we mergse all the consecutive numbers wihich are the same<br>
Then, to make it four letters, we either truncate it from the left or add zeros to the lef, or leave it<br>

for example <br>
Mississippi<br>
first letter of the code is M<br>
then, we remove the letter that are to be removed<br>
Msssspp<br>
then, we map<br>
M222211<br>
Then we join<br>
M21<br>
then we make it four digits<br>
M210<br>

## Edit distance
This is the minimum number of edits needed to go from one word to another, where valid edits are deletion, insertion, and replacement

We use a recursive algorithm for this

## spell corrector
What we will do is, we will check every possible word that can be made from the given word, with two operations, and then calculate the probability that it is that word, based on it's occurences frequency in the given text sample, and we will choose the word with the highest frequency