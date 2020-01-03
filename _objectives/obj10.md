---
layout: objective
title: "Recover cleartext document"
#date: 2018-12-03
number: "10"
#image: "challenge.md"
question: "Using the crypto tool, recover plaintext from a document"
answer: ""
elf: "holly"
images: ["1.png"]
narrative: ""
tags: [sample post, readability, test]
comments: false
image-dir: /assets/img/objectives/10
links: ["https://downloads.elfu.org/elfscrow.exe", "https://downloads.elfu.org/elfscrow.pdb", "https://downloads.elfu.org/ElfUResearchLabsSuperSledOMaticQuickStartGuideV1.2.pdf.enc", "http://www.youtube.com/watch?v=obJdpKDpFBA"]
comments: false
---
<figure>
	<img src="/assets/img/objectives/10/question.jpg">
	<figcaption>Question</figcaption>
</figure>


Holly Evergreen hint says to listen to Ron Bowes talk on reverse engineering.

NOTES FROM TALK

Tools - IDA.  www.hex-rays.com/products/ida/support/download_freeware.html
Microsoft Studio
Ruby 2.4

KEYS
7 or 8 Bytes - DES, 
16, 24, 32 Bytes - AES
Keys will look random
Key is shared somehow
Keys should be cryptographically random.  If you see a weak random generator, then the numbers are not actually random.  

Demo
In the example, he shows that some keys are generated once a second.  So, the key is based on time.  In the hint for this question, we know when the program was executed.  So we likely can use that to get the key

If the seed is the current time, then we know the code. 

Detecting bad Ramdon
Linear Congruential Generator
You start with a SEED, and then some random number is generated from it.

Take the SEED, and google the number.  You likely will find the implementation
HINT: 29943829.  Copy the constant into google, you might get the function.

We want to figure out what the algorithm is, and what the mode is.

1-byte blocks - A stream cipher like RC4 or Salsa20.
8 byte blocks - 7 or 8 byte key?  DES
16 byte blocks?  16 or 24 or 32 byte key?  AES-128, AES-192 or AES-256

ECB encrypts each blocks separatly so.
CBC with no IV is also bad.  