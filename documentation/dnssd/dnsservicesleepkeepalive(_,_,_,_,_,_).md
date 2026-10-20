# DNSServiceSleepKeepalive(_:_:_:_:_:_:)

**Framework**: dnssd  
**Kind**: func  
**Role**: Function

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
func DNSServiceSleepKeepalive(_ sdRef: UnsafeMutablePointer<DNSServiceRef?>!, _ flags: DNSServiceFlags, _ fd: Int32, _ timeout: UInt32, _ callBack: DNSServiceSleepKeepaliveReply!, _ context: UnsafeMutableRawPointer!) -> DNSServiceErrorType
```

```c
DNSServiceErrorType DNSServiceSleepKeepalive(DNSServiceRef*sdRef, DNSServiceFlags flags, int fd, unsigned int timeout, DNSServiceSleepKeepaliveReply callBack, void *context);
```

## See Also

### Functions
- [func DNSServiceAttributeCreate() -> DNSServiceAttributeRef?](./dnsserviceattributecreate%28%29.md)
- [func DNSServiceAttributeDeallocate(DNSServiceAttributeRef)](./dnsserviceattributedeallocate%28_%29.md)
- [func DNSServiceAttributeSetAAAAPolicy(DNSServiceAttributeRef, DNSServiceAAAAPolicy) -> DNSServiceErrorType](./dnsserviceattributesetaaaapolicy%28_,_%29.md)
- [func DNSServiceAttributeSetHostKeyHash(DNSServiceAttributeRef, UInt32) -> DNSServiceErrorType](./dnsserviceattributesethostkeyhash%28_,_%29.md)
- [func DNSServiceAttributeSetTimestamp(DNSServiceAttributeRef, UInt32) -> DNSServiceErrorType](./dnsserviceattributesettimestamp%28_,_%29.md)
- [func DNSServiceQueryRecordWithAttribute(UnsafeMutablePointer<DNSServiceRef>?, DNSServiceFlags, UInt32, UnsafePointer<CChar>?, UInt16, UInt16, OpaquePointer?, DNSServiceQueryRecordReply?, UnsafeMutableRawPointer?) -> DNSServiceErrorType](./dnsservicequeryrecordwithattribute%28_,_,_,_,_,_,_,_,_%29.md)
- [func DNSServiceRegisterRecordWithAttribute(DNSServiceRef?, UnsafeMutablePointer<DNSRecordRef>?, DNSServiceFlags, UInt32, UnsafePointer<CChar>?, UInt16, UInt16, UInt16, UnsafeRawPointer?, UInt32, DNSServiceAttributeRef?, DNSServiceRegisterRecordReply?, UnsafeMutableRawPointer?) -> DNSServiceErrorType](./dnsserviceregisterrecordwithattribute%28_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
- [func DNSServiceRegisterWithAttribute(UnsafeMutablePointer<DNSServiceRef>?, DNSServiceFlags, UInt32, UnsafePointer<CChar>?, UnsafePointer<CChar>?, UnsafePointer<CChar>?, UnsafePointer<CChar>?, UInt16, UInt16, UnsafeRawPointer?, DNSServiceAttributeRef?, DNSServiceRegisterReply?, UnsafeMutableRawPointer?) -> DNSServiceErrorType](./dnsserviceregisterwithattribute%28_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
- [func DNSServiceSendQueuedRequests(DNSServiceRef?) -> DNSServiceErrorType](./dnsservicesendqueuedrequests%28_%29.md)
- [func DNSServiceUpdateRecordWithAttribute(DNSServiceRef?, DNSRecordRef?, DNSServiceFlags, UInt16, UnsafeRawPointer?, UInt32, DNSServiceAttributeRef?) -> DNSServiceErrorType](./dnsserviceupdaterecordwithattribute%28_,_,_,_,_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsservicesleepkeepalive(_:_:_:_:_:_:))*