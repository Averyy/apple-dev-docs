# kDNSServiceFlagsWakeOnResolve

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
var kDNSServiceFlagsWakeOnResolve: UInt32 { get }
```

#### Discussion

This flag is meaningful only in DNSServiceResolve. When set, it tries to send a magic packet to wake up the client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/kdnsserviceflagswakeonresolve)*