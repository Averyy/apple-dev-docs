# DNSServiceAttributeSetHostKeyHash(_:_:)

**Framework**: dnssd  
**Kind**: func

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func DNSServiceAttributeSetHostKeyHash(_ attr: DNSServiceAttributeRef, _ hostkeyhash: UInt32) -> DNSServiceErrorType
```

## See Also

- [func DNSServiceSleepKeepalive(UnsafeMutablePointer<DNSServiceRef?>!, DNSServiceFlags, Int32, UInt32, DNSServiceSleepKeepaliveReply!, UnsafeMutableRawPointer!) -> DNSServiceErrorType](dnsservicesleepkeepalive(_:_:_:_:_:_:).md)
- [func DNSServiceAttributeCreate() -> DNSServiceAttributeRef?](dnsserviceattributecreate().md)
- [func DNSServiceAttributeDeallocate(DNSServiceAttributeRef)](dnsserviceattributedeallocate(_:).md)
- [func DNSServiceAttributeSetAAAAPolicy(DNSServiceAttributeRef, DNSServiceAAAAPolicy) -> DNSServiceErrorType](dnsserviceattributesetaaaapolicy(_:_:).md)
- [func DNSServiceAttributeSetTimestamp(DNSServiceAttributeRef, UInt32) -> DNSServiceErrorType](dnsserviceattributesettimestamp(_:_:).md)
- [func DNSServiceQueryRecordWithAttribute(UnsafeMutablePointer<DNSServiceRef>?, DNSServiceFlags, UInt32, UnsafePointer<CChar>?, UInt16, UInt16, OpaquePointer?, DNSServiceQueryRecordReply?, UnsafeMutableRawPointer?) -> DNSServiceErrorType](dnsservicequeryrecordwithattribute(_:_:_:_:_:_:_:_:_:).md)
- [func DNSServiceRegisterRecordWithAttribute(DNSServiceRef?, UnsafeMutablePointer<DNSRecordRef>?, DNSServiceFlags, UInt32, UnsafePointer<CChar>?, UInt16, UInt16, UInt16, UnsafeRawPointer?, UInt32, DNSServiceAttributeRef?, DNSServiceRegisterRecordReply?, UnsafeMutableRawPointer?) -> DNSServiceErrorType](dnsserviceregisterrecordwithattribute(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func DNSServiceRegisterWithAttribute(UnsafeMutablePointer<DNSServiceRef>?, DNSServiceFlags, UInt32, UnsafePointer<CChar>?, UnsafePointer<CChar>?, UnsafePointer<CChar>?, UnsafePointer<CChar>?, UInt16, UInt16, UnsafeRawPointer?, DNSServiceAttributeRef?, DNSServiceRegisterReply?, UnsafeMutableRawPointer?) -> DNSServiceErrorType](dnsserviceregisterwithattribute(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func DNSServiceSendQueuedRequests(DNSServiceRef?) -> DNSServiceErrorType](dnsservicesendqueuedrequests(_:).md)
- [func DNSServiceUpdateRecordWithAttribute(DNSServiceRef?, DNSRecordRef?, DNSServiceFlags, UInt16, UnsafeRawPointer?, UInt32, DNSServiceAttributeRef?) -> DNSServiceErrorType](dnsserviceupdaterecordwithattribute(_:_:_:_:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsserviceattributesethostkeyhash(_:_:))*