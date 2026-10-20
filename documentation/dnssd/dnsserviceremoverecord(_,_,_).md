# DNSServiceRemoveRecord(_:_:_:)

**Framework**: dnssd  
**Kind**: func  
**Role**: Function

Removes a record previously added to a service record set via [`DNSServiceAddRecord(_:_:_:_:_:_:_:)`](./dnsserviceaddrecord%28_,_,_,_,_,_,_%29.md), or deregister an record registered individually via [`DNSServiceRegisterRecord(_:_:_:_:_:_:_:_:_:_:_:_:)`](./dnsserviceregisterrecord%28_,_,_,_,_,_,_,_,_,_,_,_%29.md).

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

```c
DNSServiceErrorType DNSServiceRemoveRecord(DNSServiceRef sdRef, DNSRecordRef RecordRef, DNSServiceFlags flags);
```

#### Return Value

Returns [`kDNSServiceErr_NoError`](./kdnsserviceerr_noerror.md) on success, otherwise returns an error code indicating the error that occurred.

## Parameters

- `sdRef`: A DNSServiceRef initialized by [`DNSServiceRegister(_:_:_:_:_:_:_:_:_:_:_:_:)`](./dnsserviceregister%28_,_,_,_,_,_,_,_,_,_,_,_%29.md) (if the record being removed was registered via [`DNSServiceAddRecord(_:_:_:_:_:_:_:)`](./dnsserviceaddrecord%28_,_,_,_,_,_,_%29.md)) or by [`DNSServiceCreateConnection(_:)`](./dnsservicecreateconnection%28_%29.md) (if the record being removed was registered via [`DNSServiceRegisterRecord(_:_:_:_:_:_:_:_:_:_:_:_:)`](./dnsserviceregisterrecord%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)).
- `RecordRef`: A DNSRecordRef initialized by a successful call to [`DNSServiceAddRecord(_:_:_:_:_:_:_:)`](./dnsserviceaddrecord%28_,_,_,_,_,_,_%29.md) or [`DNSServiceRegisterRecord(_:_:_:_:_:_:_:_:_:_:_:_:)`](./dnsserviceregisterrecord%28_,_,_,_,_,_,_,_,_,_,_,_%29.md).
- `flags`: Currently ignored, reserved for future use.

## See Also

### Service Registration
- [func DNSServiceAddRecord(DNSServiceRef!, UnsafeMutablePointer<DNSRecordRef?>!, DNSServiceFlags, UInt16, UInt16, UnsafeRawPointer!, UInt32) -> DNSServiceErrorType](./dnsserviceaddrecord%28_,_,_,_,_,_,_%29.md)
  Adds a record to a registered service.
- [func DNSServiceRegister(UnsafeMutablePointer<DNSServiceRef?>!, DNSServiceFlags, UInt32, UnsafePointer<CChar>!, UnsafePointer<CChar>!, UnsafePointer<CChar>!, UnsafePointer<CChar>!, UInt16, UInt16, UnsafeRawPointer!, DNSServiceRegisterReply!, UnsafeMutableRawPointer!) -> DNSServiceErrorType](./dnsserviceregister%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Registers a service.
- [func DNSServiceUpdateRecord(DNSServiceRef!, DNSRecordRef!, DNSServiceFlags, UInt16, UnsafeRawPointer!, UInt32) -> DNSServiceErrorType](./dnsserviceupdaterecord%28_,_,_,_,_,_%29.md)
  Updates a registered resource record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsserviceremoverecord(_:_:_:))*