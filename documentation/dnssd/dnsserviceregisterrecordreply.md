# DNSServiceRegisterRecordReply

**Framework**: dnssd  
**Kind**: typealias  
**Role**: Type Alias

Callback for handling the results of a previous call to [`DNSServiceRegisterRecord(_:_:_:_:_:_:_:_:_:_:_:_:)`](./dnsserviceregisterrecord%28_,_,_,_,_,_,_,_,_,_,_,_%29.md).

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
typealias DNSServiceRegisterRecordReply = (DNSServiceRef?, DNSRecordRef?, DNSServiceFlags, DNSServiceErrorType, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*)(struct _DNSServiceRef_t *, struct _DNSRecordRef_t *, unsigned int, int, void *) DNSServiceRegisterRecordReply;
```

## Parameters

- `sdRef`: The connected DNSServiceRef initialized by [`DNSServiceCreateConnection(_:)`](./dnsservicecreateconnection%28_%29.md).
- `RecordRef`: The DNSRecordRef initialized by [`DNSServiceRegisterRecord(_:_:_:_:_:_:_:_:_:_:_:_:)`](./dnsserviceregisterrecord%28_,_,_,_,_,_,_,_,_,_,_,_%29.md). If the above DNSServiceRef is passed to [`DNSServiceRefDeallocate(_:)`](./dnsservicerefdeallocate%28_%29.md), this DNSRecordRef is invalidated, and may not be used further.
- `flags`: Currently unused, reserved for future use.
- `errorCode`: Will be [`kDNSServiceErr_NoError`](./kdnsserviceerr_noerror.md) on success, otherwise will indicate the failure that occurred (including name conflicts.) Other parameters are undefined if errorCode is nonzero.
- `context`: The context pointer that was passed to the callout.

## See Also

### Callbacks
- [typealias DNSServiceGetAddrInfoReply](./dnsservicegetaddrinforeply.md)
  Callback for handling the results of a previous call to [`DNSServiceGetAddrInfo(_:_:_:_:_:_:_:)`](./dnsservicegetaddrinfo%28_,_,_,_,_,_,_%29.md).
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

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsserviceregisterrecordreply)*