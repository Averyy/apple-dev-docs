# WINetworkSharingController

**Framework**: Wi-Fi Infrastructure  
**Kind**: class

A controller that enables your container app to control network-sharing functions with connected accessories.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
class WINetworkSharingController
```

#### Overview

Use the `WINetworkSharingController` class to request authorization for Wi-Fi network sharing and to prompt people to share networks with their accessories. This class manages the interaction between your container app and the system’s network-sharing infrastructure.

> ❗ **Important**: Only your container app can call the methods in this object. Your app needs the `com.apple.developer.wifi-infrastructure` entitlement with the `WiFiNetworkSharing` capability declared.

## Topics

### Getting the controlled accessory
- [let accessory: ASAccessory](winetworksharingcontroller/accessory.md)
  The accessory whose network-sharing features your container app controls.
### Authorizing an accessory for network sharing
- [func requestAuthorization() async throws -> WINetworkSharingController.AuthorizationState](winetworksharingcontroller/requestauthorization.md)
  Requests network-sharing authorization for the specified accessory at initial setup.
- [WINetworkSharingController.AuthorizationState](winetworksharingcontroller/authorizationstate.md)
  An enumeration that represents the authorization state for sharing Wi-Fi networks with a given accessory.
### Signaling your App Extension to ask for a network
- [func askToShare() async throws -> WINetworkSharingAskToShareState](winetworksharingcontroller/asktoshare.md)
  Signals your app extension to run and process the request to share a network.
### Initializers
- [init(for: ASAccessory) async throws](winetworksharingcontroller/init(for:).md)
  Creates a controller for a given accessory.

## See Also

- [class WINetworkSharingProvider](winetworksharingprovider.md)
  A provider that delivers updated Wi-Fi network information to your app extension.
- [enum WINetworkSharingAskToShareState](winetworksharingasktosharestate.md)
  The authorization state for sharing the current Wi-Fi network with an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingcontroller)*