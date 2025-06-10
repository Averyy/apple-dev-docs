# init(service:targetQueue:options:requirement:incomingSessionHandler:)

**Framework**: XPC  
**Kind**: init

Creates a listener with the service defined by the provided name, and requires that the session peer has the specified requirement.

**Availability**:
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
@preconcurrency
convenience init(service: String, targetQueue: DispatchQueue? = nil, options: XPCListener.InitializationOptions = .none, requirement: XPCPeerRequirement, incomingSessionHandler: @escaping (XPCListener.IncomingSessionRequest) -> XPCListener.IncomingSessionRequest.Decision) throws
```

#### Discussion

- service: The Mach service or XPC Service name to create the listener with.
- requirement: The requirement the peer must have

> **Note**: For a listener, requests that do not satisfy the requirement are dropped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpclistener/init(service:targetqueue:options:requirement:incomingsessionhandler:))*