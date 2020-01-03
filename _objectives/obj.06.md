---
layout: objective
title: "Splunk"
#date: 2018-12-03
number: "6"
#image: "challenge.md"
question: "What was the message for Kent that is embedded in the attack"
answer: "Kent you are so unfair. And we were going to make you the king of the Winter Carnival."
elf: "banas"
images: ["1.png"]
narrative: ""
tags: [sample post, readability, test]
comments: false
image-dir: /assets/img/objectives/6
links: ["https://splunk.elfu.org/","http://elfu-soc.s3-website-us-east-1.amazonaws.com/"]
comments: false
---


<figure>
	<img src="/assets/img/objectives/6/question.jpg">
	<figcaption>Question</figcaption>
</figure>

In splunk, there is the challenge questions.  There is training questions that will help with the Splunk reinal.
<figure>
	<img src="/assets/img/objectives/6/question.jpg">
	<figcaption>Question</figcaption>
</figure>


<figure>
	<img src="/assets/img/objectives/6/1.jpg">
	<figcaption>Splunk chats</figcaption>
</figure>
In the chats, there might be information

Kent mentions "crack under pressure".  Assuming a password cracking exercise

Alice Bluebird
<figure>
	<img src="/assets/img/objectives/6/alice.jpg">
	<figcaption>Alice Bluebird</figcaption>
</figure>

Raw Files at http://elfu-soc.s3-website-us-east-1.amazonaws.com/

ElfU Soc
<figure>
	<img src="/assets/img/objectives/6/elfusoc.jpg">
	<figcaption>Alice Bluebird</figcaption>
</figure>



System called Sweetums is communicating with the weird IP address from the beaconing from rita, which is professor banas


Training Question 4:
Potential process ID 5864 - 0x16e8

Using sysmon eventid of 1, found this
process ID 3552 - =0xDE0
Parent Process Id 3088 = 0xc10

Look at process 0x1748
Answer is 19th Century Holiday Cheer Assignment.docm
ANSWER - 6268 0x187c
(8/25/19 5:18:32.000 PM to 8/25/19 5:18:42.001 PM)

Question 5
index=main sourcetype=stoq |  table _time results{}.workers.smtp.to results{}.workers.smtp.from  results{}.workers.smtp.subject results{}.workers.smtp.body  | stats count(lower(results{}.workers.smtp.from)) by results{}.workers.smtp.from

21

Question 6


What was the message embedded

<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><dc:title>Holiday Cheer Assignment</dc:title><dc:subject>19th Century Cheer</dc:subject><dc:creator>Bradly Buttercups</dc:creator><cp:keywords></cp:keywords><dc:description>Kent you are so unfair. And we were going to make you the king of the Winter Carnival.</dc:description><cp:lastModifiedBy>Tim Edwards</cp:lastModifiedBy><cp:revision>4</cp:revision><dcterms:created xsi:type="dcterms:W3CDTF">2019-11-19T14:54:00Z</dcterms:created><dcterms:modified xsi:type="dcterms:W3CDTF">2019-11-19T17:50:00Z</dcterms:modified><cp:category></cp:category></cp:coreProperties>

<figure>
	<img src="/assets/img/objectives/6/answer.jpg">
	<figcaption>Final Answer</figcaption>
</figure>