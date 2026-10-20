# XPCPeerRequirement

**Framework**: XPC  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
struct XPCPeerRequirement
```

## Topics

### Initializers
- [init(lightweightCodeRequirements: XPCDictionary)](./xpcpeerrequirement/init%28lightweightcoderequirements%29.md)
### Type Methods
- [static func codeRequirement(ProcessCodeRequirement) -> XPCPeerRequirement](./xpcpeerrequirement/coderequirement%28_%29.md)
  Create an XPCPeerRequirement from a ProcessCodeRequirement
- [static func entitlement(String, matches: String) -> XPCPeerRequirement](./xpcpeerrequirement/entitlement%28_,matches%29-2bray.md)
  Create a requirement that the peer has the specified entitlement with the matching string value
- [static func entitlement(String, matches: Int) -> XPCPeerRequirement](./xpcpeerrequirement/entitlement%28_,matches%29-2ubq1.md)
  Create a requirement that the peer has the specified entitlement with the matching integer value
- [static func entitlement(String, matches: Bool) -> XPCPeerRequirement](./xpcpeerrequirement/entitlement%28_,matches%29-6h77e.md)
  Create a requirement that the peer has the specified entitlement with the matching bool value
- [static func hasEntitlement(String) -> XPCPeerRequirement](./xpcpeerrequirement/hasentitlement%28_%29.md)
  Create a requirement that the peer has the specified entitlement
- [static func isFromSameTeam(andMatchesSigningIdentifier: String?) -> XPCPeerRequirement](./xpcpeerrequirement/isfromsameteam%28andmatchessigningidentifier%29.md)
  Create a requirement that the peer is signed with the same team identifier as the current process. If provided, additionally requires that the peer has the specified signing identifier.
- [static func isPlatformCode(andMatchesSigningIdentifier: String?) -> XPCPeerRequirement](./xpcpeerrequirement/isplatformcode%28andmatchessigningidentifier%29.md)
  Create a requirement that the peer is platform binary. If provided, additionally requires that the peer has the specified signing identifier.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xpc/xpcpeerrequirement)*