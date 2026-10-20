# DNSServiceDomainEnumReply

**Framework**: dnssd  
**Kind**: typealias  
**Role**: Type Alias

Callback for handling the results of a previous call to [`DNSServiceEnumerateDomains(_:_:_:_:_:)`](./dnsserviceenumeratedomains%28_,_,_,_,_%29.md).

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
typealias DNSServiceDomainEnumReply = (DNSServiceRef?, DNSServiceFlags, UInt32, DNSServiceErrorType, UnsafePointer<CChar>?, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*)(struct _DNSServiceRef_t *, unsigned int, unsigned int, int, const char *, void *) DNSServiceDomainEnumReply;
```

## Parameters

- `sdRef`: The DNSServiceRef initialized by [`DNSServiceEnumerateDomains(_:_:_:_:_:)`](./dnsserviceenumeratedomains%28_,_,_,_,_%29.md).
- `flags`: Possible values are:

  [`kDNSServiceFlagsMoreComing`](./kdnsserviceflagsmorecoming.md)

  kDNSServiceFlagsAdd

  kDNSServiceFlagsDefault
- `interfaceIndex`: Specifies the interface on which the domain exists. (The index for a given interface is determined via the if_nametoindex() family of calls.)
- `errorCode`: Will be [`kDNSServiceErr_NoError`](./kdnsserviceerr_noerror.md) (0) on success, otherwise indicates the failure that occurred (other parameters are undefined if errorCode is nonzero).
- `replyDomain`: The name of the domain.
- `context`: The context pointer passed to DNSServiceEnumerateDomains.

## See Also

### Callbacks
- [typealias DNSServiceGetAddrInfoReply](./dnsservicegetaddrinforeply.md)
  Callback for handling the results of a previous call to [`DNSServiceGetAddrInfo(_:_:_:_:_:_:_:)`](./dnsservicegetaddrinfo%28_,_,_,_,_,_,_%29.md).
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsservicedomainenumreply)*