# WINetworkSharingProvider.Network.Credentials.EAPCredentials

**Framework**: Wi-Fi Infrastructure  
**Kind**: struct

A structure containing the credentials for a Wi-Fi network with 802.1x enterprise authentication.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
struct EAPCredentials
```

## Topics

### Structures
- [WINetworkSharingProvider.Network.Credentials.EAPCredentials.ClientIdentity](winetworksharingprovider/network/credentials-swift.enum/eapcredentials/clientidentity-swift.struct.md)
  A structure that represents the client’s identity.
- [WINetworkSharingProvider.Network.Credentials.EAPCredentials.FASTConfiguration](winetworksharingprovider/network/credentials-swift.enum/eapcredentials/fastconfiguration-swift.struct.md)
  Configuration for EAP-FAST.
- [WINetworkSharingProvider.Network.Credentials.EAPCredentials.TLSConfiguration](winetworksharingprovider/network/credentials-swift.enum/eapcredentials/tlsconfiguration-swift.struct.md)
  Configuration for the TLS protocol.
- [WINetworkSharingProvider.Network.Credentials.EAPCredentials.TTLSConfiguration](winetworksharingprovider/network/credentials-swift.enum/eapcredentials/ttlsconfiguration-swift.struct.md)
  The configuration for authentication that uses EAP-TTLS.
- [WINetworkSharingProvider.Network.Credentials.EAPCredentials.TrustedServers](winetworksharingprovider/network/credentials-swift.enum/eapcredentials/trustedservers-swift.struct.md)
  A structure that describes trusted authentication servers.
- [WINetworkSharingProvider.Network.Credentials.EAPCredentials.UserLogin](winetworksharingprovider/network/credentials-swift.enum/eapcredentials/userlogin-swift.struct.md)
  A person’s login information.
### Instance Properties
- [let acceptedEAPTypes: Set<WINetworkSharingProvider.Network.Credentials.EAPCredentials.EAPType>](winetworksharingprovider/network/credentials-swift.enum/eapcredentials/acceptedeaptypes.md)
  The EAP types allowed for this network.
- [let clientIdentity: WINetworkSharingProvider.Network.Credentials.EAPCredentials.ClientIdentity?](winetworksharingprovider/network/credentials-swift.enum/eapcredentials/clientidentity-swift.property.md)
  The information used to authenticate the client’s identity.
- [let fastConfiguration: WINetworkSharingProvider.Network.Credentials.EAPCredentials.FASTConfiguration?](winetworksharingprovider/network/credentials-swift.enum/eapcredentials/fastconfiguration-swift.property.md)
  The configuration to use for EAP-FAST.
- [let outerIdentity: String?](winetworksharingprovider/network/credentials-swift.enum/eapcredentials/outeridentity.md)
  A name that hides the user’s actual name.
- [let tlsConfiguration: WINetworkSharingProvider.Network.Credentials.EAPCredentials.TLSConfiguration?](winetworksharingprovider/network/credentials-swift.enum/eapcredentials/tlsconfiguration-swift.property.md)
  The configuration to use for Transport Layer Security (TLS).
- [let trustedServers: WINetworkSharingProvider.Network.Credentials.EAPCredentials.TrustedServers](winetworksharingprovider/network/credentials-swift.enum/eapcredentials/trustedservers-swift.property.md)
  The information used to authenticate the server.
- [let ttlsConfiguration: WINetworkSharingProvider.Network.Credentials.EAPCredentials.TTLSConfiguration?](winetworksharingprovider/network/credentials-swift.enum/eapcredentials/ttlsconfiguration-swift.property.md)
  The configuration to use for Tunneled Transport Layer Security (TTLS).
- [let userLogin: WINetworkSharingProvider.Network.Credentials.EAPCredentials.UserLogin?](winetworksharingprovider/network/credentials-swift.enum/eapcredentials/userlogin-swift.property.md)
  The information used authenticate the user and log them in.
### Enumerations
- [WINetworkSharingProvider.Network.Credentials.EAPCredentials.EAPType](winetworksharingprovider/network/credentials-swift.enum/eapcredentials/eaptype.md)
  The EAP types allowed for this network

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/network/credentials-swift.enum/eapcredentials)*