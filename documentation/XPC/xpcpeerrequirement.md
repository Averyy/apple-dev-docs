# XPCPeerRequirement

**Framework**: XPC  
**Kind**: struct

**Availability**:
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
struct XPCPeerRequirement
```

## Topics

### Initializers
- [init(lightweightCodeRequirements: XPCDictionary)](xpcpeerrequirement/init(lightweightcoderequirements:).md)
### Type Methods
- [static func codeRequirement(ProcessCodeRequirement) -> XPCPeerRequirement](xpcpeerrequirement/coderequirement(_:).md)
  Create an XPCPeerRequirement from a ProcessCodeRequirement
- [static func entitlement(String, matches: String) -> XPCPeerRequirement](xpcpeerrequirement/entitlement(_:matches:)-2bray.md)
  Create a requirement that the peer has the specified entitlement with the matching string value
- [static func entitlement(String, matches: Int) -> XPCPeerRequirement](xpcpeerrequirement/entitlement(_:matches:)-2ubq1.md)
  Create a requirement that the peer has the specified entitlement with the matching integer value
- [static func entitlement(String, matches: Bool) -> XPCPeerRequirement](xpcpeerrequirement/entitlement(_:matches:)-6h77e.md)
  Create a requirement that the peer has the specified entitlement with the matching bool value
- [static func hasEntitlement(String) -> XPCPeerRequirement](xpcpeerrequirement/hasentitlement(_:).md)
  Create a requirement that the peer has the specified entitlement
- [static func isFromSameTeam(andMatchesSigningIdentifier: String?) -> XPCPeerRequirement](xpcpeerrequirement/isfromsameteam(andmatchessigningidentifier:).md)
  Create a requirement that the peer is signed with the same team identifier as the current process. If provided, additionally requires that the peer has the specified signing identifier.
- [static func isPlatformCode(andMatchesSigningIdentifier: String?) -> XPCPeerRequirement](xpcpeerrequirement/isplatformcode(andmatchessigningidentifier:).md)
  Create a requirement that the peer is platform binary. If provided, additionally requires that the peer has the specified signing identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcpeerrequirement)*