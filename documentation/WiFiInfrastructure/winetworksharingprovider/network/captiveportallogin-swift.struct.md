# WINetworkSharingProvider.Network.CaptivePortalLogin

**Framework**: Wi-Fi Infrastructure  
**Kind**: struct  
**Role**: Structure

Captive portal login information for a Wi-Fi network.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
struct CaptivePortalLogin
```

#### Overview

Contains form data that people previously entered to complete captive portal authentication.

## Topics

### Instance Properties
- [var description: String](./captiveportallogin-swift.struct/description.md)
  A string description of the captive portal login information, for debugging purposes.
- [let userEnteredFormValues: [String : String]](./captiveportallogin-swift.struct/userenteredformvalues.md)
  The user-entered form values to complete captive portal login.

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
- [WINetworkSharingProvider.Network.Credentials](./credentials-swift.enum.md)
  Credentials for authenticating to a Wi-Fi network.
- [let captivePortalLogin: WINetworkSharingProvider.Network.CaptivePortalLogin?](./captiveportallogin-swift.property.md)
  The captive portal login information for the network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/network/captiveportallogin-swift.struct)*