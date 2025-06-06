# kDNSServiceFlagsForceMulticast

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
var kDNSServiceFlagsForceMulticast: UInt32 { get }
```

#### Discussion

Flag for signifying that a query or registration should be performed exclusively via multicast DNS, even for a name in a domain (e.g. foo.apple.com.) that would normally imply unicast DNS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsforcemulticast)*