# DNSServiceRemoveRecord(_:_:_:)

**Framework**: dnssd  
**Kind**: func

Removes a record previously added to a service record set via [`DNSServiceAddRecord(_:_:_:_:_:_:_:)`](dnsserviceaddrecord(_:_:_:_:_:_:_:).md), or deregister an record registered individually via [`DNSServiceRegisterRecord(_:_:_:_:_:_:_:_:_:_:_:_:)`](dnsserviceregisterrecord(_:_:_:_:_:_:_:_:_:_:_:_:).md).

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
func DNSServiceRemoveRecord(_ sdRef: DNSServiceRef!, _ RecordRef: DNSRecordRef!, _ flags: DNSServiceFlags) -> DNSServiceErrorType
```

#### Return Value

Returns [`kDNSServiceErr_NoError`](kdnsserviceerr_noerror.md) on success, otherwise returns an error code indicating the error that occurred.

## Parameters

- `sdRef`: A DNSServiceRef initialized by   (if the record being removed was registered via  ) or by   (if the record being removed was registered via  ).
- `RecordRef`: A DNSRecordRef initialized by a successful call to   or  .
- `flags`: Currently ignored, reserved for future use.

## See Also

- [func DNSServiceAddRecord(DNSServiceRef!, UnsafeMutablePointer<DNSRecordRef?>!, DNSServiceFlags, UInt16, UInt16, UnsafeRawPointer!, UInt32) -> DNSServiceErrorType](dnsserviceaddrecord(_:_:_:_:_:_:_:).md)
  Adds a record to a registered service.
- [func DNSServiceRegister(UnsafeMutablePointer<DNSServiceRef?>!, DNSServiceFlags, UInt32, UnsafePointer<CChar>!, UnsafePointer<CChar>!, UnsafePointer<CChar>!, UnsafePointer<CChar>!, UInt16, UInt16, UnsafeRawPointer!, DNSServiceRegisterReply!, UnsafeMutableRawPointer!) -> DNSServiceErrorType](dnsserviceregister(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Registers a service.
- [func DNSServiceUpdateRecord(DNSServiceRef!, DNSRecordRef!, DNSServiceFlags, UInt16, UnsafeRawPointer!, UInt32) -> DNSServiceErrorType](dnsserviceupdaterecord(_:_:_:_:_:_:).md)
  Updates a registered resource record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsserviceremoverecord(_:_:_:))*