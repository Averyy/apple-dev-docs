# DNSServiceRegister(_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: dnssd  
**Kind**: func

Registers a service.

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
func DNSServiceRegister(_ sdRef: UnsafeMutablePointer<DNSServiceRef?>!, _ flags: DNSServiceFlags, _ interfaceIndex: UInt32, _ name: UnsafePointer<CChar>!, _ regtype: UnsafePointer<CChar>!, _ domain: UnsafePointer<CChar>!, _ host: UnsafePointer<CChar>!, _ port: UInt16, _ txtLen: UInt16, _ txtRecord: UnsafeRawPointer!, _ callBack: DNSServiceRegisterReply!, _ context: UnsafeMutableRawPointer!) -> DNSServiceErrorType
```

#### Return Value

Returns [`kDNSServiceErr_NoError`](kdnsserviceerr_noerror.md) on success (any subsequent, asynchronous errors are delivered to the callback), otherwise returns an error code indicating the error that occurred (the callback is never invoked and the DNSServiceRef is not initialized).

## Parameters

- `sdRef`: A pointer to an uninitialized DNSServiceRef. If the call succeeds then it initializes the DNSServiceRef, returns  , and the registration will remain active indefinitely until the client terminates it by passing this DNSServiceRef to  .
- `flags`: Indicates the renaming behavior on name conflict (most applications will pass 0). See flag definitions above for details.
- `interfaceIndex`: If non-zero, specifies the interface on which to register the service (the index for a given interface is determined via the   family of calls.) Most applications will pass 0 to register on all available interfaces. See “Constants for specifying an interface index” for more details.
- `name`: If non-NULL, specifies the service name to be registered. Most applications will not specify a name, in which case the computer name is used (this name is communicated to the client via the callback). If a name is specified, it must be 1-63 bytes of UTF-8 text. If the name is longer than 63 bytes it will be automatically truncated to a legal length, unless the   flag is set, in which case   will be returned.
- `regtype`: The group identifier itself is not sent in clear. Only a hash of the group identifier is sent and the clients discover them anonymously. The group identifier may be up to 256 bytes long and may contain any eight bit values except comma which should be escaped.
- `domain`: If non-NULL, specifies the domain on which to advertise the service. Most applications will not specify a domain, instead automatically registering in the default domain(s).
- `host`: If non-NULL, specifies the SRV target host name. Most applications will not specify a host, instead automatically using the machine’s default host name(s). Note that specifying a non-NULL host does NOT create an address record for that host - the application is responsible for ensuring that the appropriate address record exists, or creating it via  .
- `port`: The port, in network byte order, on which the service accepts connections. Pass 0 for a “placeholder” service (that is, a service that will not be discovered by browsing, but will cause a name conflict if another client tries to register that same name). Most clients will not use placeholder services.
- `txtLen`: The length of the  , in bytes. Must be zero if the   is NULL.
- `txtRecord`: The TXT record  . A non-NULL   MUST be a properly formatted DNS TXT record—that is, <length byte> <data> <length byte> <data> … Passing   for the   is allowed as a synonym for  —it creates a TXT record of length one containing a single empty string. RFC 1035 doesn’t allow a TXT record to contain *zero* strings, so a single empty string is the smallest legal DNS TXT record. As with the other parameters, the DNSServiceRegister call copies the txtRecord data; for example, if you allocated the storage for the   parameter with   then you can safely free that memory right after the DNSServiceRegister call returns.
- `callBack`: The function to be called when the registration completes or asynchronously fails. The client may pass   for the callback;  the client will not be notified of the default values picked on its behalf, and the client will not be notified of any asynchronous errors (for example, out of memory errors, and so forth) that may prevent the registration of the service. The client may not pass the   flag if the callback is  . The client may still deregister the service at any time via  .
- `context`: An application context pointer that is passed to the callback function (may be  ).

## See Also

- [func DNSServiceAddRecord(DNSServiceRef!, UnsafeMutablePointer<DNSRecordRef?>!, DNSServiceFlags, UInt16, UInt16, UnsafeRawPointer!, UInt32) -> DNSServiceErrorType](dnsserviceaddrecord(_:_:_:_:_:_:_:).md)
  Adds a record to a registered service.
- [func DNSServiceRemoveRecord(DNSServiceRef!, DNSRecordRef!, DNSServiceFlags) -> DNSServiceErrorType](dnsserviceremoverecord(_:_:_:).md)
  Removes a record previously added to a service record set via [`DNSServiceAddRecord(_:_:_:_:_:_:_:)`](dnsserviceaddrecord(_:_:_:_:_:_:_:).md), or deregister an record registered individually via [`DNSServiceRegisterRecord(_:_:_:_:_:_:_:_:_:_:_:_:)`](dnsserviceregisterrecord(_:_:_:_:_:_:_:_:_:_:_:_:).md).
- [func DNSServiceUpdateRecord(DNSServiceRef!, DNSRecordRef!, DNSServiceFlags, UInt16, UnsafeRawPointer!, UInt32) -> DNSServiceErrorType](dnsserviceupdaterecord(_:_:_:_:_:_:).md)
  Updates a registered resource record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsserviceregister(_:_:_:_:_:_:_:_:_:_:_:_:))*