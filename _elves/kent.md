---
layout: elf
title: "Smart Braces Terminal"
#date: 2018-12-03
#image: "challenge.md"
question: "Keep students out of head"
answer: "q <enter>"
#terminal-hint: "Describe the hints from the terminal"
images: ["1.jpg"]
#narrative: "1"
elf-name: "Kent Tinseltooth"
elf-directory: "kent"
tags: [sample post, readability, test]
comments: false
image-dir: /assets/img/elves/kent
links: []
docker: https://docker2019.kringlecon.com/?challenge=iptables&id=8276eb87-eca0-45ac-bf8d-b8efcef8925a&username=cybergoof
hint: https://upcloud.com/community/tutorials/configure-iptables-centos/
comments: false
---

Kent Tinseltooth wants help with his terminal.

<figure>
	<img src="/assets/img/elves/kent/1.jpg">
	<figcaption>Kent Terminal</figcaption>
</figure>

Looks like there is an "inner voice".  And we need to block it out with an IPTables change.

looking in the current directory, there is an MD file that has some information about the challenge

<figure>
	<img src="/assets/img/elves/kent/2.jpg">
	<figcaption>IOTteethBraces.md</figcaption>
</figure>

It supports FTP, HTTP and SSH access.  The requirement is to configure properly.
The requirements to setup IP Tables is

A proper configuration for the Smart Braces should be exactly:
1. Set the default policies to DROP for the INPUT, FORWARD, and OUTPUT chains.
sudo iptables -P FORWARD DROP
sudo iptables -P INPUT DROP
sudo iptables -P OUTPUT DROP
2. Create a rule to ACCEPT all connections that are ESTABLISHED,RELATED on the INPUT and the OUTPU
T chains.
sudo iptables -A INPUT,OUTPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

3. Create a rule to ACCEPT only remote source IP address 172.19.0.225 to access the local SSH serv
er (on port 22).
# That IP address resolves to elfuiotbracesiptables_checker.iptablesnetwork
sudo iptables -A INPUT -p tcp --dport 22 -s 172.19.0.225 -j ACCEPT

4. Create a rule to ACCEPT any source IP to the local TCP services on ports 21 and 80.
sudo iptables -A INPUT -p tcp --dport 21,80 -j ACCEPT

5. Create a rule to ACCEPT all OUTPUT traffic with a destination TCP port of 80.
sudo iptables -A OUTPUT -p tcp --dport 80 -j ACCEPT
6. Create a rule applied to the INPUT chain to ACCEPT all traffic from the lo interface.
iptables -A INPUT -o lo -j ACCEPT

sudo iptables -A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT
sudo iptables -P FORWARD DROP
sudo iptables -P INPUT DROP
sudo iptables -P OUTPUT DROP
sudo iptables -A INPUT -p tcp --dport 22 -s 172.19.0.225 -j ACCEPT
sudo iptables -A INPUT -p tcp -m multiport --dports 21,80 -j ACCEPT
sudo iptables -A OUTPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -i lo -j ACCEPT

It worked.  It is hardened.  

<figure>
	<img src="/assets/img/elves/kent/3.jpg">
	<figcaption>IOTteethBraces.md</figcaption>
</figure>


Kent says that the "sleigh device" is being tested at srf.elfu.org with default creds
 
Kent's hint is to get into the crate in the Student Union