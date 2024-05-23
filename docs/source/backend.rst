Back End Overview
=================

As already mentioned in Source Code Overview, the backend was created using Meteor.
Meteor connects to clients using a websocket protocol, which is a full-duplex communication protocol that closes only once a connection state has died.
That is, websocket connections are bidirectional and are kept open even after the response of a request is received by the client.
The benefit of this is that after successfully connecting to a client, the server can “push” data to the client whereas over traditional protocols (HTTP), a connection to a client is closed once the response from the server is received.
A traditional client receives data updates thus by re-requesting the same resources.

For time-sensitive applications, this translates to requesting the same resources from a server in very short time intervals (polling) which unnecessarily increases the load on a server.
It is encouraged the check out the Meteor documentation for more information or even better review the old project report, pages 31-33, for a brief, but concise overview of Meteor's capabilities.

Meteor Publications
-------------------

...

Meteor Methods
--------------

...

Database Collections
--------------------

...
