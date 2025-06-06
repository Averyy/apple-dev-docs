# DNSServiceResolveReply

**Framework**: dnssd  
**Kind**: typealias

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
typealias DNSServiceResolveReply = (DNSServiceRef?, DNSServiceFlags, UInt32, DNSServiceErrorType, UnsafePointer<CChar>?, UnsafePointer<CChar>?, UInt16, UInt16, UnsafePointer<UInt8>?, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

Resolve a service name discovered via [`DNSServiceBrowse(_:_:_:_:_:_:_:)`](dnsservicebrowse(_:_:_:_:_:_:_:).md) to a target host name, port number, and txt record.

Note: Applications should NOT use [`DNSServiceResolve(_:_:_:_:_:_:_:_:)`](dnsserviceresolve(_:_:_:_:_:_:_:_:).md) solely for txt record monitoring - use [`DNSServiceQueryRecord(_:_:_:_:_:_:_:_:)`](dnsservicequeryrecord(_:_:_:_:_:_:_:_:).md) instead, as it is more efficient for this task.

Note: When the desired results have been returned, the client MUST terminate the resolve by calling [`DNSServiceRefDeallocate(_:)`](dnsservicerefdeallocate(_:).md).

Note: [`DNSServiceResolve(_:_:_:_:_:_:_:_:)`](dnsserviceresolve(_:_:_:_:_:_:_:_:).md) behaves correctly for typical services that have a single SRV record and a single TXT record. To resolve non-standard services with multiple SRV or TXT records, [`DNSServiceQueryRecord(_:_:_:_:_:_:_:_:)`](dnsservicequeryrecord(_:_:_:_:_:_:_:_:).md) should be used.

## Parameters

- `sdRef`: The DNSServiceRef initialized by  .
- `flags`: Possible values: 
- `interfaceIndex`: The interface on which the service was resolved.
- `errorCode`: Will be   (0) on success, otherwise will indicate the failure that occurred. Other parameters are undefined if the errorCode is nonzero.
- `fullname`: The full service domain name, in the form <servicename>.<protocol>.<domain>. (This name is escaped following standard DNS rules, making it suitable for passing to standard system DNS APIs such as res_query(), or to the special-purpose functions included in this API that take fullname parameters. See “Notes on DNS Name Escaping” earlier in this file for more details.)
- `hosttarget`: The target hostname of the machine providing the service. This name can be passed to functions like gethostbyname() to identify the host’s IP address.
- `port`: The port, in network byte order, on which connections are accepted for this service.
- `txtLen`: The length of the txt record, in bytes.
- `txtRecord`: The service’s primary txt record, in standard txt record format.
- `context`: This will ensure that your code compiles cleanly without warnings (and more importantly, works correctly) with both the old header and with the new corrected version.

## See Also

- [typealias DNSServiceGetAddrInfoReply](dnsservicegetaddrinforeply.md)
  Callback for handling the results of a previous call to [`DNSServiceGetAddrInfo(_:_:_:_:_:_:_:)`](dnsservicegetaddrinfo(_:_:_:_:_:_:_:).md).
- [typealias DNSServiceRegisterRecordReply](dnsserviceregisterrecordreply.md)
  Callback for handling the results of a previous call to [`DNSServiceRegisterRecord(_:_:_:_:_:_:_:_:_:_:_:_:)`](dnsserviceregisterrecord(_:_:_:_:_:_:_:_:_:_:_:_:).md).
- [typealias DNSServiceRegisterReply](dnsserviceregisterreply.md)
  Handler for the results from a previous call to [`DNSServiceRegister(_:_:_:_:_:_:_:_:_:_:_:_:)`](dnsserviceregister(_:_:_:_:_:_:_:_:_:_:_:_:).md).
- [typealias DNSServiceBrowseReply](dnsservicebrowsereply.md)
  Callback for handling the results of previous calls to DNSServiceBrowse.
- [typealias DNSServiceQueryRecordReply](dnsservicequeryrecordreply.md)
  Callback for handling the results of a previous call to [`DNSServiceQueryRecord(_:_:_:_:_:_:_:_:)`](dnsservicequeryrecord(_:_:_:_:_:_:_:_:).md).
- [typealias DNSServiceNATPortMappingReply](dnsservicenatportmappingreply.md)
  Callback for handling the reply from a previous call to [`DNSServiceNATPortMappingReply`](dnsservicenatportmappingreply.md).
- [typealias DNSServiceDomainEnumReply](dnsservicedomainenumreply.md)
  Callback for handling the results of a previous call to [`DNSServiceEnumerateDomains(_:_:_:_:_:)`](dnsserviceenumeratedomains(_:_:_:_:_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsserviceresolvereply)*