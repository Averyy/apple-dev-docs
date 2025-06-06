# DNSServiceReconfirmRecord(_:_:_:_:_:_:_:)

**Framework**: dnssd  
**Kind**: func

Instructs the daemon to verify the validity of a resource record that appears to be out of date (for example, because TCP connection to a service’s target failed).

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
func DNSServiceReconfirmRecord(_ flags: DNSServiceFlags, _ interfaceIndex: UInt32, _ fullname: UnsafePointer<CChar>!, _ rrtype: UInt16, _ rrclass: UInt16, _ rdlen: UInt16, _ rdata: UnsafeRawPointer!) -> DNSServiceErrorType
```

#### Discussion

Causes the record to be flushed from the daemon’s cache (as well as all other daemons’ caches on the network) if the record is determined to be invalid.

> ❗ **Important**:  Use this routine conservatively. Reconfirming a record necessarily consumes network bandwidth, so this should not be done indiscriminately.

 Use this routine conservatively. Reconfirming a record necessarily consumes network bandwidth, so this should not be done indiscriminately.

## Parameters

- `flags`: Not currently used.
- `interfaceIndex`: Specifies the interface of the record in question. The caller must specify the interface. This API (by design) causes increased network traffic, so it requires the caller to be precise about which record should be reconfirmed. It is not possible to pass zero for the interface index to perform a “wildcard” reconfirmation, where *all* matching records are reconfirmed.
- `fullname`: The resource record’s full domain name.
- `rrtype`: The resource record’s type (e.g. kDNSServiceType_PTR, kDNSServiceType_SRV, and so on).
- `rrclass`: The class of the resource record (usually  ).
- `rdlen`: The length, in bytes, of the resource record rdata.
- `rdata`: The raw rdata of the resource record.

## See Also

- [func DNSServiceCreateConnection(UnsafeMutablePointer<DNSServiceRef?>!) -> DNSServiceErrorType](dnsservicecreateconnection(_:).md)
  Creates a connection to the daemon, allowing efficient registration of multiple individual records.
- [func DNSServiceRegisterRecord(DNSServiceRef!, UnsafeMutablePointer<DNSRecordRef?>!, DNSServiceFlags, UInt32, UnsafePointer<CChar>!, UInt16, UInt16, UInt16, UnsafeRawPointer!, UInt32, DNSServiceRegisterRecordReply!, UnsafeMutableRawPointer!) -> DNSServiceErrorType](dnsserviceregisterrecord(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Registers an individual resource record on a connected DNSServiceRef.
- [func PeerConnectionRelease(DNSServiceFlags, UnsafePointer<CChar>!, UnsafePointer<CChar>!, UnsafePointer<CChar>!) -> DNSServiceErrorType](peerconnectionrelease(_:_:_:_:).md)
  Releases P2P connection resources associated with the service instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsservicereconfirmrecord(_:_:_:_:_:_:_:))*