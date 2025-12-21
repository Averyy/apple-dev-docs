# WINetworkSharingProvider.Network.CaptivePortalLogin

**Framework**: Wi-Fi Infrastructure  
**Kind**: struct

Captive portal login information for a Wi-Fi network.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
struct CaptivePortalLogin
```

#### Overview

Contains form data that people previously entered to complete captive portal authentication.

## Topics

### Instance Properties
- [var description: String](winetworksharingprovider/network/captiveportallogin-swift.struct/description.md)
  A string description of the captive portal login information, for debugging purposes.
- [let userEnteredFormValues: [String : String]](winetworksharingprovider/network/captiveportallogin-swift.struct/userenteredformvalues.md)
  The user-entered form values to complete captive portal login.

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
- [WINetworkSharingProvider.Network.Credentials](winetworksharingprovider/network/credentials-swift.enum.md)
  Credentials for authenticating to a Wi-Fi network.
- [let captivePortalLogin: WINetworkSharingProvider.Network.CaptivePortalLogin?](winetworksharingprovider/network/captiveportallogin-swift.property.md)
  The captive portal login information for the network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/network/captiveportallogin-swift.struct)*