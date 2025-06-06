# DNS Service Discovery C

**Framework**: dnssd

See the Overview section above for header-level documentation.

##### Overview

###### Included Headers

- [`types.h`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/types/index.html#//apple_ref/doc/header/types.h)
- [`types.h`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Darwin/Reference/usr_APIs/types/index.html#//apple_ref/doc/header/types.h)
- “Tiano.h”
- <windows.h>
- <stdint.h>
- <dispatch/dispatch.h>

## Topics

### Version checking
- [func DNSServiceGetProperty(UnsafePointer<CChar>!, UnsafeMutableRawPointer!, UnsafeMutablePointer<UInt32>!) -> DNSServiceErrorType](dnsservicegetproperty(_:_:_:).md)
  Gets the specified property of a service.
### Unix Domain Socket access, DNSServiceRef deallocation, and data processing functions
- [func DNSServiceProcessResult(DNSServiceRef!) -> DNSServiceErrorType](dnsserviceprocessresult(_:).md)
  Reads a reply from the daemon, calling the appropriate application callback.
- [func DNSServiceRefDeallocate(DNSServiceRef!)](dnsservicerefdeallocate(_:).md)
  Terminates a connection with the daemon and frees memory associated with the DNSServiceRef.
- [func DNSServiceRefSockFD(DNSServiceRef!) -> dnssd_sock_t](dnsservicerefsockfd(_:).md)
  Accesses underlying Unix domain socket for an initialized DNSServiceRef.
### Unified lookup of both IPv4 and IPv6 addresses for a fully qualified hostname
- [func DNSServiceGetAddrInfo(UnsafeMutablePointer<DNSServiceRef?>!, DNSServiceFlags, UInt32, DNSServiceProtocol, UnsafePointer<CChar>!, DNSServiceGetAddrInfoReply!, UnsafeMutableRawPointer!) -> DNSServiceErrorType](dnsservicegetaddrinfo(_:_:_:_:_:_:_:).md)
  Queries for the IP address of a hostname by using either Multicast or Unicast DNS.
### TXT Record Parsing Functions
- [DNSServiceCreateDelegateConnection](dnsservicecreatedelegateconnection.md)
  Create a delegate connection to the daemon allowing efficient registration of multiple individual records.
- [func DNSServiceSetDispatchQueue(DNSServiceRef!, dispatch_queue_t!) -> DNSServiceErrorType](dnsservicesetdispatchqueue(_:_:).md)
  Allows you to schedule a DNSServiceRef on a serial dispatch queue for receiving asynchronous callbacks.
- [func TXTRecordContainsKey(UInt16, UnsafeRawPointer!, UnsafePointer<CChar>!) -> Int32](txtrecordcontainskey(_:_:_:).md)
  Allows you to determine if a given TXT Record contains a specified key.
- [func TXTRecordGetCount(UInt16, UnsafeRawPointer!) -> UInt16](txtrecordgetcount(_:_:).md)
  Returns the number of keys stored in the TXT Record.
- [func TXTRecordGetItemAtIndex(UInt16, UnsafeRawPointer!, UInt16, UInt16, UnsafeMutablePointer<CChar>!, UnsafeMutablePointer<UInt8>!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> DNSServiceErrorType](txtrecordgetitematindex(_:_:_:_:_:_:_:).md)
  Allows you to retrieve a key name and value pointer, given an index into a TXT Record.
- [func TXTRecordGetValuePtr(UInt16, UnsafeRawPointer!, UnsafePointer<CChar>!, UnsafeMutablePointer<UInt8>!) -> UnsafeRawPointer!](txtrecordgetvalueptr(_:_:_:_:).md)
  Allows you to retrieve the value for a given key from a TXT Record.
### TXT Record Construction Functions
- [func TXTRecordCreate(UnsafeMutablePointer<TXTRecordRef>!, UInt16, UnsafeMutableRawPointer!)](txtrecordcreate(_:_:_:).md)
  Creates a new empty TXTRecordRef referencing the specified storage.
- [func TXTRecordDeallocate(UnsafeMutablePointer<TXTRecordRef>!)](txtrecorddeallocate(_:).md)
  Releases resources associated with a TXT record.
- [func TXTRecordGetBytesPtr(UnsafePointer<TXTRecordRef>!) -> UnsafeRawPointer!](txtrecordgetbytesptr(_:).md)
  Allows you to retrieve a pointer to the raw bytes within a TXTRecordRef.
- [func TXTRecordGetLength(UnsafePointer<TXTRecordRef>!) -> UInt16](txtrecordgetlength(_:).md)
  Allows you to determine the length of the raw bytes within a TXTRecordRef.
- [func TXTRecordRemoveValue(UnsafeMutablePointer<TXTRecordRef>!, UnsafePointer<CChar>!) -> DNSServiceErrorType](txtrecordremovevalue(_:_:).md)
  Removes a key from a TXTRecordRef.
- [func TXTRecordSetValue(UnsafeMutablePointer<TXTRecordRef>!, UnsafePointer<CChar>!, UInt8, UnsafeRawPointer!) -> DNSServiceErrorType](txtrecordsetvalue(_:_:_:_:).md)
  Adds a key (optionally with value) to a TXTRecordRef.
### Special Purpose Calls
- [func DNSServiceCreateConnection(UnsafeMutablePointer<DNSServiceRef?>!) -> DNSServiceErrorType](dnsservicecreateconnection(_:).md)
  Creates a connection to the daemon, allowing efficient registration of multiple individual records.
- [func DNSServiceReconfirmRecord(DNSServiceFlags, UInt32, UnsafePointer<CChar>!, UInt16, UInt16, UInt16, UnsafeRawPointer!) -> DNSServiceErrorType](dnsservicereconfirmrecord(_:_:_:_:_:_:_:).md)
  Instructs the daemon to verify the validity of a resource record that appears to be out of date (for example, because TCP connection to a service’s target failed).
- [func DNSServiceRegisterRecord(DNSServiceRef!, UnsafeMutablePointer<DNSRecordRef?>!, DNSServiceFlags, UInt32, UnsafePointer<CChar>!, UInt16, UInt16, UInt16, UnsafeRawPointer!, UInt32, DNSServiceRegisterRecordReply!, UnsafeMutableRawPointer!) -> DNSServiceErrorType](dnsserviceregisterrecord(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Registers an individual resource record on a connected DNSServiceRef.
- [func PeerConnectionRelease(DNSServiceFlags, UnsafePointer<CChar>!, UnsafePointer<CChar>!, UnsafePointer<CChar>!) -> DNSServiceErrorType](peerconnectionrelease(_:_:_:_:).md)
  Releases P2P connection resources associated with the service instance.
### Service Registration
- [func DNSServiceAddRecord(DNSServiceRef!, UnsafeMutablePointer<DNSRecordRef?>!, DNSServiceFlags, UInt16, UInt16, UnsafeRawPointer!, UInt32) -> DNSServiceErrorType](dnsserviceaddrecord(_:_:_:_:_:_:_:).md)
  Adds a record to a registered service.
- [func DNSServiceRegister(UnsafeMutablePointer<DNSServiceRef?>!, DNSServiceFlags, UInt32, UnsafePointer<CChar>!, UnsafePointer<CChar>!, UnsafePointer<CChar>!, UnsafePointer<CChar>!, UInt16, UInt16, UnsafeRawPointer!, DNSServiceRegisterReply!, UnsafeMutableRawPointer!) -> DNSServiceErrorType](dnsserviceregister(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Registers a service.
- [func DNSServiceRemoveRecord(DNSServiceRef!, DNSRecordRef!, DNSServiceFlags) -> DNSServiceErrorType](dnsserviceremoverecord(_:_:_:).md)
  Removes a record previously added to a service record set via [`DNSServiceAddRecord(_:_:_:_:_:_:_:)`](dnsserviceaddrecord(_:_:_:_:_:_:_:).md), or deregister an record registered individually via [`DNSServiceRegisterRecord(_:_:_:_:_:_:_:_:_:_:_:_:)`](dnsserviceregisterrecord(_:_:_:_:_:_:_:_:_:_:_:_:).md).
- [func DNSServiceUpdateRecord(DNSServiceRef!, DNSRecordRef!, DNSServiceFlags, UInt16, UnsafeRawPointer!, UInt32) -> DNSServiceErrorType](dnsserviceupdaterecord(_:_:_:_:_:_:).md)
  Updates a registered resource record.
### Service Discovery
- [func DNSServiceBrowse(UnsafeMutablePointer<DNSServiceRef?>!, DNSServiceFlags, UInt32, UnsafePointer<CChar>!, UnsafePointer<CChar>!, DNSServiceBrowseReply!, UnsafeMutableRawPointer!) -> DNSServiceErrorType](dnsservicebrowse(_:_:_:_:_:_:_:).md)
  Browses for available services.
- [func DNSServiceResolve(UnsafeMutablePointer<DNSServiceRef?>!, DNSServiceFlags, UInt32, UnsafePointer<CChar>!, UnsafePointer<CChar>!, UnsafePointer<CChar>!, DNSServiceResolveReply!, UnsafeMutableRawPointer!) -> DNSServiceErrorType](dnsserviceresolve(_:_:_:_:_:_:_:_:).md)
### Querying Individual Specific Records
- [func DNSServiceQueryRecord(UnsafeMutablePointer<DNSServiceRef?>!, DNSServiceFlags, UInt32, UnsafePointer<CChar>!, UInt16, UInt16, DNSServiceQueryRecordReply!, UnsafeMutableRawPointer!) -> DNSServiceErrorType](dnsservicequeryrecord(_:_:_:_:_:_:_:_:).md)
  Query for an arbitrary DNS record.
### NAT Port Mapping
- [func DNSServiceNATPortMappingCreate(UnsafeMutablePointer<DNSServiceRef?>!, DNSServiceFlags, UInt32, DNSServiceProtocol, UInt16, UInt16, UInt32, DNSServiceNATPortMappingReply!, UnsafeMutableRawPointer!) -> DNSServiceErrorType](dnsservicenatportmappingcreate(_:_:_:_:_:_:_:_:_:).md)
  Requests a port mapping in the NAT gateway, which maps a port on the local machine to an external port on the NAT.
### General Utility Functions
- [func DNSServiceConstructFullName(UnsafeMutablePointer<CChar>!, UnsafePointer<CChar>!, UnsafePointer<CChar>!, UnsafePointer<CChar>!) -> DNSServiceErrorType](dnsserviceconstructfullname(_:_:_:_:).md)
  Concatenates a three-part domain name (as returned by the above callbacks) into a properly-escaped full domain name.
### Domain Enumeration
- [func DNSServiceEnumerateDomains(UnsafeMutablePointer<DNSServiceRef?>!, DNSServiceFlags, UInt32, DNSServiceDomainEnumReply!, UnsafeMutableRawPointer!) -> DNSServiceErrorType](dnsserviceenumeratedomains(_:_:_:_:_:).md)
  Enumerates domains that are recommended for registration and browsing.
### Callbacks
- [typealias DNSServiceGetAddrInfoReply](dnsservicegetaddrinforeply.md)
  Callback for handling the results of a previous call to [`DNSServiceGetAddrInfo(_:_:_:_:_:_:_:)`](dnsservicegetaddrinfo(_:_:_:_:_:_:_:).md).
- [typealias DNSServiceRegisterRecordReply](dnsserviceregisterrecordreply.md)
  Callback for handling the results of a previous call to [`DNSServiceRegisterRecord(_:_:_:_:_:_:_:_:_:_:_:_:)`](dnsserviceregisterrecord(_:_:_:_:_:_:_:_:_:_:_:_:).md).
- [typealias DNSServiceRegisterReply](dnsserviceregisterreply.md)
  Handler for the results from a previous call to [`DNSServiceRegister(_:_:_:_:_:_:_:_:_:_:_:_:)`](dnsserviceregister(_:_:_:_:_:_:_:_:_:_:_:_:).md).
- [typealias DNSServiceBrowseReply](dnsservicebrowsereply.md)
  Callback for handling the results of previous calls to DNSServiceBrowse.
- [typealias DNSServiceResolveReply](dnsserviceresolvereply.md)
- [typealias DNSServiceQueryRecordReply](dnsservicequeryrecordreply.md)
  Callback for handling the results of a previous call to [`DNSServiceQueryRecord(_:_:_:_:_:_:_:_:)`](dnsservicequeryrecord(_:_:_:_:_:_:_:_:).md).
- [typealias DNSServiceNATPortMappingReply](dnsservicenatportmappingreply.md)
  Callback for handling the reply from a previous call to [`DNSServiceNATPortMappingReply`](dnsservicenatportmappingreply.md).
- [typealias DNSServiceDomainEnumReply](dnsservicedomainenumreply.md)
  Callback for handling the results of a previous call to [`DNSServiceEnumerateDomains(_:_:_:_:_:)`](dnsserviceenumeratedomains(_:_:_:_:_:).md).
### Data Types
- [typealias DNSServiceErrorType](dnsserviceerrortype.md)
- [typealias DNSServiceFlags](dnsserviceflags.md)
- [typealias DNSServiceProtocol](dnsserviceprotocol.md)
- [typealias TXTRecordRef](txtrecordref.md)
  Opaque internal data type that represents a DNS-SD TXT record.
### Constants
- [Constants for specifying an interface index](constants-for-specifying-an-interface-index.md)
- [Miscellaneous Defines](miscellaneous-defines.md)

## See Also

- [dnssd Enumerations](dnssd-enumerations.md)
- [dnssd Functions](dnssd-functions.md)
- [dnssd Data Types](dnssd-data-types.md)
- [dnssd Constants](dnssd-constants.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/dns-service-discovery-c)*