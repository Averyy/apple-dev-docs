# DNSServiceCreateConnection(_:)

**Framework**: dnssd  
**Kind**: func

Creates a connection to the daemon, allowing efficient registration of multiple individual records.

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
func DNSServiceCreateConnection(_ sdRef: UnsafeMutablePointer<DNSServiceRef?>!) -> DNSServiceErrorType
```

#### Return Value

Returns [`kDNSServiceErr_NoError`](kdnsserviceerr_noerror.md) on success, otherwise returns an error code indicating the specific failure that occurred (in which case the DNSServiceRef is not initialized).

## Parameters

- `sdRef`: A pointer to an uninitialized DNSServiceRef. Deallocating the reference (via  ) severs the connection and deregisters all records registered on this connection.

## See Also

- [func DNSServiceReconfirmRecord(DNSServiceFlags, UInt32, UnsafePointer<CChar>!, UInt16, UInt16, UInt16, UnsafeRawPointer!) -> DNSServiceErrorType](dnsservicereconfirmrecord(_:_:_:_:_:_:_:).md)
  Instructs the daemon to verify the validity of a resource record that appears to be out of date (for example, because TCP connection to a service’s target failed).
- [func DNSServiceRegisterRecord(DNSServiceRef!, UnsafeMutablePointer<DNSRecordRef?>!, DNSServiceFlags, UInt32, UnsafePointer<CChar>!, UInt16, UInt16, UInt16, UnsafeRawPointer!, UInt32, DNSServiceRegisterRecordReply!, UnsafeMutableRawPointer!) -> DNSServiceErrorType](dnsserviceregisterrecord(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Registers an individual resource record on a connected DNSServiceRef.
- [func PeerConnectionRelease(DNSServiceFlags, UnsafePointer<CChar>!, UnsafePointer<CChar>!, UnsafePointer<CChar>!) -> DNSServiceErrorType](peerconnectionrelease(_:_:_:_:).md)
  Releases P2P connection resources associated with the service instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsservicecreateconnection(_:))*