---
layout: elf
title: "Nyanshell"
#date: 2018-12-03
#image: "challenge.md"
question: "List the home directory"
answer: "/bin/ls ~/."
#terminal-hint: "Describe the hints from the terminal"
images: ["1.png"]
#narrative: "1"
elf-name: "Alabaster Snowball"
elf-directory: "alabaster"
tags: [sample post, readability, test]
comments: false
image-dir: /assets/img/elves/alabaster
links: [https://linux.die.net/man/1/chattr]
location: Speaker Unprepardness Room
comments: false
---

Try and log into the shell, but Nyan cat comes in

<figure>
	<img src="/assets/img/elves/alabaster/question.jpg">
	<figcaption>Alabaster Question</figcaption>
</figure>

<figure>
	<img src="/assets/img/elves/alabaster/riddle.jpg">
	<figcaption>Alabaster Riddle</figcaption>
</figure>

The hint was about chattr, which changes the attribute on a file.

Attempting to log in just shows Nyancat

<figure>
	<img src="/assets/img/elves/alabaster/1.jpg">
	<figcaption>The Cat</figcaption>
</figure>

Going into Alabaster's directory, I can see the success app.  I also used "sudo -l" to see
what I can SUDO.  Chattr is one I can use sudo with.
<figure>
	<img src="/assets/img/elves/alabaster/2.jpg">
	<figcaption>Doing LS</figcaption>
</figure>

The bashrc file has a resource ID that is different when the terminal is opened.  And the date indicates
that bashrc is being changed for every player.

<figure>
	<img src="/assets/img/elves/alabaster/3.jpg">
	<figcaption>Bashrc</figcaption>
</figure>

The hint says he can't overwrite his shell.  File dates are key hints in Kringlcon. Looking at
the files in /bin, there is an nsh, that is probably nyanshell

<figure>
	<img src="/assets/img/elves/alabaster/4.jpg">
	<figcaption>Nsh</figcaption>
</figure>

The lattr and sh show that nsh is immutable but could be overwritten
<figure>
	<img src="/assets/img/elves/alabaster/5.jpg">
	<figcaption>Listing</figcaption>
</figure>

I just need to copy "bash" to "nsh" after I remove the immutable bit
<figure>
	<img src="/assets/img/elves/alabaster/6.jpg">
	<figcaption>Changing the bit</figcaption>
</figure>



Su as alabaster gets it working
<figure>
	<img src="/assets/img/elves/alabaster/success.jpg">
	<figcaption>Getting next hint</figcaption>
</figure>

Alabaster then reveals a hint. The Frido Sleigh context has a capta.  There is a talk about machine learning that might help

<figure>
	<img src="/assets/img/elves/alabaster/hint.jpg">
	<figcaption>Getting next hint</figcaption>
</figure>