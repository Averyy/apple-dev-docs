# xpc_peer_requirement_t

**Framework**: XPC  
**Kind**: typealias

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias xpc_peer_requirement_t = OS_xpc_peer_requirement
```

#### Discussion

XPC peer requirement is an abstract type that represents a validated requirement on peers.

Users can specify a requirement via `xpc_peer_requirement_create_*` API. These constructors will return a non-null xpc_peer_requirement_t if the requirement is valid. Users can set a xpc_peer_requirement_t on connections, sessions or listeners using one of `xpc_*_set_peer_requirement` API.

xpc_peer_requirement_t is reference counted and concurrency-safe. One xpc_peer_requirement_t can be shared among multiple connections, sessions or listeners.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpc_peer_requirement_t)*