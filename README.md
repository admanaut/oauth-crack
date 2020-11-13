# OAuth 2.0 Crack

_A partial implementation of the OAuth 2.0 framework to showcase some common auth flow use cases, for educational purposes._

Abstract Protocol Flow:

```
+--------+                               +---------------+
|        |--(A)- Authorization Request ->|   Resource    |
|        |                               |     Owner     |
|        |<-(B)-- Authorization Grant ---|               |
|        |                               +---------------+
|        |
|        |                               +---------------+
|        |--(C)-- Authorization Grant -->| Authorization |
| Client |                               |     Server    |
|        |<-(D)----- Access Token -------|               |
|        |                               +---------------+
|        |
|        |                               +---------------+
|        |--(E)----- Access Token ------>|    Resource   |
|        |                               |     Server    |
|        |<-(F)--- Protected Resource ---|               |
+--------+                               +---------------+
```

Each of these entities (except Resource Owner*) are implemented in separate services, and they are:

* Client               - [fissure](./fissure)
* Authorization Server - [crater](./crater)
* Resource Server      - [crevasse](./crevasse)

_*to keep it simple, Resource Owner is an end-user and the (A) Authorization Request is made to the Authorization Server directly_

This implementation follows the standard [RFC6749](https://tools.ietf.org/html/rfc6749) but only partially.

## Try it out

TODO
