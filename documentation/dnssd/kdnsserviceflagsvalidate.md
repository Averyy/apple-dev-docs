# kDNSServiceFlagsValidate

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
var kDNSServiceFlagsValidate: UInt32 { get }
```

#### Discussion

This flag is meaningful in DNSServiceGetAddrInfo and DNSServiceQueryRecord. This is the ONLY flag that is both valid as an input to the APIs and also as an output through the callbacks in the APIs.

When this flag is passed to DNSServiceQueryRecord and DNSServiceGetAddrInfo to resolve unicast names, the response is validated using DNSSEC. The validation results are delivered using the flags field in the callback and kDNSServiceFlagsValidate is marked in the flags to indicate that DNSSEC status is also available. When the callback is called to deliver the query results, the validation results may or may not be available. If it is not delivered along with the results, the validation status is delivered when the validation completes.

When the validation results are delivered in the callback, it is indicated by marking the flags with kDNSServiceFlagsValidate and kDNSServiceFlagsAdd along with the DNSSEC status flags (described below) and a NULL sockaddr is returned for DNSServiceGetAddrInfo and zero length rdata is returned for DNSServiceQueryRecord. DNSSEC validation results are for the whole RRSet and not just individual records delivered in the callback. When kDNSServiceFlagsAdd is not set in the flags, applications should implicitly assume that the DNSSEC status of the RRSet that has been delivered up until that point is not valid anymore, till another callback is called with kDNSServiceFlagsAdd and kDNSServiceFlagsValidate.

The kDNSServiceFlagsValidate, kDNSServiceFlagsSecure, kDNSServiceFlagsInsecure, and kDNSServiceFlagsBogus flags indicate the status of the DNSSEC validation and marked in the flags field of the callback. When any of these four flags is set, kDNSServiceFlagsValidate is also set. To check the validation status, the other applicable output flags should be masked. See `kDNSServiceOutputFlags` below.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsvalidate)*