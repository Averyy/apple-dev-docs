# DNSServiceRegisterReply

**Framework**: dnssd  
**Kind**: typealias

Handler for the results from a previous call to [`DNSServiceRegister(_:_:_:_:_:_:_:_:_:_:_:_:)`](dnsserviceregister(_:_:_:_:_:_:_:_:_:_:_:_:).md).

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
typealias DNSServiceRegisterReply = (DNSServiceRef?, DNSServiceFlags, DNSServiceErrorType, UnsafePointer<CChar>?, UnsafePointer<CChar>?, UnsafePointer<CChar>?, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `sdRef`: The DNSServiceRef initialized by  .
- `flags`: When a name is successfully registered, the callback will be invoked with the kDNSServiceFlagsAdd flag set. When Wide-Area DNS-SD is in use, it is possible for a single service to get more than one success callback (e.g. one in the “local” multicast DNS domain, and another in a wide-area unicast DNS domain). If a successfully-registered name later suffers a name conflict or similar problem and has to be deregistered, the callback will be invoked with the kDNSServiceFlagsAdd flag not set. The callback is *not* invoked in the case where the caller explicitly terminates the service registration by calling DNSServiceRefDeallocate(ref);
- `errorCode`: Will be   on success, otherwise will indicate the failure that occurred (including name conflicts, if the kDNSServiceFlagsNoAutoRename flag was used when registering.) Other parameters are undefined if errorCode is nonzero.
- `name`: The service name registered (if the application did not specify a name in  , this indicates what name was automatically chosen).
- `regtype`: The type of service registered, as it was passed to the callout.
- `domain`: The domain on which the service was registered (if the application did not specify a domain in  , this indicates the default domain on which the service was registered).
- `context`: The context pointer that was passed to the callout.

## See Also

- [typealias DNSServiceGetAddrInfoReply](dnsservicegetaddrinforeply.md)
  Callback for handling the results of a previous call to [`DNSServiceGetAddrInfo(_:_:_:_:_:_:_:)`](dnsservicegetaddrinfo(_:_:_:_:_:_:_:).md).
- [typealias DNSServiceRegisterRecordReply](dnsserviceregisterrecordreply.md)
  Callback for handling the results of a previous call to [`DNSServiceRegisterRecord(_:_:_:_:_:_:_:_:_:_:_:_:)`](dnsserviceregisterrecord(_:_:_:_:_:_:_:_:_:_:_:_:).md).
- [typealias DNSServiceBrowseReply](dnsservicebrowsereply.md)
  Callback for handling the results of previous calls to DNSServiceBrowse.
- [typealias DNSServiceResolveReply](dnsserviceresolvereply.md)
- [typealias DNSServiceQueryRecordReply](dnsservicequeryrecordreply.md)
  Callback for handling the results of a previous call to [`DNSServiceQueryRecord(_:_:_:_:_:_:_:_:)`](dnsservicequeryrecord(_:_:_:_:_:_:_:_:).md).
- [typealias DNSServiceNATPortMappingReply](dnsservicenatportmappingreply.md)
  Callback for handling the reply from a previous call to [`DNSServiceNATPortMappingReply`](dnsservicenatportmappingreply.md).
- [typealias DNSServiceDomainEnumReply](dnsservicedomainenumreply.md)
  Callback for handling the results of a previous call to [`DNSServiceEnumerateDomains(_:_:_:_:_:)`](dnsserviceenumeratedomains(_:_:_:_:_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsserviceregisterreply)*