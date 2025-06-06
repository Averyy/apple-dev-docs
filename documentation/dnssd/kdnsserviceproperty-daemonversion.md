# kDNSServiceProperty_DaemonVersion

**Framework**: dnssd  
**Kind**: var

The daemon version property.

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
var kDNSServiceProperty_DaemonVersion: String { get }
```

#### Discussion

When requesting [`kDNSServiceProperty_DaemonVersion`](kdnsserviceproperty_daemonversion.md), the result pointer must point to a 32-bit unsigned integer, and the size parameter must be set to sizeof(uint32_t).

On return, the 32-bit unsigned integer contains the version number, formatted as follows:

Major part of the build number * 10000 +

minor part of the build number * 100

For example, OS X 10.4.9 has mDNSResponder-108.4, which would be represented as version 1080400. This allows applications to do simple greater-than and less-than comparisons: e.g. an application that requires at least mDNSResponder-108.4 can check:

```objc
 
   if (version >= 1080400) ...
 
```

Example usage:

```objc
 
 
 uint32_t version;
 uint32_t size = sizeof(version);
 DNSServiceErrorType err = DNSServiceGetProperty(kDNSServiceProperty_DaemonVersion, &version, &size);
 if (!err) printf("Bonjour version is %d.%d\n", version / 10000, version / 100 % 100);
 
 
```

## See Also

- [var DNS_SD_ORIGINAL_ENCODING_VERSION_NUMBER_MAX: Int32](dns_sd_original_encoding_version_number_max.md)
- [let kDNSServiceAttributeAAAAFallback: <<error type>>](kdnsserviceattributeaaaafallback.md)
- [var kDNSServiceInterfaceIndexAny: Int32](kdnsserviceinterfaceindexany.md)
- [var kDNSServiceInterfaceIndexBLE: UInt32](kdnsserviceinterfaceindexble.md)
- [var kDNSServiceInterfaceIndexInfra: UInt32](kdnsserviceinterfaceindexinfra.md)
- [var kDNSServiceInterfaceIndexLocalOnly: UInt32](kdnsserviceinterfaceindexlocalonly.md)
- [var kDNSServiceInterfaceIndexP2P: UInt32](kdnsserviceinterfaceindexp2p.md)
- [var kDNSServiceInterfaceIndexUnicast: UInt32](kdnsserviceinterfaceindexunicast.md)
- [var kDNSServiceMaxDomainName: Int32](kdnsservicemaxdomainname.md)
- [var kDNSServiceMaxServiceName: Int32](kdnsservicemaxservicename.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/kdnsserviceproperty_daemonversion)*