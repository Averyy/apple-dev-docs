# DNSServiceQueryRecord(_:_:_:_:_:_:_:_:)

**Framework**: dnssd  
**Kind**: func

Query for an arbitrary DNS record.

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
func DNSServiceQueryRecord(_ sdRef: UnsafeMutablePointer<DNSServiceRef?>!, _ flags: DNSServiceFlags, _ interfaceIndex: UInt32, _ fullname: UnsafePointer<CChar>!, _ rrtype: UInt16, _ rrclass: UInt16, _ callBack: DNSServiceQueryRecordReply!, _ context: UnsafeMutableRawPointer!) -> DNSServiceErrorType
```

#### Return Value

Returns [`kDNSServiceErr_NoError`](kdnsserviceerr_noerror.md) on success (any subsequent, asynchronous errors are delivered to the callback), otherwise returns an error code indicating the error that occurred (the callback is never invoked and the DNSServiceRef is not initialized).

## Parameters

- `sdRef`: A pointer to an uninitialized DNSServiceRef. If the call succeeds then it initializes the DNSServiceRef, returns  , and the query operation will run indefinitely until the client terminates it by passing this DNSServiceRef to  .
- `flags`: kDNSServiceFlagsForceMulticast or kDNSServiceFlagsLongLivedQuery. Pass kDNSServiceFlagsLongLivedQuery to create a “long-lived” unicast query to a unicast DNS server that implements the protocol. This flag has no effect on link-local multicast queries.
- `interfaceIndex`: If non-zero, specifies the interface on which to issue the query (the index for a given interface is determined via the if_nametoindex() family of calls.) Passing 0 causes the name to be queried for on all interfaces. See “Constants for specifying an interface index” for more details.
- `fullname`: The full domain name of the resource record to be queried for.
- `rrtype`: The numerical type of the resource record to be queried for (e.g. kDNSServiceType_PTR, kDNSServiceType_SRV, and so on).
- `rrclass`: The class of the resource record (usually  ).
- `callBack`: The function to be called when a result is found, or if the call asynchronously fails.
- `context`: An application context pointer which is passed to the callback function (may be NULL).


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsservicequeryrecord(_:_:_:_:_:_:_:_:))*