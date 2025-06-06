# kDNSServiceFlagsReturnIntermediates

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
var kDNSServiceFlagsReturnIntermediates: UInt32 { get }
```

#### Discussion

Flag for returning intermediate results. For example, if a query results in an authoritative NXDomain (name does not exist) then that result is returned to the client. However the query is not implicitly cancelled – it remains active and if the answer subsequently changes (e.g. because a VPN tunnel is subsequently established) then that positive result will still be returned to the client. Similarly, if a query results in a CNAME record, then in addition to following the CNAME referral, the intermediate CNAME result is also returned to the client. When this flag is not set, NXDomain errors are not returned, and CNAME records are followed silently without informing the client of the intermediate steps. (In earlier builds this flag was briefly called kDNSServiceFlagsReturnCNAME.)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsreturnintermediates)*