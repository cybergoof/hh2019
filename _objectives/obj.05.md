---
layout: objective
title: "Network Log Analysis: Determine Compromised System"
#date: 2018-12-03
number: "5"
#image: "challenge.md"
question: "Can you help identify the IP address of the malware-infected system "
answer: "192.168.134.130"
elf: "sparkle"
images: ["1.png"]
narrative: ""
tags: [sample post, readability, test]
comments: false
image-dir: /assets/img/objectives/5
links: ["https://downloads.elfu.org/elfu-zeeklogs.zip",https://github.com/activecm/rita"]
comments: false
---


<figure>
	<img src="/assets/img/objectives/5/question.jpg">
	<figcaption>Question</figcaption>
</figure>

The hint was for Sparkle Redberry terminal

<figure>
	<img src="/assets/img/elves/sparkle/hint.jpg">
	<figcaption>Hint for image</figcaption>
</figure>

The hint says to talk to Rita. This likely references Real Intelligence Threat Analytics https://github.com/activecm/rita

Running Rita was not necessary, the log files already had the exported HTML files in <path>/ELFU

<figure>
	<img src="/assets/img/objectives/5/1.jpg">
	<figcaption>The Beacons</figcaption>
</figure>

Just trying the first ip address of 192.168.134.130 worked
