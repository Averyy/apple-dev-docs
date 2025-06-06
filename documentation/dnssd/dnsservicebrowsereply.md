# DNSServiceBrowseReply

**Framework**: dnssd  
**Kind**: typealias

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

## Parameters

- `sdRef`: The DNSServiceRef initialized by  .
- `flags`: Possible values are   and kDNSServiceFlagsAdd. See flag definitions for details.
- `interfaceIndex`: The interface on which the service is advertised. This index should be passed to   when resolving the service.
- `errorCode`: Will be   (0) on success, otherwise will indicate the failure that occurred. Other parameters are undefined if the errorCode is nonzero.
- `serviceName`: The discovered service name. This name should be displayed to the user, and stored for subsequent use in the   call.
- `regtype`: The service type, which is usually (but not always) the same as was passed to  . One case where the discovered service type may not be the same as the requested service type is when using subtypes: The client may want to browse for only those ftp servers that allow anonymous connections. The client will pass the string “_ftp._tcp,_anon” to  , but the type of the service that’s discovered is simply “_ftp._tcp”. The regtype for each discovered service instance should be stored along with the name, so that it can be passed to   when the service is later resolved.
- `replyDomain`: The domain of the discovered service instance. This may or may not be the same as the domain that was passed to  . The domain for each discovered service instance should be stored along with the name, so that it can be passed to   when the service is later resolved.
- `context`: The context pointer that was passed to the callout.

## See Also

- [typealias DNSServiceGetAddrInfoReply](dnsservicegetaddrinforeply.md)
  Callback for handling the results of a previous call to [`DNSServiceGetAddrInfo(_:_:_:_:_:_:_:)`](dnsservicegetaddrinfo(_:_:_:_:_:_:_:).md).
- [typealias DNSServiceRegisterRecordReply](dnsserviceregisterrecordreply.md)
  Callback for handling the results of a previous call to [`DNSServiceRegisterRecord(_:_:_:_:_:_:_:_:_:_:_:_:)`](dnsserviceregisterrecord(_:_:_:_:_:_:_:_:_:_:_:_:).md).
- [typealias DNSServiceRegisterReply](dnsserviceregisterreply.md)
  Handler for the results from a previous call to [`DNSServiceRegister(_:_:_:_:_:_:_:_:_:_:_:_:)`](dnsserviceregister(_:_:_:_:_:_:_:_:_:_:_:_:).md).
- [typealias DNSServiceResolveReply](dnsserviceresolvereply.md)
- [typealias DNSServiceQueryRecordReply](dnsservicequeryrecordreply.md)
  Callback for handling the results of a previous call to [`DNSServiceQueryRecord(_:_:_:_:_:_:_:_:)`](dnsservicequeryrecord(_:_:_:_:_:_:_:_:).md).
- [typealias DNSServiceNATPortMappingReply](dnsservicenatportmappingreply.md)
  Callback for handling the reply from a previous call to [`DNSServiceNATPortMappingReply`](dnsservicenatportmappingreply.md).
- [typealias DNSServiceDomainEnumReply](dnsservicedomainenumreply.md)
  Callback for handling the results of a previous call to [`DNSServiceEnumerateDomains(_:_:_:_:_:)`](dnsserviceenumeratedomains(_:_:_:_:_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsservicebrowsereply)*