# kDNSServiceFlagsTimeout

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
var kDNSServiceFlagsTimeout: UInt32 { get }
```

#### Discussion

When passed to [`DNSServiceQueryRecord(_:_:_:_:_:_:_:_:)`](dnsservicequeryrecord(_:_:_:_:_:_:_:_:).md) or [`DNSServiceGetAddrInfo(_:_:_:_:_:_:_:)`](dnsservicegetaddrinfo(_:_:_:_:_:_:_:).md), the query is stopped after a certain number of seconds have elapsed. The time at which the query is stopped is determined by the system and cannot be configured by the user. The query is stopped irrespective of whether a response was given earlier or not. When the query is stopped, the callback is called with an error code of kDNSServiceErr_Timeout and a NULL sockaddr is returned for [`DNSServiceGetAddrInfo(_:_:_:_:_:_:_:)`](dnsservicegetaddrinfo(_:_:_:_:_:_:_:).md) and zero length rdata is returned for [`DNSServiceQueryRecord(_:_:_:_:_:_:_:_:)`](dnsservicequeryrecord(_:_:_:_:_:_:_:_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/kdnsserviceflagstimeout)*