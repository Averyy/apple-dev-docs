# DNSServiceSleepKeepaliveReply

**Framework**: dnssd  
**Kind**: typealias  
**Role**: Type Alias

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
typealias DNSServiceSleepKeepaliveReply = (DNSServiceRef?, DNSServiceErrorType, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*)(struct _DNSServiceRef_t *, int, void *) DNSServiceSleepKeepaliveReply;
```

## See Also

### Data Types
- [struct CompileTimeAssertionChecks_DNS_SD](./compiletimeassertionchecks_dns_sd.md)
- [typealias DNSRecordRef](./dnsrecordref.md)
- [typealias DNSServiceRef](./dnsserviceref.md)
- [typealias dnssd_sock_t](./dnssd_sock_t.md)
- [typealias DNSServiceAttributeRef](./dnsserviceattributeref.md)
- [DNSServiceAttribute](./dnsserviceattribute.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsservicesleepkeepalivereply)*