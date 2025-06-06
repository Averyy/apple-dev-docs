# dnssd Functions

**Framework**: dnssd

## Topics

### Functions
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
- [func DNSServiceUpdateRecordWithAttribute(DNSServiceRef?, DNSRecordRef?, DNSServiceFlags, UInt16, UnsafeRawPointer?, UInt32, DNSServiceAttributeRef?) -> DNSServiceErrorType](dnsserviceupdaterecordwithattribute(_:_:_:_:_:_:_:).md)

## See Also

- [DNS Service Discovery C](dns-service-discovery-c.md)
  See the Overview section above for header-level documentation.
- [dnssd Enumerations](dnssd-enumerations.md)
- [dnssd Data Types](dnssd-data-types.md)
- [dnssd Constants](dnssd-constants.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnssd-functions)*