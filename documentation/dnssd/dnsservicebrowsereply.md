# DNSServiceBrowseReply

**Framework**: dnssd  
**Kind**: typealias  
**Role**: Type Alias

Callback for handling the results of previous calls to DNSServiceBrowse.

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
typealias DNSServiceBrowseReply = (DNSServiceRef?, DNSServiceFlags, UInt32, DNSServiceErrorType, UnsafePointer<CChar>?, UnsafePointer<CChar>?, UnsafePointer<CChar>?, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*)(struct _DNSServiceRef_t *, unsigned int, unsigned int, int, const char *, const char *, const char *, void *) DNSServiceBrowseReply;
```

## Parameters

- `sdRef`: The DNSServiceRef initialized by [`DNSServiceBrowse(_:_:_:_:_:_:_:)`](./dnsservicebrowse%28_,_,_,_,_,_,_%29.md).
- `flags`: Possible values are [`kDNSServiceFlagsMoreComing`](./kdnsserviceflagsmorecoming.md) and kDNSServiceFlagsAdd. See flag definitions for details.
- `interfaceIndex`: The interface on which the service is advertised. This index should be passed to [`DNSServiceResolve(_:_:_:_:_:_:_:_:)`](./dnsserviceresolve%28_,_,_,_,_,_,_,_%29.md) when resolving the service.
- `errorCode`: Will be [`kDNSServiceErr_NoError`](./kdnsserviceerr_noerror.md) (0) on success, otherwise will indicate the failure that occurred. Other parameters are undefined if the errorCode is nonzero.
- `serviceName`: The discovered service name. This name should be displayed to the user, and stored for subsequent use in the [`DNSServiceResolve(_:_:_:_:_:_:_:_:)`](./dnsserviceresolve%28_,_,_,_,_,_,_,_%29.md) call.
- `regtype`: The service type, which is usually (but not always) the same as was passed to [`DNSServiceBrowse(_:_:_:_:_:_:_:)`](./dnsservicebrowse%28_,_,_,_,_,_,_%29.md). One case where the discovered service type may not be the same as the requested service type is when using subtypes: The client may want to browse for only those ftp servers that allow anonymous connections. The client will pass the string “_ftp._tcp,_anon” to [`DNSServiceBrowse(_:_:_:_:_:_:_:)`](./dnsservicebrowse%28_,_,_,_,_,_,_%29.md), but the type of the service that’s discovered is simply “_ftp._tcp”. The regtype for each discovered service instance should be stored along with the name, so that it can be passed to [`DNSServiceResolve(_:_:_:_:_:_:_:_:)`](./dnsserviceresolve%28_,_,_,_,_,_,_,_%29.md) when the service is later resolved.
- `replyDomain`: The domain of the discovered service instance. This may or may not be the same as the domain that was passed to [`DNSServiceBrowse(_:_:_:_:_:_:_:)`](./dnsservicebrowse%28_,_,_,_,_,_,_%29.md). The domain for each discovered service instance should be stored along with the name, so that it can be passed to [`DNSServiceResolve(_:_:_:_:_:_:_:_:)`](./dnsserviceresolve%28_,_,_,_,_,_,_,_%29.md) when the service is later resolved.
- `context`: The context pointer that was passed to the callout.

## See Also

### Callbacks
- [typealias DNSServiceGetAddrInfoReply](./dnsservicegetaddrinforeply.md)
  Callback for handling the results of a previous call to [`DNSServiceGetAddrInfo(_:_:_:_:_:_:_:)`](./dnsservicegetaddrinfo%28_,_,_,_,_,_,_%29.md).
- [typealias DNSServiceRegisterRecordReply](./dnsserviceregisterrecordreply.md)
  Callback for handling the results of a previous call to [`DNSServiceRegisterRecord(_:_:_:_:_:_:_:_:_:_:_:_:)`](./dnsserviceregisterrecord%28_,_,_,_,_,_,_,_,_,_,_,_%29.md).
- [typealias DNSServiceRegisterReply](./dnsserviceregisterreply.md)
  Handler for the results from a previous call to [`DNSServiceRegister(_:_:_:_:_:_:_:_:_:_:_:_:)`](./dnsserviceregister%28_,_,_,_,_,_,_,_,_,_,_,_%29.md).
- [typealias DNSServiceResolveReply](./dnsserviceresolvereply.md)
- [typealias DNSServiceQueryRecordReply](./dnsservicequeryrecordreply.md)
  Callback for handling the results of a previous call to [`DNSServiceQueryRecord(_:_:_:_:_:_:_:_:)`](./dnsservicequeryrecord%28_,_,_,_,_,_,_,_%29.md).
- [typealias DNSServiceNATPortMappingReply](./dnsservicenatportmappingreply.md)
  Callback for handling the reply from a previous call to [`DNSServiceNATPortMappingReply`](./dnsservicenatportmappingreply.md).
- [typealias DNSServiceDomainEnumReply](./dnsservicedomainenumreply.md)
  Callback for handling the results of a previous call to [`DNSServiceEnumerateDomains(_:_:_:_:_:)`](./dnsserviceenumeratedomains%28_,_,_,_,_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsservicebrowsereply)*