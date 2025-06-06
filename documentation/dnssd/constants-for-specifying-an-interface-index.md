# Constants for specifying an interface index

**Framework**: dnssd

#### Overview

This section describes the functions, callbacks, and data structures that make up the DNS Service Discovery API.

The DNS Service Discovery API is part of Bonjour, Apple’s implementation of zero-configuration networking (ZEROCONF).

Bonjour allows you to register a network service, such as a printer or file server, so that it can be found by name or browsed for by service type and domain. Using Bonjour, applications can discover what services are available on the network, along with all the information – such as name, IP address, and port – necessary to access a particular service.

In effect, Bonjour combines the functions of a local DNS server and AppleTalk. Bonjour allows applications to provide user-friendly printer and server browsing, among other things, over standard IP networks. This behavior is a result of combining protocols such as multicast and DNS to add new functionality to the network (such as multicast DNS).

Bonjour gives applications easy access to services over local IP networks without requiring the service or the application to support an AppleTalk or a Netbeui stack, and without requiring a DNS server for the local network.

Notes on DNS Name Escaping

– or –

“Why is [`kDNSServiceMaxDomainName`](kdnsservicemaxdomainname.md) 1009, when the maximum legal domain name is 256 bytes?”

All strings used in the DNS-SD APIs are UTF-8 strings. Apart from the exceptions noted below, the APIs expect the strings to be properly escaped, using the conventional DNS escaping rules:

- ‘\\’ represents a single literal ‘\’ in the name
- ‘\.’ represents a single literal ‘.’ in the name
- ‘\ddd’, where ddd is a three-digit decimal value from 000 to 255, represents a single literal byte with that value.
- A bare unescaped ‘.’ is a label separator, marking a boundary between domain and subdomain.

The exceptions, that do not use escaping, are the routines where the full DNS name of a resource is broken, for convenience, into servicename/regtype/domain. In these routines, the “servicename” is NOT escaped. It does not need to be, since it is, by definition, just a single literal string. Any characters in that string represent exactly what they are. The “regtype” portion is, technically speaking, escaped, but since legal regtypes are only allowed to contain letters, digits, and hyphens, there is nothing to escape, so the issue is moot. The “domain” portion is also escaped, though most domains in use on the public Internet today, like regtypes, don’t contain any characters that need to be escaped. As DNS-SD becomes more popular, rich-text domains for service discovery will become common, so software should be written to cope with domains with escaping.

The servicename may be up to 63 bytes of UTF-8 text (not counting the C-String terminating NULL at the end). The regtype is of the form _service._tcp or _service._udp, where the “service” part is 1-15 characters, which may be letters, digits, or hyphens. The domain part of the three-part name may be any legal domain, providing that the resulting servicename+regtype+domain name does not exceed 256 bytes.

For most software, these issues are transparent. When browsing, the discovered servicenames should simply be displayed as-is. When resolving, the discovered servicename/regtype/domain are simply passed unchanged to [`DNSServiceResolve(_:_:_:_:_:_:_:_:)`](dnsserviceresolve(_:_:_:_:_:_:_:_:).md). When a [`DNSServiceResolve(_:_:_:_:_:_:_:_:)`](dnsserviceresolve(_:_:_:_:_:_:_:_:).md) succeeds, the returned fullname is already in the correct format to pass to standard system DNS APIs such as res_query(). For converting from servicename/regtype/domain to a single properly-escaped full DNS name, the helper function [`DNSServiceConstructFullName(_:_:_:_:)`](dnsserviceconstructfullname(_:_:_:_:).md) is provided.

The following (highly contrived) example illustrates the escaping process. Suppose you have an service called “Dr. Smith\Dr. Johnson”, of type “_ftp._tcp” in subdomain “4th. Floor” of subdomain “Building 2” of domain “apple.com.” The full (escaped) DNS name of this service’s SRV record would be: Dr\.\032Smith\\Dr\.\032Johnson._ftp._tcp.4th\.\032Floor.Building\0322.apple.com.

## Topics

### Constants
- [var kDNSServiceInterfaceIndexAny: Int32](kdnsserviceinterfaceindexany.md)
- [var kDNSServiceInterfaceIndexLocalOnly: UInt32](kdnsserviceinterfaceindexlocalonly.md)
- [var kDNSServiceInterfaceIndexP2P: UInt32](kdnsserviceinterfaceindexp2p.md)
- [var kDNSServiceInterfaceIndexUnicast: UInt32](kdnsserviceinterfaceindexunicast.md)

## See Also

- [Miscellaneous Defines](miscellaneous-defines.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/constants-for-specifying-an-interface-index)*