# DNSServiceQueryRecordReply

**Framework**: dnssd  
**Kind**: typealias

Callback for handling the results of a previous call to [`DNSServiceQueryRecord(_:_:_:_:_:_:_:_:)`](dnsservicequeryrecord(_:_:_:_:_:_:_:_:).md).

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
typealias DNSServiceQueryRecordReply = (DNSServiceRef?, DNSServiceFlags, UInt32, DNSServiceErrorType, UnsafePointer<CChar>?, UInt16, UInt16, UInt16, UnsafeRawPointer?, UInt32, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `sdRef`: The DNSServiceRef initialized by  .
- `flags`: Possible values are   and kDNSServiceFlagsAdd. The Add flag is NOT set for PTR records with a ttl of 0, i.e. “Remove” events.
- `interfaceIndex`: The interface on which the query was resolved (the index for a given interface is determined via the if_nametoindex() family of calls). See “Constants for specifying an interface index” for more details.
- `errorCode`: Will be   on success, otherwise will indicate the failure that occurred. Other parameters are undefined if errorCode is nonzero.
- `fullname`: The resource record’s full domain name.
- `rrtype`: The resource record’s type (e.g. kDNSServiceType_PTR, kDNSServiceType_SRV, and so on).
- `rrclass`: The class of the resource record (usually  ).
- `rdlen`: The length, in bytes, of the resource record rdata.
- `rdata`: The raw rdata of the resource record.
- `ttl`: If the client wishes to cache the result for performance reasons, the TTL indicates how long the client may legitimately hold onto this result, in seconds. After the TTL expires, the client should consider the result no longer valid, and if it requires this data again, it should be re-fetched with a new query. Of course, this only applies to clients that cancel the asynchronous operation when they get a result. Clients that leave the asynchronous operation running can safely assume that the data remains valid until they get another callback telling them otherwise.
- `context`: The context pointer that was passed to the callout.

## See Also

- [typealias DNSServiceGetAddrInfoReply](dnsservicegetaddrinforeply.md)
  Callback for handling the results of a previous call to [`DNSServiceGetAddrInfo(_:_:_:_:_:_:_:)`](dnsservicegetaddrinfo(_:_:_:_:_:_:_:).md).
- [typealias DNSServiceRegisterRecordReply](dnsserviceregisterrecordreply.md)
  Callback for handling the results of a previous call to [`DNSServiceRegisterRecord(_:_:_:_:_:_:_:_:_:_:_:_:)`](dnsserviceregisterrecord(_:_:_:_:_:_:_:_:_:_:_:_:).md).
- [typealias DNSServiceRegisterReply](dnsserviceregisterreply.md)
  Handler for the results from a previous call to [`DNSServiceRegister(_:_:_:_:_:_:_:_:_:_:_:_:)`](dnsserviceregister(_:_:_:_:_:_:_:_:_:_:_:_:).md).
- [typealias DNSServiceBrowseReply](dnsservicebrowsereply.md)
  Callback for handling the results of previous calls to DNSServiceBrowse.
- [typealias DNSServiceResolveReply](dnsserviceresolvereply.md)
- [typealias DNSServiceNATPortMappingReply](dnsservicenatportmappingreply.md)
  Callback for handling the reply from a previous call to [`DNSServiceNATPortMappingReply`](dnsservicenatportmappingreply.md).
- [typealias DNSServiceDomainEnumReply](dnsservicedomainenumreply.md)
  Callback for handling the results of a previous call to [`DNSServiceEnumerateDomains(_:_:_:_:_:)`](dnsserviceenumeratedomains(_:_:_:_:_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsservicequeryrecordreply)*