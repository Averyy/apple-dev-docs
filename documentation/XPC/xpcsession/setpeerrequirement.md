# setPeerRequirement(_:)

**Framework**: XPC  
**Kind**: method

Requires that the session peer has the specified requirement

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func setPeerRequirement(_ requirement: XPCPeerRequirement)
```

#### Discussion

- requirement: The requirement the peer must have

> **Note**: The session must be inactive to set a peer requirement. It is a programming error to call multiple of the `setPeerRequirement` method on the same session.

> **Note**: All messages received on this session will be checked to ensure that they come from a peer who satisfies the requirement. When a reply is expected on the session and the peer does not satisfy the requirement, the session will be canceled and user’s cancelation handler will be invoked with `XPCRichError` describing the code signing error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcsession/setpeerrequirement(_:))*