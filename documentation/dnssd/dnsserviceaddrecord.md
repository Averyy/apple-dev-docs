# DNSServiceAddRecord(_:_:_:_:_:_:_:)

**Framework**: dnssd  
**Kind**: func

Adds a record to a registered service.

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
func DNSServiceAddRecord(_ sdRef: DNSServiceRef!, _ RecordRef: UnsafeMutablePointer<DNSRecordRef?>!, _ flags: DNSServiceFlags, _ rrtype: UInt16, _ rdlen: UInt16, _ rdata: UnsafeRawPointer!, _ ttl: UInt32) -> DNSServiceErrorType
```

#### Return Value

Returns [`kDNSServiceErr_NoError`](kdnsserviceerr_noerror.md) on success, otherwise returns an error code indicating the error that occurred (the RecordRef is not initialized).

#### Discussion

The name of the record will be the same as the registered service’s name. The record can later be updated or deregistered by passing the RecordRef initialized by this function to [`DNSServiceUpdateRecord(_:_:_:_:_:_:)`](dnsserviceupdaterecord(_:_:_:_:_:_:).md) or [`DNSServiceRemoveRecord(_:_:_:)`](dnsserviceremoverecord(_:_:_:).md).

Note that the DNSServiceAddRecord/UpdateRecord/RemoveRecord are *NOT* thread-safe with respect to a single DNSServiceRef. If you plan to have multiple threads in your program simultaneously add, update, or remove records from the same DNSServiceRef, then it’s the caller’s responsibility to use a mutext lock or take similar appropriate precautions to serialize those calls.

## Parameters

- `sdRef`: A DNSServiceRef initialized by  .
- `RecordRef`: A pointer to an uninitialized DNSRecordRef. Upon succesfull completion of this call, this ref may be passed to   or  . If the above DNSServiceRef is passed to  , RecordRef is also invalidated and may not be used further.
- `flags`: Currently ignored, reserved for future use.
- `rrtype`: The type of the record (e.g. kDNSServiceType_TXT, kDNSServiceType_SRV, and so on).
- `rdlen`: The length, in bytes, of the rdata.
- `rdata`: The raw rdata to be contained in the added resource record.
- `ttl`: The time to live of the resource record, in seconds. Most clients should pass 0 to indicate that the system should select a sensible default value.

## See Also

- [func DNSServiceRegister(UnsafeMutablePointer<DNSServiceRef?>!, DNSServiceFlags, UInt32, UnsafePointer<CChar>!, UnsafePointer<CChar>!, UnsafePointer<CChar>!, UnsafePointer<CChar>!, UInt16, UInt16, UnsafeRawPointer!, DNSServiceRegisterReply!, UnsafeMutableRawPointer!) -> DNSServiceErrorType](dnsserviceregister(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Registers a service.
- [func DNSServiceRemoveRecord(DNSServiceRef!, DNSRecordRef!, DNSServiceFlags) -> DNSServiceErrorType](dnsserviceremoverecord(_:_:_:).md)
  Removes a record previously added to a service record set via [`DNSServiceAddRecord(_:_:_:_:_:_:_:)`](dnsserviceaddrecord(_:_:_:_:_:_:_:).md), or deregister an record registered individually via [`DNSServiceRegisterRecord(_:_:_:_:_:_:_:_:_:_:_:_:)`](dnsserviceregisterrecord(_:_:_:_:_:_:_:_:_:_:_:_:).md).
- [func DNSServiceUpdateRecord(DNSServiceRef!, DNSRecordRef!, DNSServiceFlags, UInt16, UnsafeRawPointer!, UInt32) -> DNSServiceErrorType](dnsserviceupdaterecord(_:_:_:_:_:_:).md)
  Updates a registered resource record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsserviceaddrecord(_:_:_:_:_:_:_:))*