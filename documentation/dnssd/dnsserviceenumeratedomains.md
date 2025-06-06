# DNSServiceEnumerateDomains(_:_:_:_:_:)

**Framework**: dnssd  
**Kind**: func

Enumerates domains that are recommended for registration and browsing.

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
func DNSServiceEnumerateDomains(_ sdRef: UnsafeMutablePointer<DNSServiceRef?>!, _ flags: DNSServiceFlags, _ interfaceIndex: UInt32, _ callBack: DNSServiceDomainEnumReply!, _ context: UnsafeMutableRawPointer!) -> DNSServiceErrorType
```

#### Return Value

Returns [`kDNSServiceErr_NoError`](kdnsserviceerr_noerror.md) on success (any subsequent, asynchronous errors are delivered to the callback), otherwise returns an error code indicating the error that occurred (the callback is not invoked and the DNSServiceRef is not initialized).

#### Discussion

The enumeration MUST be cancelled via [`DNSServiceRefDeallocate(_:)`](dnsservicerefdeallocate(_:).md) when no more domains are to be found.

Note that the names returned are (like all of DNS-SD) UTF-8 strings, and are escaped using standard DNS escaping rules. (See “Notes on DNS Name Escaping” earlier in this file for more details.) A graphical browser displaying a hierarchical tree-structured view should cut the names at the bare dots to yield individual labels, then de-escape each label according to the escaping rules, and then display the resulting UTF-8 text.

## Parameters

- `sdRef`: A pointer to an uninitialized DNSServiceRef. If the call succeeds then it initializes the DNSServiceRef, returns  , and the enumeration operation will run indefinitely until the client terminates it by passing this DNSServiceRef to  .
- `flags`: Possible values are: kDNSServiceFlagsBrowseDomains to enumerate domains recommended for browsing. kDNSServiceFlagsRegistrationDomains to enumerate domains recommended for registration.
- `interfaceIndex`: If non-zero, specifies the interface on which to look for domains. (the index for a given interface is determined via the if_nametoindex() family of calls.) Most applications will pass 0 to enumerate domains on all interfaces. See “Constants for specifying an interface index” for more details.
- `callBack`: The function to be called when a domain is found or the call asynchronously fails.
- `context`: An application context pointer which is passed to the callback function (may be NULL).


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsserviceenumeratedomains(_:_:_:_:_:))*