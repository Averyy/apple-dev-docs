# DNSServiceUpdateRecord(_:_:_:_:_:_:)

**Framework**: dnssd  
**Kind**: func

Updates a registered resource record.

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
func DNSServiceUpdateRecord(_ sdRef: DNSServiceRef!, _ recordRef: DNSRecordRef!, _ flags: DNSServiceFlags, _ rdlen: UInt16, _ rdata: UnsafeRawPointer!, _ ttl: UInt32) -> DNSServiceErrorType
```

#### Return Value

Returns [`kDNSServiceErr_NoError`](kdnsserviceerr_noerror.md) on success, otherwise returns an error code indicating the error that occurred.

#### Discussion

The record must either be:

- The primary txt record of a service registered via [`DNSServiceRegister(_:_:_:_:_:_:_:_:_:_:_:_:)`](dnsserviceregister(_:_:_:_:_:_:_:_:_:_:_:_:).md)
- A record added to a registered service via [`DNSServiceAddRecord(_:_:_:_:_:_:_:)`](dnsserviceaddrecord(_:_:_:_:_:_:_:).md)
- An individual record registered by [`DNSServiceRegisterRecord(_:_:_:_:_:_:_:_:_:_:_:_:)`](dnsserviceregisterrecord(_:_:_:_:_:_:_:_:_:_:_:_:).md)

## Parameters

- `sdRef`: A DNSServiceRef that was initialized by   or  .
- `recordRef`: A DNSRecordRef initialized by  , or NULL to update the service’s primary txt record.
- `flags`: Currently ignored, reserved for future use.
- `rdlen`: The length, in bytes, of the new rdata.
- `rdata`: The new rdata to be contained in the updated resource record.
- `ttl`: The time to live of the updated resource record, in seconds. Most clients should pass 0 to indicate that the system should select a sensible default value.

## See Also

- [func DNSServiceAddRecord(DNSServiceRef!, UnsafeMutablePointer<DNSRecordRef?>!, DNSServiceFlags, UInt16, UInt16, UnsafeRawPointer!, UInt32) -> DNSServiceErrorType](dnsserviceaddrecord(_:_:_:_:_:_:_:).md)
  Adds a record to a registered service.
- [func DNSServiceRegister(UnsafeMutablePointer<DNSServiceRef?>!, DNSServiceFlags, UInt32, UnsafePointer<CChar>!, UnsafePointer<CChar>!, UnsafePointer<CChar>!, UnsafePointer<CChar>!, UInt16, UInt16, UnsafeRawPointer!, DNSServiceRegisterReply!, UnsafeMutableRawPointer!) -> DNSServiceErrorType](dnsserviceregister(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Registers a service.
- [func DNSServiceRemoveRecord(DNSServiceRef!, DNSRecordRef!, DNSServiceFlags) -> DNSServiceErrorType](dnsserviceremoverecord(_:_:_:).md)
  Removes a record previously added to a service record set via [`DNSServiceAddRecord(_:_:_:_:_:_:_:)`](dnsserviceaddrecord(_:_:_:_:_:_:_:).md), or deregister an record registered individually via [`DNSServiceRegisterRecord(_:_:_:_:_:_:_:_:_:_:_:_:)`](dnsserviceregisterrecord(_:_:_:_:_:_:_:_:_:_:_:_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsserviceupdaterecord(_:_:_:_:_:_:))*