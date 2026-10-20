# DNSServiceRegisterRecord(_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: dnssd  
**Kind**: func  
**Role**: Function

Registers an individual resource record on a connected DNSServiceRef.

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
func DNSServiceRegisterRecord(_ sdRef: DNSServiceRef!, _ RecordRef: UnsafeMutablePointer<DNSRecordRef?>!, _ flags: DNSServiceFlags, _ interfaceIndex: UInt32, _ fullname: UnsafePointer<CChar>!, _ rrtype: UInt16, _ rrclass: UInt16, _ rdlen: UInt16, _ rdata: UnsafeRawPointer!, _ ttl: UInt32, _ callBack: DNSServiceRegisterRecordReply!, _ context: UnsafeMutableRawPointer!) -> DNSServiceErrorType
```

```c
DNSServiceErrorType DNSServiceRegisterRecord(DNSServiceRef sdRef, DNSRecordRef*RecordRef, DNSServiceFlags flags, uint32_t interfaceIndex, const char *fullname, uint16_t rrtype, uint16_t rrclass, uint16_t rdlen, const void *rdata, uint32_t ttl, DNSServiceRegisterRecordReply callBack, void *context);
```

#### Return Value

Returns [`kDNSServiceErr_NoError`](./kdnsserviceerr_noerror.md) on success (any subsequent, asynchronous errors are delivered to the callback), otherwise returns an error code indicating the error that occurred (the callback is never invoked and the DNSRecordRef is not initialized).

#### Discussion

Note that name conflicts occurring for records registered via this call must be handled by the client in the callback.

## Parameters

- `sdRef`: A DNSServiceRef initialized by [`DNSServiceCreateConnection(_:)`](./dnsservicecreateconnection%28_%29.md).
- `RecordRef`: A pointer to an uninitialized DNSRecordRef. Upon succesfull completion of this call, this ref may be passed to [`DNSServiceUpdateRecord(_:_:_:_:_:_:)`](./dnsserviceupdaterecord%28_,_,_,_,_,_%29.md) or [`DNSServiceRemoveRecord(_:_:_:)`](./dnsserviceremoverecord%28_,_,_%29.md). (To deregister ALL records registered on a single connected DNSServiceRef and deallocate each of their corresponding DNSServiceRecordRefs, call [`DNSServiceRefDeallocate(_:)`](./dnsservicerefdeallocate%28_%29.md)).
- `flags`: Possible values are kDNSServiceFlagsShared or kDNSServiceFlagsUnique (see flag type definitions for details).
- `interfaceIndex`: If non-zero, specifies the interface on which to register the record (the index for a given interface is determined via the if_nametoindex() family of calls.) Passing 0 causes the record to be registered on all interfaces. See “Constants for specifying an interface index” for more details.
- `fullname`: The full domain name of the resource record.
- `rrtype`: The numerical type of the resource record (e.g. kDNSServiceType_PTR, kDNSServiceType_SRV, and so on).
- `rrclass`: The class of the resource record (usually [`kDNSServiceClass_IN`](./kdnsserviceclass_in.md))
- `rdlen`: Length, in bytes, of the rdata.
- `rdata`: A pointer to the raw rdata, as it is to appear in the DNS record.
- `ttl`: The time to live of the resource record, in seconds. Most clients should pass 0 to indicate that the system should select a sensible default value.
- `callBack`: The function to be called when a result is found, or if the call asynchronously fails (e.g. because of a name conflict.)
- `context`: An application context pointer which is passed to the callback function (may be NULL).

## See Also

### Special Purpose Calls
- [func DNSServiceCreateConnection(UnsafeMutablePointer<DNSServiceRef?>!) -> DNSServiceErrorType](./dnsservicecreateconnection%28_%29.md)
  Creates a connection to the daemon, allowing efficient registration of multiple individual records.
- [func DNSServiceReconfirmRecord(DNSServiceFlags, UInt32, UnsafePointer<CChar>!, UInt16, UInt16, UInt16, UnsafeRawPointer!) -> DNSServiceErrorType](./dnsservicereconfirmrecord%28_,_,_,_,_,_,_%29.md)
  Instructs the daemon to verify the validity of a resource record that appears to be out of date (for example, because TCP connection to a service’s target failed).
- [func PeerConnectionRelease(DNSServiceFlags, UnsafePointer<CChar>!, UnsafePointer<CChar>!, UnsafePointer<CChar>!) -> DNSServiceErrorType](./peerconnectionrelease%28_,_,_,_%29.md)
  Releases P2P connection resources associated with the service instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsserviceregisterrecord(_:_:_:_:_:_:_:_:_:_:_:_:))*