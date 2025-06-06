# kDNSServiceFlagsSuppressUnusable

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
var kDNSServiceFlagsSuppressUnusable: UInt32 { get }
```

#### Discussion

This flag is meaningful only in DNSServiceQueryRecord which suppresses unusable queries on the wire. If “hostname” is a wide-area unicast DNS hostname (i.e. not a “.local.” name) but this host has no routable IPv6 address, then the call will not try to look up IPv6 addresses for “hostname”, since any addresses it found would be unlikely to be of any use anyway. Similarly, if this host has no routable IPv4 address, the call will not try to look up IPv4 addresses for “hostname”.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/kdnsserviceflagssuppressunusable)*