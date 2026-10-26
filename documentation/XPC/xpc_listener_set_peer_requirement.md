# xpc_listener_set_peer_requirement

**Framework**: XPC  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
extern void xpc_listener_set_peer_requirement(xpc_listener_t listener, xpc_peer_requirement_t requirement);
```

#### Discussion

Requires that the listener peer satisfies a requirement.

It is a programming error to call `xpc_listener_set_peer_*requirement` more than once per listener.

All messages received on this listener will be checked to ensure they come from a peer who satisfies the code signing requirement. Requests that do not satisfy the requirement are dropped.

Peer sessions created from the listener do not inherit the requirement.

## Parameters

- `listener`: The listener object which is to be modified. Must be inactive.
- `requirement`: The requirement to be satisfied by the peer. It will be retained by XPC.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_listener_set_peer_requirement)*