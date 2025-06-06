# PeerConnectionRelease(_:_:_:_:)

**Framework**: dnssd  
**Kind**: func

Releases P2P connection resources associated with the service instance.

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
func PeerConnectionRelease(_ flags: DNSServiceFlags, _ name: UnsafePointer<CChar>!, _ regtype: UnsafePointer<CChar>!, _ domain: UnsafePointer<CChar>!) -> DNSServiceErrorType
```

#### Discussion

When a service is resolved over a P2P interface, a connection is brought up to the peer advertising the service instance. This call will free the resources associated with that connection. Note that the reference to the service instance will only be maintained by the mDNSResponder daemon while the browse for the service type is still running. Thus the sequence of calls to discover, resolve, and then terminate the connection associated with a given P2P service instance would be:

DNSServiceRef BrowseRef, ResolveRef; DNSServiceBrowse(&BrowseRef, …) // browse for all instances of the service DNSServiceResolve(&ResolveRef, …) // resolving a service instance creates a // connection to the peer device advertising that service DNSServiceRefDeallocate(ResolveRef) // Stop the resolve, which does not close the peer connection

// Communicate with the peer application.

PeerConnectionRelease() // release the connection to the peer device for the specified service instance

DNSServiceRefDeallocate(BrowseRef) // stop the browse // Any further calls to PeerConnectionRelease() will have no affect since the // service instance to peer connection relationship is only maintained by the // mDNSResponder daemon while the browse is running.

flags: Not currently used.

name: The name of the service instance to be resolved, as reported to the [`DNSServiceBrowseReply`](dnsservicebrowsereply.md) callback.

regtype: The type of the service instance to be resolved, as reported to the [`DNSServiceBrowseReply`](dnsservicebrowsereply.md) callback.

domain: The domain of the service instance to be resolved, as reported to the [`DNSServiceBrowseReply`](dnsservicebrowsereply.md) callback.

return value: Returns [`kDNSServiceErr_NoError`](kdnsserviceerr_noerror.md) on success or the error that occurred.

## See Also

- [func DNSServiceCreateConnection(UnsafeMutablePointer<DNSServiceRef?>!) -> DNSServiceErrorType](dnsservicecreateconnection(_:).md)
  Creates a connection to the daemon, allowing efficient registration of multiple individual records.
- [func DNSServiceReconfirmRecord(DNSServiceFlags, UInt32, UnsafePointer<CChar>!, UInt16, UInt16, UInt16, UnsafeRawPointer!) -> DNSServiceErrorType](dnsservicereconfirmrecord(_:_:_:_:_:_:_:).md)
  Instructs the daemon to verify the validity of a resource record that appears to be out of date (for example, because TCP connection to a service’s target failed).
- [func DNSServiceRegisterRecord(DNSServiceRef!, UnsafeMutablePointer<DNSRecordRef?>!, DNSServiceFlags, UInt32, UnsafePointer<CChar>!, UInt16, UInt16, UInt16, UnsafeRawPointer!, UInt32, DNSServiceRegisterRecordReply!, UnsafeMutableRawPointer!) -> DNSServiceErrorType](dnsserviceregisterrecord(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Registers an individual resource record on a connected DNSServiceRef.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/peerconnectionrelease(_:_:_:_:))*