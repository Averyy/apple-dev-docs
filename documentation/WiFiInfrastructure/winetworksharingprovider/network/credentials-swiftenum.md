# WINetworkSharingProvider.Network.Credentials

**Framework**: Wi-Fi Infrastructure  
**Kind**: enum

Credentials for authenticating to a Wi-Fi network.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
enum Credentials
```

## Topics

### Enumeration Cases
- [WINetworkSharingProvider.Network.Credentials.none](winetworksharingprovider/network/credentials-swift.enum/none.md)
  No credentials are available for the Wi-Fi network.
- [WINetworkSharingProvider.Network.Credentials.password(_:)](winetworksharingprovider/network/credentials-swift.enum/password(_:).md)
  A password is available for the Wi-Fi network, with the associated value containing the password.
### Instance Properties
- [var description: String](winetworksharingprovider/network/credentials-swift.enum/description.md)
  A string description of the credentials, for debugging purposes.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let securityPolicy: Set<WINetworkSharingProvider.Network.SecurityPolicy>](winetworksharingprovider/network/securitypolicy-swift.property.md)
  The set of security types allowed for connecting to this network.
- [WINetworkSharingProvider.Network.SecurityPolicy](winetworksharingprovider/network/securitypolicy-swift.enum.md)
  The security policies allowed for connecting to a Wi-Fi network.
- [let credentials: WINetworkSharingProvider.Network.Credentials](winetworksharingprovider/network/credentials-swift.property.md)
  The credentials the accessory needs to connect to this network.
- [let captivePortalLogin: WINetworkSharingProvider.Network.CaptivePortalLogin?](winetworksharingprovider/network/captiveportallogin-swift.property.md)
  The captive portal login information for the network.
- [WINetworkSharingProvider.Network.CaptivePortalLogin](winetworksharingprovider/network/captiveportallogin-swift.struct.md)
  Captive portal login information for a Wi-Fi network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/network/credentials-swift.enum)*