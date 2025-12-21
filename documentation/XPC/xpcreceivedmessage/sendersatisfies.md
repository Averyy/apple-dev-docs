# senderSatisfies(_:)

**Framework**: XPC  
**Kind**: method

Check whether the sender of the received message satisfies the specified requirement.

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func senderSatisfies(_ requirement: XPCPeerRequirement) -> Bool
```

#### Return Value

A `Bool` indicating whether the sender satisfies the requirement

#### Discussion

- requirement: The requirement the peer must have


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcreceivedmessage/sendersatisfies(_:))*