# entitlement(_:matches:)

**Framework**: XPC  
**Kind**: method

Create a requirement that the peer has the specified entitlement with the matching bool value

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
static func entitlement(_ entitlement: String, matches value: Bool) -> XPCPeerRequirement
```

#### Return Value

A `XPCPeerRequirement` object representing the requirement

#### Discussion

- entitlement: The entitlement to check.
- value: The bool value to match


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcpeerrequirement/entitlement(_:matches:)-6h77e)*