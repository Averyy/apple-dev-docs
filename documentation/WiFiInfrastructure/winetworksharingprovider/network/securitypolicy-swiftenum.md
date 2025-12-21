# WINetworkSharingProvider.Network.SecurityPolicy

**Framework**: Wi-Fi Infrastructure  
**Kind**: enum

The security policies allowed for connecting to a Wi-Fi network.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
enum SecurityPolicy
```

## Topics

### Enumeration Cases
- [WINetworkSharingProvider.Network.SecurityPolicy.open](winetworksharingprovider/network/securitypolicy-swift.enum/open.md)
  Allows open network security, with no authentication or encryption.
- [WINetworkSharingProvider.Network.SecurityPolicy.owe](winetworksharingprovider/network/securitypolicy-swift.enum/owe.md)
  Allows Opportunistic Wireless Encryption (OWE).
- [WINetworkSharingProvider.Network.SecurityPolicy.wep](winetworksharingprovider/network/securitypolicy-swift.enum/wep.md)
  Allows WEP encryption.
- [WINetworkSharingProvider.Network.SecurityPolicy.wpa](winetworksharingprovider/network/securitypolicy-swift.enum/wpa.md)
  Allows WPA Personal authentication.
- [WINetworkSharingProvider.Network.SecurityPolicy.wpa2](winetworksharingprovider/network/securitypolicy-swift.enum/wpa2.md)
  Allows WPA2 Personal authentication.
- [WINetworkSharingProvider.Network.SecurityPolicy.wpa3](winetworksharingprovider/network/securitypolicy-swift.enum/wpa3.md)
  Allows WPA3-SAE authentication.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let securityPolicy: Set<WINetworkSharingProvider.Network.SecurityPolicy>](winetworksharingprovider/network/securitypolicy-swift.property.md)
  The set of security types allowed for connecting to this network.
- [let credentials: WINetworkSharingProvider.Network.Credentials](winetworksharingprovider/network/credentials-swift.property.md)
  The credentials the accessory needs to connect to this network.
- [WINetworkSharingProvider.Network.Credentials](winetworksharingprovider/network/credentials-swift.enum.md)
  Credentials for authenticating to a Wi-Fi network.
- [let captivePortalLogin: WINetworkSharingProvider.Network.CaptivePortalLogin?](winetworksharingprovider/network/captiveportallogin-swift.property.md)
  The captive portal login information for the network.
- [WINetworkSharingProvider.Network.CaptivePortalLogin](winetworksharingprovider/network/captiveportallogin-swift.struct.md)
  Captive portal login information for a Wi-Fi network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/network/securitypolicy-swift.enum)*