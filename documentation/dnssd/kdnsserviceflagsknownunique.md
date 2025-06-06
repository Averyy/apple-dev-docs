# kDNSServiceFlagsKnownUnique

**Framework**: dnssd  
**Kind**: var

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var kDNSServiceFlagsKnownUnique: UInt32 { get }
```

#### Discussion

Client guarantees that record names are unique, so we can skip sending out initial probe messages. Standard name conflict resolution is still done if a conflict is discovered. Currently only valid for a DNSServiceRegister call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsknownunique)*