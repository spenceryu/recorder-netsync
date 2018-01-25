# Testing all of the socket combinations valid for a connect-bind pair...
* PUB SUB - can send message from one to many
* REQ REP - requires response message... so maybe not the fastest
* REQ ROUTER
* DEALER ROUTER
* DEALER DEALER
* ROUTER ROUTER
* PUSH PULL
* PAIR PAIR - doesn't work

http://api.zeromq.org/3-2:zmq-socket
http://zguide.zeromq.org/page:all#toc32
https://www.digitalocean.com/community/tutorials/how-to-work-with-the-zeromq-messaging-library

TO DO:
- fix push pull : currently giving "address already in use" errors
