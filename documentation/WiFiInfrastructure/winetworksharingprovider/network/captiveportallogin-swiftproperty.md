# captivePortalLogin

**Framework**: Wi-Fi Infrastructure  
**Kind**: property

The captive portal login information for the network.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
let captivePortalLogin: WINetworkSharingProvider.Network.CaptivePortalLogin?
```

#### Discussion

Contains data when the person previously completed captive portal authentication, or `nil` when this network doesn’t require captive portal login.

## See Also

- [let securityPolicy: Set<WINetworkSharingProvider.Network.SecurityPolicy>](winetworksharingprovider/network/securitypolicy-swift.property.md)
  The set of security types allowed for connecting to this network.
- [WINetworkSharingProvider.Network.SecurityPolicy](winetworksharingprovider/network/securitypolicy-swift.enum.md)
  The security policies allowed for connecting to a Wi-Fi network.
- [let credentials: WINetworkSharingProvider.Network.Credentials](winetworksharingprovider/network/credentials-swift.property.md)
  The credentials the accessory needs to connect to this network.
- [WINetworkSharingProvider.Network.Credentials](winetworksharingprovider/network/credentials-swift.enum.md)
  Credentials for authenticating to a Wi-Fi network.
- [WINetworkSharingProvider.Network.CaptivePortalLogin](winetworksharingprovider/network/captiveportallogin-swift.struct.md)
  Captive portal login information for a Wi-Fi network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/network/captiveportallogin-swift.property)*