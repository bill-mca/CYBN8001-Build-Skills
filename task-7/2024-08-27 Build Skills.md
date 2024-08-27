---
title: 2024-08-27 Build Skills

---

# Part 1 - Break a cipher

## Decryption

This is the cipher I was given:

> ZYP ZQ ESP XZDE DTYRFWLC NSLCLNEPCTDETND ZQ ESP LCE ZQ OPNTASPCTYR TD ESP DECZYR NZYGTNETZY AZDDPDDPO MJ PGPCJ APCDZY, PGPY XZOPCLEPWJ LNBFLTYEPO HTES TE, ESLE SP TD LMWP EZ NZYDECFNE L NTASPC HSTNS YZMZOJ PWDP NLY OPNTASPC. T SLGP LWDZ ZMDPCGPO ESLE ESP NWPGPCPC ESP APCDZY, ESP XZCP TYETXLEP TD STD NZYGTNETZY.

I used the online tool from [cryptii.com](https://cryptii.com/) to decode the cipher. By a process of trial and error, I found that it has a **shift of 11**. The decoded Message reads:

> ONE OF THE MOST SINGULAR CHARACTERISTICS OF THE ART OF DECIPHERING IS THE STRONG CONVICTION POSSESSED BY EVERY PERSON, EVEN MODERATELY ACQUAINTED WITH IT, THAT HE IS ABLE TO CONSTRUCT A CIPHER WHICH NOBODY ELSE CAN DECIPHER. I HAVE ALSO OBSERVED THAT THE CLEVERER THE PERSON, THE MORE INTIMATE IS HIS CONVICTION.

![A screenshot of cryptii's deciphering tool.](src/2024-08-27_Cryptii_cipher.png)

## Improvements

If you often needed to break caesar ciphers, you could automate this process a little bit more by having a script test all possible permutations at once. If you save the cipher as a txt file. It would be possible to try all possible permutations in bash using the following script

```bash
for i in {1..25}; do
    echo "Shift $i:"
    tr "$(printf %${i}s | tr ' ' '[A-Za-z]')" "$(printf %${i}s | tr 'A-Za-z' '[A-Za-z]')" < cipher.txt
    echo
done
```


This automates the process of testing all 25 possible permutatons. A human still needs to read each version of the output text to see if it is sensible. Further automation would result from getting the computer to check the output for sensibility. There are two approaches. 

### Test for sensible words
One would be to take some of the output and check if the words are dictionary words. You can download a version of the [Moby dictionary](https://en.wikipedia.org/wiki/Moby_Project) like this:

```bash
wget https://github.com/dwyl/english-words/raw/master/words.txt 
```

Adding a loop to generate and save possible permutaions, the core of the code would test each permutation like this:


```bash
cat permutation.txt | tr '[:upper:]' '[:lower:]' | tr -s '[:space:]' '\n' | grep -Fx -f ./words.txt | wc -l
```

### Test for character frequency
Rather than grepping a 4.6Mb file many times, it would be much more efficient to test the [letter frequency](https://en.wikipedia.org/wiki/Letter_frequency) of each permutation. In real english text E occurs more often than other characters. According to the Wikipedia article:

>Herbert S. Zim, in his classic introductory cryptography text Codes and Secret Writing, gives the English letter frequency sequence as "ETAON RISHD LFCMU GYPWB VKJXZQ"...

There's a bit of statistics involved, so you'd have to write or find some custom software rather than relying on standard command line utilities but checking the letter frequency of each possible shift would allow you to identify the right shift.

### Best method
Calculating the frequency on the cipher would actually be the most computationally efficient way of breaking an arbitrary caesar cipher. If you calculate the letter frequencies, you will find that there is a similar distribution to real English writing but that, for example, X is the most common letter instead of E. This would indicate a shift of -7. This approach is not nearly as demanding of computational resources as the method that brute forces all possible permutations. 

This method relies on some of the redundant information in the message to break the cipher. The frequency of occurence of different letters isn't enough to know the message, but it is enough to know whether it is a message in English.We don't need to process the whole message break the caesar cipher. this little bit of metadata is enough. 

# Part 2 - Analyze code

