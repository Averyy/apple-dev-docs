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

- `sdRef`: A pointer to an uninitialized DNSServiceRef. If the call succeeds then it initializes the DNSServiceRef, returns [`kDNSServiceErr_NoError`](kdnsserviceerr_noerror.md), and the registration will remain active indefinitely until the client terminates it by passing this DNSServiceRef to [`DNSServiceRefDeallocate(_:)`](dnsservicerefdeallocate(_:).md).
- `flags`: Indicates the renaming behavior on name conflict (most applications will pass 0). See flag definitions above for details.
- `interfaceIndex`: If non-zero, specifies the interface on which to register the service (the index for a given interface is determined via the `if_nametoindex()` family of calls.) Most applications will pass 0 to register on all available interfaces. See “Constants for specifying an interface index” for more details.
- `name`: If non-NULL, specifies the service name to be registered. Most applications will not specify a name, in which case the computer name is used (this name is communicated to the client via the callback). If a name is specified, it must be 1-63 bytes of UTF-8 text. If the name is longer than 63 bytes it will be automatically truncated to a legal length, unless the `NoAutoRename` flag is set, in which case `kDNSServiceErr_BadParam` will be returned.
- `regtype`: The service type followed by the protocol, separated by a dot (for example, “_ftp._tcp”). The service type must be an underscore, followed by 1-15 characters, which may be letters, digits, or hyphens. The transport protocol must be “_tcp” or “_udp”. New service types should be registered at [`http://www.dns-sd.org/ServiceTypes.html`](https://developer.apple.comhttp://www.dns-sd.org/ServiceTypes.html). Additional subtypes of the primary service type (where a service type has defined subtypes) follow the primary service type in a comma-separated list, with no additional spaces. For example, “_primarytype._tcp,_subtype1,_subtype2,_subtype3” . Subtypes provide a mechanism for filtered browsing: A client browsing for “_primarytype._tcp” will discover all instances of this type; a client browsing for “_primarytype._tcp,_subtype2” will discover only those instances that were registered with “_subtype2” in their list of registered subtypes. The subtype mechanism can be illustrated with some examples using the dns-sd command-line tool: % dns-sd -R Simple _test._tcp “” 1001 & % dns-sd -R Better _test._tcp,HasFeatureA “” 1002 & % dns-sd -R Best _test._tcp,HasFeatureA,HasFeatureB “” 1003 & Now: `% dns-sd -B _test._tcp #` will find all three services, `% dns-sd -B _test._tcp,HasFeatureA #` finds “Better” and “Best”, and `% dns-sd -B _test._tcp,HasFeatureB #` finds only “Best” Subtype labels may be up to 63 bytes long, and may contain any eight- bit byte values, including zero bytes. However, due to the nature of using a C-string-based API, conventional DNS escaping must be used for dots (’.’), commas (’,’), backslashes (’’) and zero bytes, as shown below: `% dns-sd -R Test '_test._tcp,s.one,s,two,s\three,s000four' local 123` When a service is registered, all the clients browsing for the registered type (“regtype”) will discover it. If the discovery should be restricted to a smaller set of well known peers, the service can be registered with additional data (group identifier) that is known only to a smaller set of peers. The group identifier should follow primary service type using a colon (”:”) as a delimiter. If subtypes are also present, it should be given before the subtype as shown below. `% dns-sd -R _test1 _http._tcp:mygroup1 local 1001 % dns-sd -R _test2 _http._tcp:mygroup2 local 1001 % dns-sd -R _test3 _http._tcp:mygroup3,HasFeatureA local 1001` Now: `% dns-sd -B _http._tcp:"mygroup1" #` will discover only test1, `% dns-sd -B _http._tcp:"mygroup2" #` will discover only test2 %, and `dns-sd -B _http._tcp:"mygroup3",HasFeatureA #` will discover only test3. By specifying the group information, only the members of that group are discovered. The group identifier itself is not sent in clear. Only a hash of the group identifier is sent and the clients discover them anonymously. The group identifier may be up to 256 bytes long and may contain any eight bit values except comma which should be escaped.
- `domain`: If non-NULL, specifies the domain on which to advertise the service. Most applications will not specify a domain, instead automatically registering in the default domain(s).
- `host`: If non-NULL, specifies the SRV target host name. Most applications will not specify a host, instead automatically using the machine’s default host name(s). Note that specifying a non-NULL host does NOT create an address record for that host - the application is responsible for ensuring that the appropriate address record exists, or creating it via [`DNSServiceRegisterRecord(_:_:_:_:_:_:_:_:_:_:_:_:)`](dnsserviceregisterrecord(_:_:_:_:_:_:_:_:_:_:_:_:).md).
- `port`: The port, in network byte order, on which the service accepts connections. Pass 0 for a “placeholder” service (that is, a service that will not be discovered by browsing, but will cause a name conflict if another client tries to register that same name). Most clients will not use placeholder services.
- `txtLen`: The length of the `txtRecord`, in bytes. Must be zero if the `txtRecord` is NULL.
- `txtRecord`: The TXT record `rdata`. A non-NULL `txtRecord` MUST be a properly formatted DNS TXT record—that is, <length byte> <data> <length byte> <data> … Passing `NULL` for the `txtRecord` is allowed as a synonym for `txtLen=1, txtRecord=""`—it creates a TXT record of length one containing a single empty string. RFC 1035 doesn’t allow a TXT record to contain *zero* strings, so a single empty string is the smallest legal DNS TXT record. As with the other parameters, the DNSServiceRegister call copies the txtRecord data; for example, if you allocated the storage for the `txtRecord` parameter with `malloc()` then you can safely free that memory right after the DNSServiceRegister call returns.
- `callBack`: The function to be called when the registration completes or asynchronously fails. The client may pass `NULL` for the callback;  the client will not be notified of the default values picked on its behalf, and the client will not be notified of any asynchronous errors (for example, out of memory errors, and so forth) that may prevent the registration of the service. The client may not pass the `NoAutoRename` flag if the callback is `NULL`. The client may still deregister the service at any time via [`DNSServiceRefDeallocate(_:)`](dnsservicerefdeallocate(_:).md).
- `context`: An application context pointer that is passed to the callback function (may be `NULL`).

## See Also

- [func DNSServiceAddRecord(DNSServiceRef!, UnsafeMutablePointer<DNSRecordRef?>!, DNSServiceFlags, UInt16, UInt16, UnsafeRawPointer!, UInt32) -> DNSServiceErrorType](dnsserviceaddrecord(_:_:_:_:_:_:_:).md)
  Adds a record to a registered service.
- [func DNSServiceRemoveRecord(DNSServiceRef!, DNSRecordRef!, DNSServiceFlags) -> DNSServiceErrorType](dnsserviceremoverecord(_:_:_:).md)
  Removes a record previously added to a service record set via [`DNSServiceAddRecord(_:_:_:_:_:_:_:)`](dnsserviceaddrecord(_:_:_:_:_:_:_:).md), or deregister an record registered individually via [`DNSServiceRegisterRecord(_:_:_:_:_:_:_:_:_:_:_:_:)`](dnsserviceregisterrecord(_:_:_:_:_:_:_:_:_:_:_:_:).md).
- [func DNSServiceUpdateRecord(DNSServiceRef!, DNSRecordRef!, DNSServiceFlags, UInt16, UnsafeRawPointer!, UInt32) -> DNSServiceErrorType](dnsserviceupdaterecord(_:_:_:_:_:_:).md)
  Updates a registered resource record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dnsserviceregister(_:_:_:_:_:_:_:_:_:_:_:_:))*