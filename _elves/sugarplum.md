---
layout: elf
title: "Linux Path"
#date: 2018-12-03
#image: "challenge.md"
question: "List the home directory"
answer: "/bin/ls ~/."
#terminal-hint: "Describe the hints from the terminal"
images: ["1.png"]
#narrative: "1"
elf-name: "Sugarplum Mary"
elf-directory: "sugarplum"
tags: [sample post, readability, test]
comments: false
image-dir: /assets/img/elves/sugarplum
links: [https://www.endgame.com/our-experts/ross-wolf]
location: Hermy Hall
comments: false
---

Sugarplum Mary is requesting that we review files in linux

<figure>
	<img src="/assets/img/elves/sugarplum/question.jpg">
	<figcaption>Sugarplum Question</figcaption>
</figure>

<figure>
	<img src="/assets/img/elves/sugarplum/riddle.jpg">
	<figcaption>Sugarplum Riddle</figcaption>
</figure>

In the question, there is a hint that the green words mean something
* file
* home/
* ls
* which
* find
* path
* location

I need to get a listing for my home directory

Doing an "ls" shows that the ls is in the wrong place

<figure>
	<img src="/assets/img/elves/sugarplum/1.jpg">
	<figcaption>Doing LS</figcaption>
</figure>

Using find, I was able to find the real ls 
<figure>
	<img src="/assets/img/elves/sugarplum/2.jpg">
	<figcaption>Doing LS</figcaption>
</figure>

Running the right ls, I get success
<figure>
	<img src="/assets/img/elves/sugarplum/success.jpg">
	<figcaption>Getting next hint</figcaption>
</figure>

Sugarplum then reveals a hint. The Sysmon and EQL Challenge, leverage Ross Wolf's work in EQL

<figure>
	<img src="/assets/img/elves/sugarplum/hint.jpg">
	<figcaption>Getting next hint</figcaption>
</figure>