# DNSServiceUpdateRecordWithAttribute(_:_:_:_:_:_:_:)

**Framework**: dnssd  
**Kind**: func

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func DNSServiceUpdateRecordWithAttribute(_ sdRef: DNSServiceRef?, _ recordRef: DNSRecordRef?, _ flags: DNSServiceFlags, _ rdlen: UInt16, _ rdata: UnsafeRawPointer?, _ ttl: UInt32, _ attr: DNSServiceAttributeRef?) -> DNSServiceErrorType
```

## See Also

- [func DNSServiceSleepKeepalive(UnsafeMutablePointer<DNSServiceRef?>!, DNSServiceFlags, Int32, UInt32, DNSServiceSleepKeepaliveReply!, UnsafeMutableRawPointer!) -> DNSServiceErrorType](dnsservicesleepkeepalive(_:_:_:_:_:_:).md)
- [func DNSServiceAttributeCreate() -> DNSServiceAttributeRef?](dnsserviceattributecreate().md)
- [func DNSServiceAttributeDeallocate(DNSServiceAttributeRef)](dnsserviceattributedeallocate(_:).md)
- [func DNSServiceAttributeSetAAAAPolicy(DNSServiceAttributeRef, DNSServiceAAAAPolicy) -> DNSServiceErrorType](dnsserviceattributesetaaaapolicy(_:_:).md)
- [func DNSServiceAttributeSetHostKeyHash(DNSServiceAttributeRef, UInt32) -> DNSServiceErrorType](dnsserviceattributesethostkeyhash(_:_:).md)
- [func DNSServiceAttributeSetTimestamp(DNSServiceAttributeRef, UInt32) -> DNSServiceErrorType](dnsserviceattributesettimestamp(_:_:).md)
- [func DNSServiceQueryRecordWithAttribute(UnsafeMutablePointer<DNSServiceRef>?, DNSServiceFlags, UInt32, UnsafePointer<CChar>?, UInt16, UInt16, OpaquePointer?, DNSServiceQueryRecordReply?, UnsafeMutableRawPointer?) -> DNSServiceErrorType](dnsservicequeryrecordwithattribute(_:_:_:_:_:_:_:_:_:).md)
- [func DNSServiceRegisterRecordWithAttribute(DNSServiceRef?, UnsafeMutablePointer<DNSRecordRef>?, DNSServiceFlags, UInt32, UnsafePointer<CChar>?, UInt16, UInt16, UInt16, UnsafeRawPointer?, UInt32, DNSServiceAttributeRef?, DNSServiceRegisterRecordReply?, UnsafeMutableRawPointer?) -> DNSServiceErrorType](dnsserviceregisterrecordwithattribute(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func DNSServiceRegisterWithAttribute(UnsafeMutablePointer<DNSServiceRef>?, DNSServiceFlags, UInt32, UnsafePointer<CChar>?, UnsafePointer<CChar>?, UnsafePointer<CChar>?, UnsafePointer<CChar>?, UInt16, UInt16, UnsafeRawPointer?, DNSServiceAttributeRef?, DNSServiceRegisterReply?, UnsafeMutableRawPointer?) -> DNSServiceErrorType](dnsserviceregisterwithattribute(_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
- [func DNSServiceSendQueuedRequests(DNSServiceRef?) -> DNSServiceErrorType](dnsservicesendqueuedrequests(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsserviceupdaterecordwithattribute(_:_:_:_:_:_:_:))*