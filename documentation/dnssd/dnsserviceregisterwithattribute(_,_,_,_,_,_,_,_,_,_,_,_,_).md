# DNSServiceRegisterWithAttribute(_:_:_:_:_:_:_:_:_:_:_:_:_:)

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
func DNSServiceRegisterWithAttribute(_ sdRef: UnsafeMutablePointer<DNSServiceRef>?, _ flags: DNSServiceFlags, _ interfaceIndex: UInt32, _ name: UnsafePointer<CChar>?, _ regtype: UnsafePointer<CChar>?, _ domain: UnsafePointer<CChar>?, _ host: UnsafePointer<CChar>?, _ portInNetworkByteOrder: UInt16, _ txtLen: UInt16, _ txtRecord: UnsafeRawPointer?, _ attr: DNSServiceAttributeRef?, _ callBack: DNSServiceRegisterReply?, _ context: UnsafeMutableRawPointer?) -> DNSServiceErrorType
```

```c
DNSServiceErrorType DNSServiceRegisterWithAttribute(DNSServiceRef*sdRef, DNSServiceFlags flags, uint32_t interfaceIndex, const char *name, const char *regtype, const char *domain, const char *host, uint16_t portInNetworkByteOrder, uint16_t txtLen, const void *txtRecord, DNSServiceAttributeRef const attr, DNSServiceRegisterReply callBack, void *context);
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
- [func DNSServiceSendQueuedRequests(DNSServiceRef?) -> DNSServiceErrorType](./dnsservicesendqueuedrequests%28_%29.md)
- [func DNSServiceUpdateRecordWithAttribute(DNSServiceRef?, DNSRecordRef?, DNSServiceFlags, UInt16, UnsafeRawPointer?, UInt32, DNSServiceAttributeRef?) -> DNSServiceErrorType](./dnsserviceupdaterecordwithattribute%28_,_,_,_,_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsserviceregisterwithattribute(_:_:_:_:_:_:_:_:_:_:_:_:_:))*