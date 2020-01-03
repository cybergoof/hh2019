---
layout: objective
title: "Windows Log Analysis: Evaluate Attack Outcome"
#date: 2018-12-03
number: "3"
#image: "challenge.md"
question: "Attacks against the ELf U domain.  Identify the user account that the attacker compromised wtih password spary"
answer: "supatree"
elf: "busy"
images: ["1.png"]
narrative: ""
tags: [sample post, readability, test]
comments: false
image-dir: /assets/img/objectives/3
links: ["https://downloads.elfu.org/Security.evtx.zip","https://github.com/sans-blue-team/DeepBlueCLI"]
comments: false
---



<figure>
	<img src="/assets/img/objectives/3/question.jpg">
	<figcaption>Question</figcaption>
</figure>

The hint was for Busy Evergreen's terminal

<figure>
	<img src="/assets/img/elves/busy/hint.jpg">
	<figcaption>Hint for image</figcaption>
</figure>

The DeepBlueCLI tool can help detect password spray
https://github.com/sans-blue-team/DeepBlueCLI

Running the command, I found some password sprays

Date    : 11/19/2019 7:21:51 AM
Log     : Security
EventID : 4648
Message : Distributed Account Explicit Credential Use (Password Spray Attack)
Results : The use of multiple user account access attempts with explicit credentials is an indicator of a password 
          spray attack.
          Target Usernames: ygoldentrifle esparklesleigh hevergreen Administrator sgreenbells cjinglebuns 
          tcandybaubles bbrandyleaves bevergreen lstripyleaves gchocolatewine ltrufflefig wopenslae mstripysleigh 
          pbrandyberry civysparkles sscarletpie ftwinklestockings cstripyfluff gcandyfluff smullingfluff hcandysnaps 
          mbrandybells twinterfig supatree civypears ygreenpie ftinseltoes smary ttinselbubbles dsparkleleaves 
          Accessing Username: -
          Accessing Host Name: -

Then looked for successful logins

Date    : 8/23/2019 8:00:20 PM
Log     : Security
EventID : 4672
Message : Multiple admin logons for one account
Results : Username: supatree
          User SID Access Count: 2

Answer: supatree