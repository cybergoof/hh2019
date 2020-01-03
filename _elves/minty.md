---
layout: elf
title: "Holiday Trail"
#date: 2018-12-03
#image: "challenge.md"
question: "Win Holiday Trail"
answer: ""
#terminal-hint: "Check the talk about Web Applicaiton Pen Testing"
terminal-hyperlink: "https://trail.elfu.org?challenge=trail&id=21692743-3f79-4742-b5d2-2816a353f470&username=cybergoof"
talk: http://www.youtube.com/watch?v=0T6-DQtzCgM
images: ["1.png"]
#narrative: "1"
elf-name: "Minty Candycane"
elf-directory: "minty"
location: 
tags: [sample post, readability, test]
comments: false
image-dir: /assets/img/elves/minty
links: []
comments: false
---
<figure>
	<img src="/assets/img/elves/minty/question.png">
	<figcaption>Mintys Question</figcaption>
</figure>

Minty Candycan wants to play a game, which looks like a play on Oregan Trail

<figure>
	<img src="/assets/img/elves/minty/1.png">
	<figcaption>Play Game</figcaption>
</figure>
A hint is to watch the video
<figure>
	<img src="/assets/img/elves/minty/talk.png">
	<figcaption>Talk for game</figcaption>
</figure>

Hints from talk:
Manipulate the URL
HTML/String injection.  HInt is that there is no escaping
Chat or video might do some level of hashing.  Look at breaking integrity of data by breaking client side.



At the top of the game, there is a URL that has some really interesting information
hhc://trail.hhc/store/?difficulty=0&distance=0&money=5000&pace=0&curmonth=7&curday=1&reindeer=2&runners=2&ammo=100&meds=20&food=400&name0=Chloe&health0=100&cond0=0&causeofdeath0=&deathday0=0&deathmonth0=0&name1=Dop&health1=100&cond1=0&causeofdeath1=&deathday1=0&deathmonth1=0&name2=Emmanuel&health2=100&cond2=0&causeofdeath2=&deathday2=0&deathmonth2=0&name3=Mildred&health3=100&cond3=0&causeofdeath3=&deathday3=0&deathmonth3=0

All values are here

I just changed "money" to 50000.  And then bought a bunch of supplies and then started the game.

hash was 275cae9b5161303d241d84225f72947a

For MEDIUM, I dived into the javascript and found where all the hidden values are.  I changed 'distance' to 8000
<figure>
	<img src="/assets/img/elves/minty/2.png">
	<figcaption>Making the change</figcaption>
</figure>


<figure>
	<img src="/assets/img/elves/minty/medium.png">
	<figcaption>Medium</figcaption>
</figure>

Trying to manipulate the hidden form elements on the game page will result in an error. Therefore, there is some sort of evaluation happening of the elements.

There is a "hash value", which is an easily crackable MD5.

The MD5 for the initial game is "bc573864331a9e42e4511de6f678aa83" which is decoded to 1626

After tracking changes to values, it seems that decoded value is simply all the variable values added up.

Therefore, to skip to the end, take 1626, which has a "distance" 0, add 8000, and MD5 the resulting 9626
649d45bf179296e31731adfd4df25588

<figure>
	<img src="/assets/img/elves/minty/hard.png">
	<figcaption>Hard</figcaption>
</figure>

Received varification hash of 57ec46350ce6dbd9881127dd6d102cfb

Minty's hint is about physical key from the key grinder.  Need to look in the console for a key image

<figure>
	<img src="/assets/img/elves/minty/hint.png">
	<figcaption>Hard</figcaption>
</figure>

