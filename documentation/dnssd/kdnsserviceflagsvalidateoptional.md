# kDNSServiceFlagsValidateOptional

**Framework**: dnssd  
**Kind**: var

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
var kDNSServiceFlagsValidateOptional: UInt32 { get }
```

#### Discussion

This flag is identical to kDNSServiceFlagsValidate except for the case where the response cannot be validated. If this flag is set in DNSServiceQueryRecord or DNSServiceGetAddrInfo, the DNSSEC records will be requested for validation. If they cannot be received for some reason during the validation (e.g., zone is not signed, zone is signed but cannot be traced back to root, recursive server does not understand DNSSEC etc.), then this falls back to the default behavior where the validation is not performed and no DNSSEC results are provided.

If the zone is signed and there is a valid path to a known trust anchor configured in the system and the application requires DNSSEC validation irrespective of the DNSSEC awareness in the current network, then this option MUST not be used. This is only intended to be used during the transition period where the different nodes participating in the DNS resolution may not understand DNSSEC or managed properly (e.g. missing DS record) but still want to be able to resolve DNS successfully.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dnssd/kdnsserviceflagsvalidateoptional)*