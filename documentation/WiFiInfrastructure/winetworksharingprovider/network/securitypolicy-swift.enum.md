# WINetworkSharingProvider.Network.SecurityPolicy

**Framework**: Wi-Fi Infrastructure  
**Kind**: enum  
**Role**: Enumeration

The security policies allowed for connecting to a Wi-Fi network.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
enum SecurityPolicy
```

## Topics

### Enumeration Cases
- [WINetworkSharingProvider.Network.SecurityPolicy.open](./securitypolicy-swift.enum/open.md)
  Allows open network security, with no authentication or encryption.
- [WINetworkSharingProvider.Network.SecurityPolicy.owe](./securitypolicy-swift.enum/owe.md)
  Allows Opportunistic Wireless Encryption (OWE), providing encryption without authentication.
- [WINetworkSharingProvider.Network.SecurityPolicy.wep](./securitypolicy-swift.enum/wep.md)
  Allows WEP encryption.
- [WINetworkSharingProvider.Network.SecurityPolicy.wpa](./securitypolicy-swift.enum/wpa.md)
  Allows WPA1 authentication.
- [WINetworkSharingProvider.Network.SecurityPolicy.wpa2](./securitypolicy-swift.enum/wpa2.md)
  Allows WPA2 authentication.
- [WINetworkSharingProvider.Network.SecurityPolicy.wpa3](./securitypolicy-swift.enum/wpa3.md)
  Allows WPA3 authentication.
### Instance Properties
- [var description: String](./securitypolicy-swift.enum/description.md)
  A string description of the security policy, for debugging purposes.

## Relationships

### Conforms To
- [CaseIterable](../../../Swift/caseiterable.md)
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
- [let credentials: WINetworkSharingProvider.Network.Credentials](./credentials-swift.property.md)
  The credentials the accessory needs to connect to this network.
- [WINetworkSharingProvider.Network.Credentials](./credentials-swift.enum.md)
  Credentials for authenticating to a Wi-Fi network.
- [let captivePortalLogin: WINetworkSharingProvider.Network.CaptivePortalLogin?](./captiveportallogin-swift.property.md)
  The captive portal login information for the network.
- [WINetworkSharingProvider.Network.CaptivePortalLogin](./captiveportallogin-swift.struct.md)
  Captive portal login information for a Wi-Fi network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/network/securitypolicy-swift.enum)*