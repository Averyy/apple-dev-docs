# WINetworkSharingProvider.Network.Credentials

**Framework**: Wi-Fi Infrastructure  
**Kind**: enum  
**Role**: Enumeration

Credentials for authenticating to a Wi-Fi network.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
enum Credentials
```

## Topics

### Structures
- [WINetworkSharingProvider.Network.Credentials.EAPCredentials](./credentials-swift.enum/eapcredentials.md)
  A structure containing the credentials for a Wi-Fi network with 802.1x enterprise authentication.
### Enumeration Cases
- [case enterprise(WINetworkSharingProvider.Network.Credentials.EAPCredentials)](./credentials-swift.enum/enterprise%28_%29.md)
  The credentials to login to a network using 802.1x Enterprise authentication.
- [WINetworkSharingProvider.Network.Credentials.none](./credentials-swift.enum/none.md)
  No credentials are available for the Wi-Fi network.
- [WINetworkSharingProvider.Network.Credentials.password(_:)](./credentials-swift.enum/password%28_%29.md)
  A password is available for the Wi-Fi network, with the associated value containing the password.
### Instance Properties
- [var description: String](./credentials-swift.enum/description.md)
  A string description of the credentials, for debugging purposes.

## Relationships

### Conforms To
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting the network credentials
- [let securityPolicy: Set<WINetworkSharingProvider.Network.SecurityPolicy>](./securitypolicy-swift.property.md)
  The set of security types allowed for connecting to this network.
- [WINetworkSharingProvider.Network.SecurityPolicy](./securitypolicy-swift.enum.md)
  The security policies allowed for connecting to a Wi-Fi network.
- [let credentials: WINetworkSharingProvider.Network.Credentials](./credentials-swift.property.md)
  The credentials the accessory needs to connect to this network.
- [let captivePortalLogin: WINetworkSharingProvider.Network.CaptivePortalLogin?](./captiveportallogin-swift.property.md)
  The captive portal login information for the network.
- [WINetworkSharingProvider.Network.CaptivePortalLogin](./captiveportallogin-swift.struct.md)
  Captive portal login information for a Wi-Fi network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/network/credentials-swift.enum)*