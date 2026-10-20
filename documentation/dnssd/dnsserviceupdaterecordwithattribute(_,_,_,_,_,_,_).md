# DNSServiceUpdateRecordWithAttribute(_:_:_:_:_:_:_:)

**Framework**: dnssd  
**Kind**: func  
**Role**: Function

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

```c
DNSServiceErrorType DNSServiceUpdateRecordWithAttribute(DNSServiceRef sdRef, DNSRecordRef recordRef, DNSServiceFlags flags, uint16_t rdlen, const void *rdata, uint32_t ttl, DNSServiceAttributeRef const attr);
```

## See Also

### Functions
- [func DNSServiceSleepKeepalive(UnsafeMutablePointer<DNSServiceRef?>!, DNSServiceFlags, Int32, UInt32, DNSServiceSleepKeepaliveReply!, UnsafeMutableRawPointer!) -> DNSServiceErrorType](./dnsservicesleepkeepalive%28_,_,_,_,_,_%29.md)
- [func DNSServiceAttributeCreate() -> DNSServiceAttributeRef?](./dnsserviceattributecreate%28%29.md)
- [func DNSServiceAttributeDeallocate(DNSServiceAttributeRef)](./dnsserviceattributedeallocate%28_%29.md)
- [func DNSServiceAttributeSetAAAAPolicy(DNSServiceAttributeRef, DNSServiceAAAAPolicy) -> DNSServiceErrorType](./dnsserviceattributesetaaaapolicy%28_,_%29.md)
- [func DNSServiceAttributeSetHostKeyHash(DNSServiceAttributeRef, UInt32) -> DNSServiceErrorType](./dnsserviceattributesethostkeyhash%28_,_%29.md)
- [func DNSServiceAttributeSetTimestamp(DNSServiceAttributeRef, UInt32) -> DNSServiceErrorType](./dnsserviceattributesettimestamp%28_,_%29.md)
- [func DNSServiceQueryRecordWithAttribute(UnsafeMutablePointer<DNSServiceRef>?, DNSServiceFlags, UInt32, UnsafePointer<CChar>?, UInt16, UInt16, OpaquePointer?, DNSServiceQueryRecordReply?, UnsafeMutableRawPointer?) -> DNSServiceErrorType](./dnsservicequeryrecordwithattribute%28_,_,_,_,_,_,_,_,_%29.md)
- [func DNSServiceRegisterRecordWithAttribute(DNSServiceRef?, UnsafeMutablePointer<DNSRecordRef>?, DNSServiceFlags, UInt32, UnsafePointer<CChar>?, UInt16, UInt16, UInt16, UnsafeRawPointer?, UInt32, DNSServiceAttributeRef?, DNSServiceRegisterRecordReply?, UnsafeMutableRawPointer?) -> DNSServiceErrorType](./dnsserviceregisterrecordwithattribute%28_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
- [func DNSServiceRegisterWithAttribute(UnsafeMutablePointer<DNSServiceRef>?, DNSServiceFlags, UInt32, UnsafePointer<CChar>?, UnsafePointer<CChar>?, UnsafePointer<CChar>?, UnsafePointer<CChar>?, UInt16, UInt16, UnsafeRawPointer?, DNSServiceAttributeRef?, DNSServiceRegisterReply?, UnsafeMutableRawPointer?) -> DNSServiceErrorType](./dnsserviceregisterwithattribute%28_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
- [func DNSServiceSendQueuedRequests(DNSServiceRef?) -> DNSServiceErrorType](./dnsservicesendqueuedrequests%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsserviceupdaterecordwithattribute(_:_:_:_:_:_:_:))*