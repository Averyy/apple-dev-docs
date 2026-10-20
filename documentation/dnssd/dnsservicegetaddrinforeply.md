# DNSServiceGetAddrInfoReply

**Framework**: dnssd  
**Kind**: typealias  
**Role**: Type Alias

Callback for handling the results of a previous call to [`DNSServiceGetAddrInfo(_:_:_:_:_:_:_:)`](./dnsservicegetaddrinfo%28_,_,_,_,_,_,_%29.md).

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
typealias DNSServiceGetAddrInfoReply = (DNSServiceRef?, DNSServiceFlags, UInt32, DNSServiceErrorType, UnsafePointer<CChar>?, UnsafePointer<sockaddr>?, UInt32, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*)(struct _DNSServiceRef_t *, unsigned int, unsigned int, int, const char *, const struct sockaddr *, unsigned int, void *) DNSServiceGetAddrInfoReply;
```

## Parameters

- `sdRef`: The DNSServiceRef initialized by [`DNSServiceGetAddrInfo(_:_:_:_:_:_:_:)`](./dnsservicegetaddrinfo%28_,_,_,_,_,_,_%29.md).
- `flags`: Possible values are [`kDNSServiceFlagsMoreComing`](./kdnsserviceflagsmorecoming.md) and kDNSServiceFlagsAdd.
- `interfaceIndex`: The interface to which the answers pertain.
- `errorCode`: Will be [`kDNSServiceErr_NoError`](./kdnsserviceerr_noerror.md) on success, otherwise will indicate the failure that occurred. Other parameters are undefined if errorCode is nonzero.
- `hostname`: The fully qualified domain name of the host to be queried for.
- `address`: IPv4 or IPv6 address.
- `ttl`: If the client wishes to cache the result for performance reasons, the TTL indicates how long the client may legitimately hold onto this result, in seconds. After the TTL expires, the client should consider the result no longer valid, and if it requires this data again, it should be re-fetched with a new query. Of course, this only applies to clients that cancel the asynchronous operation when they get a result. Clients that leave the asynchronous operation running can safely assume that the data remains valid until they get another callback telling them otherwise.
- `context`: The context pointer that was passed to the callout.

## See Also

### Callbacks
- [typealias DNSServiceRegisterRecordReply](./dnsserviceregisterrecordreply.md)
  Callback for handling the results of a previous call to [`DNSServiceRegisterRecord(_:_:_:_:_:_:_:_:_:_:_:_:)`](./dnsserviceregisterrecord%28_,_,_,_,_,_,_,_,_,_,_,_%29.md).
- [typealias DNSServiceRegisterReply](./dnsserviceregisterreply.md)
  Handler for the results from a previous call to [`DNSServiceRegister(_:_:_:_:_:_:_:_:_:_:_:_:)`](./dnsserviceregister%28_,_,_,_,_,_,_,_,_,_,_,_%29.md).
- [typealias DNSServiceBrowseReply](./dnsservicebrowsereply.md)
  Callback for handling the results of previous calls to DNSServiceBrowse.
- [typealias DNSServiceResolveReply](./dnsserviceresolvereply.md)
- [typealias DNSServiceQueryRecordReply](./dnsservicequeryrecordreply.md)
  Callback for handling the results of a previous call to [`DNSServiceQueryRecord(_:_:_:_:_:_:_:_:)`](./dnsservicequeryrecord%28_,_,_,_,_,_,_,_%29.md).
- [typealias DNSServiceNATPortMappingReply](./dnsservicenatportmappingreply.md)
  Callback for handling the reply from a previous call to [`DNSServiceNATPortMappingReply`](./dnsservicenatportmappingreply.md).
- [typealias DNSServiceDomainEnumReply](./dnsservicedomainenumreply.md)
  Callback for handling the results of a previous call to [`DNSServiceEnumerateDomains(_:_:_:_:_:)`](./dnsserviceenumeratedomains%28_,_,_,_,_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsservicegetaddrinforeply)*