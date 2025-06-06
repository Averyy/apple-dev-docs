# DNSServiceRegisterWithAttribute(_:_:_:_:_:_:_:_:_:_:_:_:_:)

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
func DNSServiceRegisterWithAttribute(_ sdRef: UnsafeMutablePointer<DNSServiceRef>?, _ flags: DNSServiceFlags, _ interfaceIndex: UInt32, _ name: UnsafePointer<CChar>?, _ regtype: UnsafePointer<CChar>?, _ domain: UnsafePointer<CChar>?, _ host: UnsafePointer<CChar>?, _ portInNetworkByteOrder: UInt16, _ txtLen: UInt16, _ txtRecord: UnsafeRawPointer?, _ attr: DNSServiceAttributeRef?, _ callBack: DNSServiceRegisterReply?, _ context: UnsafeMutableRawPointer?) -> DNSServiceErrorType
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
- [func DNSServiceSendQueuedRequests(DNSServiceRef?) -> DNSServiceErrorType](dnsservicesendqueuedrequests(_:).md)
- [func DNSServiceUpdateRecordWithAttribute(DNSServiceRef?, DNSRecordRef?, DNSServiceFlags, UInt16, UnsafeRawPointer?, UInt32, DNSServiceAttributeRef?) -> DNSServiceErrorType](dnsserviceupdaterecordwithattribute(_:_:_:_:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsserviceregisterwithattribute(_:_:_:_:_:_:_:_:_:_:_:_:_:))*