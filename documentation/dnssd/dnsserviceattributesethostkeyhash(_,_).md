# DNSServiceAttributeSetHostKeyHash(_:_:)

**Framework**: dnssd  
**Kind**: func  
**Role**: Function

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

```c
DNSServiceErrorType DNSServiceAttributeSetHostKeyHash(DNSServiceAttributeRef attr, uint32_t hostkeyhash);
```

## See Also

### Functions
- [func DNSServiceSleepKeepalive(UnsafeMutablePointer<DNSServiceRef?>!, DNSServiceFlags, Int32, UInt32, DNSServiceSleepKeepaliveReply!, UnsafeMutableRawPointer!) -> DNSServiceErrorType](./dnsservicesleepkeepalive%28_,_,_,_,_,_%29.md)
- [func DNSServiceAttributeCreate() -> DNSServiceAttributeRef?](./dnsserviceattributecreate%28%29.md)
- [func DNSServiceAttributeDeallocate(DNSServiceAttributeRef)](./dnsserviceattributedeallocate%28_%29.md)
- [func DNSServiceAttributeSetAAAAPolicy(DNSServiceAttributeRef, DNSServiceAAAAPolicy) -> DNSServiceErrorType](./dnsserviceattributesetaaaapolicy%28_,_%29.md)
- [func DNSServiceAttributeSetTimestamp(DNSServiceAttributeRef, UInt32) -> DNSServiceErrorType](./dnsserviceattributesettimestamp%28_,_%29.md)
- [func DNSServiceQueryRecordWithAttribute(UnsafeMutablePointer<DNSServiceRef>?, DNSServiceFlags, UInt32, UnsafePointer<CChar>?, UInt16, UInt16, OpaquePointer?, DNSServiceQueryRecordReply?, UnsafeMutableRawPointer?) -> DNSServiceErrorType](./dnsservicequeryrecordwithattribute%28_,_,_,_,_,_,_,_,_%29.md)
- [func DNSServiceRegisterRecordWithAttribute(DNSServiceRef?, UnsafeMutablePointer<DNSRecordRef>?, DNSServiceFlags, UInt32, UnsafePointer<CChar>?, UInt16, UInt16, UInt16, UnsafeRawPointer?, UInt32, DNSServiceAttributeRef?, DNSServiceRegisterRecordReply?, UnsafeMutableRawPointer?) -> DNSServiceErrorType](./dnsserviceregisterrecordwithattribute%28_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
- [func DNSServiceRegisterWithAttribute(UnsafeMutablePointer<DNSServiceRef>?, DNSServiceFlags, UInt32, UnsafePointer<CChar>?, UnsafePointer<CChar>?, UnsafePointer<CChar>?, UnsafePointer<CChar>?, UInt16, UInt16, UnsafeRawPointer?, DNSServiceAttributeRef?, DNSServiceRegisterReply?, UnsafeMutableRawPointer?) -> DNSServiceErrorType](./dnsserviceregisterwithattribute%28_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
- [func DNSServiceSendQueuedRequests(DNSServiceRef?) -> DNSServiceErrorType](./dnsservicesendqueuedrequests%28_%29.md)
- [func DNSServiceUpdateRecordWithAttribute(DNSServiceRef?, DNSRecordRef?, DNSServiceFlags, UInt16, UnsafeRawPointer?, UInt32, DNSServiceAttributeRef?) -> DNSServiceErrorType](./dnsserviceupdaterecordwithattribute%28_,_,_,_,_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsserviceattributesethostkeyhash(_:_:))*