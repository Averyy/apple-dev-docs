# hasEntitlement(_:)

**Framework**: XPC  
**Kind**: method

Create a requirement that the peer has the specified entitlement

**Availability**:
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
static func hasEntitlement(_ entitlement: String) -> XPCPeerRequirement
```

#### Return Value

A `XPCPeerRequirement` object representing the requirement

#### Discussion

- entitlement: The entitlement to check.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcpeerrequirement/hasentitlement(_:))*