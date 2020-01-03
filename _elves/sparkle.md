---
layout: elf
title: "Xmas Cheer Laser"
#date: 2018-12-03
#image: "challenge.md"
question: "Recalibrate the Laser"
answer: "q <enter>"
#terminal-hint: "Describe the hints from the terminal"
images: ["1.png"]
#narrative: "1"
elf-name: "Sparkle Redberry"
elf-directory: "sparkle"
tags: [sample post, readability, test]
comments: false
image-dir: /assets/img/elves/sparkle
links: []
comments: false
---

Sparkle is requesting help recalibrating the laser

<figure>
	<img src="/assets/img/elves/sparkle/riddle.jpg">
	<figcaption>The main terminal screen</figcaption>
</figure>

The message tells how to command the laser
<figure>
	<img src="/assets/img/elves/sparkle/3.jpg">
	<figcaption>Laser Command</figcaption>
</figure>
We need to find values for Refraction, Temperature and Gas Mixture.

## Angle
The message said to play the calling card.  
<figure>
	<img src="/assets/img/elves/sparkle/2.jpg">
	<figcaption>The calling card</figcaption>
</figure>

It says to get the history, so we run the command Get-History, and format it so that we can read the entire message.
<figure>
	<img src="/assets/img/elves/sparkle/4.jpg">
	<figcaption>History Command</figcaption>
</figure>

The answer for angle is found here. Curiously, the angle example command is not in the help screen
<figure>
	<img src="/assets/img/elves/sparkle/6.jpg">
	<figcaption>Results of History Command</figcaption>
</figure>


## Refraction
<figure>
	<img src="/assets/img/elves/sparkle/5.jpg">
	<figcaption>Results of History Command</figcaption>
</figure>

The hint says to look at for application system wide variables.  This is likely environment variables


<figure>
	<img src="/assets/img/elves/sparkle/7.jpg">
	<figcaption>The environment command</figcaption>
</figure>
<figure>
	<img src="/assets/img/elves/sparkle/8.jpg">
	<figcaption>The environment command</figcaption>
</figure>

This did not produce a value, but a hint. Need to look all through /etc for a file that is compressed.  Look for the latest written file

<figure>
	<img src="/assets/img/elves/sparkle/9.jpg">
	<figcaption>The environment command</figcaption>
</figure>

<figure>
	<img src="/assets/img/elves/sparkle/10.jpg">
	<figcaption>Exapand the archive and new Type</figcaption>
</figure>

<figure>
	<img src="/assets/img/elves/sparkle/11.jpg">
	<figcaption>The runme.elf</figcaption>
</figure>

The refraction is 1.867

## Temperature
The hint says to look for the MD5 file in the home directory

Look through all the files and pipe to Get-FileHash
<figure>
	<img src="/assets/img/elves/sparkle/12.jpg">
	<figcaption>Get File Hash</figcaption>
</figure>

<figure>
	<img src="/assets/img/elves/sparkle/13.jpg">
	<figcaption>Get File Hash</figcaption>
</figure>

The Temperature is -33.5

## Gas
The hint says to look for the largest filename file with path
<figure>
	<img src="/assets/img/elves/sparkle/13.jpg">
	<figcaption>Get File Hash</figcaption>
</figure>

<figure>
	<img src="/assets/img/elves/sparkle/14.jpg">
	<figcaption>Retrieve the largest file path</figcaption>
</figure>


<figure>
	<img src="/assets/img/elves/sparkle/15.jpg">
	<figcaption>Retrieve the largest file path</figcaption>
</figure>

It says to stop the processes in order, and reveal file /shall/see

<figure>
	<img src="/assets/img/elves/sparkle/16.jpg">
	<figcaption>Get the processes</figcaption>
</figure>

now, we stop them in order and then stop each process in order, and see the value
<figure>
	<img src="/assets/img/elves/sparkle/17.jpg">
	<figcaption>Getting next hint</figcaption>
</figure>

We have to look through an xml file and get the ID with the least occurances, then read the event log

<figure>
	<img src="/assets/img/elves/sparkle/18.jpg">
	<figcaption>Getting next hint</figcaption>
</figure>

Searching gets me the gas values

<figure>
	<img src="/assets/img/elves/sparkle/19.jpg">
	<figcaption>Getting next hint</figcaption>
</figure>

Gas O=6&H=7&He=3&N=4&Ne=22&Ar=11&Xe=10&F=20&Kr=8&Rn=9

# Putting it together.
The command to calibrate the laser


(Invoke-WebRequest -Uri http://localhost:1225/api/off).RawContent
(Invoke-WebRequest -Uri http://localhost:1225/api/refraction?val=1.867).RawContent
(Invoke-WebRequest -Uri http://localhost:1225/api/temperature?val=-33.5).RawContent
(Invoke-WebRequest -Uri http://localhost:1225/api/angle?val=65.5).RawContent
(Invoke-WebRequest -Uri http://localhost:1225/api/gas -Method POST -Body "O=6&H=7&He=3&N=4&Ne=22&Ar=11&Xe=10&F=20&Kr=8&Rn=9").RawContent
(Invoke-WebRequest -Uri http://localhost:1225/api/on).RawContent
(Invoke-WebRequest -Uri http://localhost:1225/api/output).RawContent

<figure>
	<img src="/assets/img/elves/sparkle/success.jpg">
	<figcaption>Getting next hint</figcaption>
</figure>

Sparkle then reveals a hint

<figure>
	<img src="/assets/img/elves/sparkle/hint.jpg">
	<figcaption>Getting next hint</figcaption>
</figure>