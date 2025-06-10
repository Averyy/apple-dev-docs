# entitlement(_:matches:)

**Framework**: XPC  
**Kind**: method

Create a requirement that the peer has the specified entitlement with the matching string value

**Availability**:
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
static func entitlement(_ entitlement: String, matches value: String) -> XPCPeerRequirement
```

#### Return Value

A `XPCPeerRequirement` object representing the requirement

#### Discussion

- entitlement: The entitlement to check.
- value: The string value to match


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcpeerrequirement/entitlement(_:matches:)-2bray)*