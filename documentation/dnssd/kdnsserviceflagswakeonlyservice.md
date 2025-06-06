# kDNSServiceFlagsWakeOnlyService

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
var kDNSServiceFlagsWakeOnlyService: UInt32 { get }
```

#### Discussion

This flag is meaningful only in DNSServiceRegister. When set, the service is not registered with a sleep proxy server during sleep.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/kdnsserviceflagswakeonlyservice)*