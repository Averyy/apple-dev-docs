# OS_xpc_peer_requirement

**Framework**: XPC  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```objc
@protocol OS_xpc_peer_requirement <NSObject>
```

#### Overview

XPC peer requirement is an abstract type that represents a validated requirement on peers.

Users can specify a requirement via `xpc_peer_requirement_create_*` API. These constructors will return a non-null xpc_peer_requirement_t if the requirement is valid. Users can set a xpc_peer_requirement_t on connections, sessions or listeners using one of `xpc_*_set_peer_requirement` API.

xpc_peer_requirement_t is reference counted and concurrency-safe. One xpc_peer_requirement_t can be shared among multiple connections, sessions or listeners.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/os_xpc_peer_requirement)*