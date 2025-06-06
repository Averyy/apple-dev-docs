# DNSServiceConstructFullName(_:_:_:_:)

**Framework**: dnssd  
**Kind**: func

Concatenates a three-part domain name (as returned by the above callbacks) into a properly-escaped full domain name.

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
func DNSServiceConstructFullName(_ fullName: UnsafeMutablePointer<CChar>!, _ service: UnsafePointer<CChar>!, _ regtype: UnsafePointer<CChar>!, _ domain: UnsafePointer<CChar>!) -> DNSServiceErrorType
```

#### Return Value

Returns [`kDNSServiceErr_NoError`](kdnsserviceerr_noerror.md) (0) on success, kDNSServiceErr_BadParam on error.

#### Discussion

Note that callbacks in the above functions ALREADY ESCAPE strings where necessary.

## Parameters

- `fullName`: A pointer to a buffer that where the resulting full domain name is to be written. The buffer must be   (1009) bytes in length to accommodate the longest legal domain name without buffer overrun.
- `service`: The service name - any dots or backslashes must NOT be escaped. May be NULL (to construct a PTR record name, e.g. “_ftp._tcp.apple.com.”).
- `regtype`: The service type followed by the protocol, separated by a dot (e.g. “_ftp._tcp”).
- `domain`: The domain name, e.g. “apple.com.”. Literal dots or backslashes, if any, must be escaped, e.g. “1st. Floor.apple.com.”


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsserviceconstructfullname(_:_:_:_:))*