# WINetworkSharingProvider.Network.Credentials.EAPCredentials.TLSConfiguration

**Framework**: Wi-Fi Infrastructure  
**Kind**: struct

Configuration for the TLS protocol.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
struct TLSConfiguration
```

## Topics

### Instance Properties
- [let isCertificateRequired: Bool](winetworksharingprovider/network/credentials-swift.enum/eapcredentials/tlsconfiguration-swift.struct/iscertificaterequired.md)
  A Boolean value that indicates whether the configuration allows two-factor authentication for specific Transport Layer Security (TLS) configurations.
- [let maximumTLSVersion: WINetworkSharingProvider.Network.Credentials.EAPCredentials.TLSConfiguration.TLSVersion?](winetworksharingprovider/network/credentials-swift.enum/eapcredentials/tlsconfiguration-swift.struct/maximumtlsversion.md)
  The newest version of Transport Layer Security (TLS) that this configuration accepts to authenticate this network.
- [let minimumTLSVersion: WINetworkSharingProvider.Network.Credentials.EAPCredentials.TLSConfiguration.TLSVersion?](winetworksharingprovider/network/credentials-swift.enum/eapcredentials/tlsconfiguration-swift.struct/minimumtlsversion.md)
  The oldest version of Transport Layer Security (TLS) that this configuration accepts to authenticate this network.
### Enumerations
- [WINetworkSharingProvider.Network.Credentials.EAPCredentials.TLSConfiguration.TLSVersion](winetworksharingprovider/network/credentials-swift.enum/eapcredentials/tlsconfiguration-swift.struct/tlsversion.md)
  Values that define the version of the Transport Layer Security (TLS) protocol to use with EAP authentication.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/network/credentials-swift.enum/eapcredentials/tlsconfiguration-swift.struct)*