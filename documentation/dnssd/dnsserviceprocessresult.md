# DNSServiceProcessResult(_:)

**Framework**: dnssd  
**Kind**: func

Reads a reply from the daemon, calling the appropriate application callback.

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
func DNSServiceProcessResult(_ sdRef: DNSServiceRef!) -> DNSServiceErrorType
```

#### Return Value

Returns [`kDNSServiceErr_NoError`](kdnsserviceerr_noerror.md) on success, otherwise returns an error code indicating the specific failure that occurred.

#### Discussion

This call blocks until the daemon’s response is received. Use [`DNSServiceRefSockFD(_:)`](dnsservicerefsockfd(_:).md) in conjunction with a run loop or select() to determine the presence of a response from the server before calling this function to process the reply without blocking. Call this function at any point if it is acceptable to block until the daemon’s response arrives. Note that the client is responsible for ensuring that [`DNSServiceProcessResult(_:)`](dnsserviceprocessresult(_:).md) is called whenever there is a reply from the daemon - the daemon may terminate its connection with a client that does not process the daemon’s responses.

## Parameters

- `sdRef`: A DNSServiceRef initialized by any of the DNSService calls that take a callback parameter.

## See Also

- [func DNSServiceRefDeallocate(DNSServiceRef!)](dnsservicerefdeallocate(_:).md)
  Terminates a connection with the daemon and frees memory associated with the DNSServiceRef.
- [func DNSServiceRefSockFD(DNSServiceRef!) -> dnssd_sock_t](dnsservicerefsockfd(_:).md)
  Accesses underlying Unix domain socket for an initialized DNSServiceRef.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsserviceprocessresult(_:))*