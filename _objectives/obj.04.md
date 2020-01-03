---
layout: objective
title: "Windows Log Analysis: Determine Attacker Technique"
#date: 2018-12-03
number: "4"
#image: "challenge.md"
question: "Identify the tool the attakcer used to retrieve domain password hashes from lsass.exe.  "
answer: "ntdsutil"
elf: "sugarplum"
images: ["1.png"]
narrative: ""
tags: [sample post, readability, test]
comments: false
image-dir: /assets/img/objectives/4
links: ["https://downloads.elfu.org/sysmon-data.json.zip","https://pen-testing.sans.org/blog/2019/12/10/eql-threat-hunting/comment-page-1/"]
comments: false
---


<figure>
	<img src="/assets/img/objectives/4/question.jpg">
	<figcaption>Question</figcaption>
</figure>

The hint was for SugarPlum Mary's terminal

<figure>
	<img src="/assets/img/elves/sugarplum/hint.jpg">
	<figcaption>Hint for image</figcaption>
</figure>


Just looking through the sysmon file, found this command

 "command_line": "ntdsutil.exe  \"ac i ntds\" ifm \"create full c:\\hive\" q q",


This didn't look like any of the other commands so I tried it.

ntdsutil