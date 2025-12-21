# isFromSameTeam(andMatchesSigningIdentifier:)

**Framework**: XPC  
**Kind**: method

Create a requirement that the peer is signed with the same team identifier as the current process. If provided, additionally requires that the peer has the specified signing identifier.

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
static func isFromSameTeam(andMatchesSigningIdentifier: String? = nil) -> XPCPeerRequirement
```

#### Return Value

A `XPCPeerRequirement` object representing the requirement

#### Discussion

- andMatchesSigningIdentifier: If non-nil, The signing identifier the peer must have


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcpeerrequirement/isfromsameteam(andmatchessigningidentifier:))*