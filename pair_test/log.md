# Testing all of the socket combinations valid for a connect-bind pair...
* PUB SUB - can send message from one to many
* REQ REP - requires response message... so maybe not the fastest
* REQ ROUTER
* DEALER REP - addr in use error
* DEALER ROUTER
* DEALER DEALER
* ROUTER ROUTER
* PUSH PULL - addr in use error
* PAIR PAIR - doesn't work
-- Note: ROUTER sends messages to a specified client. Not useful here.

http://api.zeromq.org/3-2:zmq-socket
http://zguide.zeromq.org/page:all#toc32
https://www.digitalocean.com/community/tutorials/how-to-work-with-the-zeromq-messaging-library

TO DO:
- fix push pull : currently giving "address already in use" errors
