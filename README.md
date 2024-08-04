# text-blackout-generator

This is a project to make a script which takes a small amount of input text and generates some possibilities for blacking out text to say something new.

## Examples

One of my favorite examples of this is a Kung-Fu Panda meme which uses the line,

> Finally, a worthy opponent! Our battle will be legendary!

Which is edited by blacking out text and adding a caption: 

> When fish evolved to go on land:
> Fin_____ _ ______ _________ ___ ______ will be leg______!

## How it works

My current idea for the algorithm is that it will first strip any extra characters, just leaving lowercase letters. Then, from each point, it will use a list of dictionary words to check for possible completions from that point.

So it would pretty quickly find "Fin" as a possibility, but another one that I can see might be "F__all".

"Fin" is a slice from [0:2]
"Fall" is a slice from [0:5]

Both would be added to a list, which at the end of processing would procedurally go through the collection and string together random phrases.

At the very least, there would have to be 1 character of padding after each word, or else it would be very difficult to read.

### Detailed Steps:
1. **Preprocessing**: Strip extra characters, leaving only lowercase letters.
2. **Word Search**: From each position, check for possible completions using a dictionary of words.
3. **Phrase Generation**: String together random phrases from the list of possible completions, ensuring readability by adding padding.

## Scoping

This algorithm will be extremely slow- O(n^3) at least.

Some possible ways of scoping:
* Limit the number of blackout blocks- Notice that in my example above, there are really only 2 blackout blocks.
* Limit the number of scattered words- It might be a little too chaotic to have a ton of individual characters, maybe not.
* Limit the number of input words returned- With no word broken apart, you can just blackout whole words. The number of resulting solutions would be 2^n alone, where n is the number of whole words. That is, each word can be turned on or off.

# Shoutout
Words list taken from this project:
https://www.mit.edu/~ecprice/wordlist.10000
Originally, but I added curse words and such and deleted nonsense words like "tn"
