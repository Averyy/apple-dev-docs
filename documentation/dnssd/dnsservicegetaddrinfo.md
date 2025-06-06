# DNSServiceGetAddrInfo(_:_:_:_:_:_:_:)

**Framework**: dnssd  
**Kind**: func

Queries for the IP address of a hostname by using either Multicast or Unicast DNS.

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
func DNSServiceGetAddrInfo(_ sdRef: UnsafeMutablePointer<DNSServiceRef?>!, _ flags: DNSServiceFlags, _ interfaceIndex: UInt32, _ protocol: DNSServiceProtocol, _ hostname: UnsafePointer<CChar>!, _ callBack: DNSServiceGetAddrInfoReply!, _ context: UnsafeMutableRawPointer!) -> DNSServiceErrorType
```

#### Return Value

Returns [`kDNSServiceErr_NoError`](kdnsserviceerr_noerror.md) on success (any subsequent, asynchronous errors are delivered to the callback), otherwise returns an error code indicating the error that occurred.

## Parameters

- `sdRef`: A pointer to an uninitialized DNSServiceRef. If the call succeeds then it initializes the DNSServiceRef, returns  , and the query begins and will last indefinitely until the client terminates the query by passing this DNSServiceRef to  .
- `flags`: kDNSServiceFlagsForceMulticast or kDNSServiceFlagsLongLivedQuery. Pass kDNSServiceFlagsLongLivedQuery to create a “long-lived” unicast query to a unicast DNS server that implements the protocol. This flag has no effect on link-local multicast queries.
- `interfaceIndex`: The interface on which to issue the query. Passing 0 causes the query to be sent on all active interfaces via Multicast or the primary interface via Unicast.
- `protocol`: * If “hostname” is a wide-area unicast DNS hostname (i.e. not a “.local.” name) but this host has no routable IPv6 address, then the call will not try to look up IPv6 addresses for “hostname”, since any addresses it found would be unlikely to be of any use anyway. Similarly, if this host has no routable IPv4 address, the call will not try to look up IPv4 addresses for “hostname”.
- `hostname`: The fully qualified domain name of the host to be queried for.
- `callBack`: The function to be called when the query succeeds or fails asynchronously.
- `context`: An application context pointer which is passed to the callback function (may be NULL).


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsservicegetaddrinfo(_:_:_:_:_:_:_:))*