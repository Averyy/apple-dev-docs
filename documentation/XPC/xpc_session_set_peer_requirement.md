# xpc_session_set_peer_requirement

**Framework**: XPC  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```c
extern void xpc_session_set_peer_requirement(xpc_session_t session, xpc_peer_requirement_t requirement);
```

## Discussion

Requires that the session peer satisfies a requirement.

It is a programming error to call `xpc_session_set_peer_*requirement` more than once per session.

All messages received on this session will be checked to ensure they come from a peer who satisfies the requirement. When a reply is expected on the session and the peer does not satisfy the requirement, the session will be canceled with cancellation handler called with a rich error describing the peer code signing error. For `xpc_session_send_message_with_reply_sync` NULL will be returned instead of reply, with `error_out` (if set) pointing to the rich error describing the peer code signing error.

## Parameters

- `session`: The session object which is to be modified. Must be inactive.
- `requirement`: The requirement to be satisfied by the peer. It will be retained by XPC.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_session_set_peer_requirement)*