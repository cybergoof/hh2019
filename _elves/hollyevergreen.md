---
layout: elf
title: "Mongo Pilfer"
#date: 2018-12-03
#image: "challenge.md"
question: "Get quiz answers"
answer: "/bin/ls ~/."
#terminal-hint: "Describe the hints from the terminal"
images: ["1.png"]
#narrative: "1"
elf-name: "Holly Evergreen"
elf-directory: "holly"
tags: [sample post, readability, test]
comments: false
image-dir: /assets/img/elves/holly
links: []
location: Netwars Room
comments: false
---

Need to get back into the mongo database and get the quiz solutions.  Need answers.


<figure>
	<img src="/assets/img/elves/holly/question.jpg">
	<figcaption>Holly Question</figcaption>
</figure>

Tried lsof -i, but the tool doesn't exist.  There is a ps tool.  

1) Need to Log into Mongo
2) Need to get the solution to the quiz

Doing a "ps -aux > test.txt" will show the command that started mongo

The port is 12121


<figure>
	<img src="/assets/img/elves/holly/2.jpg">
	<figcaption>Connect to mongo</figcaption>
</figure>

Using "show databases" gives a list of the database

<figure>
	<img src="/assets/img/elves/holly/3.jpg">
	<figcaption>Getting the databases</figcaption>
</figure>

Its likely test or elfu

"use test" and then "show collections" has a collection called "redherring"

So trying elfu


<figure>
	<img src="/assets/img/elves/holly/4.jpg">
	<figcaption>ElfU collection</figcaption>
</figure>

this gives us a command to run


<figure>
	<img src="/assets/img/elves/holly/success.jpg">
	<figcaption>Getting next hint</figcaption>
</figure>

Holly reveals a hint on digital rights management.  Ron Bowes talk on ElfScrow.  

<figure>
	<img src="/assets/img/elves/holly/hint.jpg">
	<figcaption>Getting next hint</figcaption>
</figure>