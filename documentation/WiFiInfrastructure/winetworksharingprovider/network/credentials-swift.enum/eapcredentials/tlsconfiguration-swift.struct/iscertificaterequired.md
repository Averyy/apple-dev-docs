# isCertificateRequired

**Framework**: Wi-Fi Infrastructure  
**Kind**: property

A Boolean value that indicates whether the configuration allows two-factor authentication for specific Transport Layer Security (TLS) configurations.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
let isCertificateRequired: Bool
```

#### Discussion

If `true`, the configuration allows two-factor authentication for EAP-TTLS, PEAP, or EAP-FAST. If `false`, the configuration allows zero-factor authentication for EAP-TLS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/network/credentials-swift.enum/eapcredentials/tlsconfiguration-swift.struct/iscertificaterequired)*