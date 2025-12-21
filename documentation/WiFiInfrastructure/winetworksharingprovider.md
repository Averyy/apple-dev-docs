# WINetworkSharingProvider

**Framework**: Wi-Fi Infrastructure  
**Kind**: class

A provider that delivers updated Wi-Fi network information to your app extension.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
class WINetworkSharingProvider
```

#### Overview

Use `WINetworkSharingProvider` to receive real-time updates about Wi-Fi networks the system shares with connected accessories and to present network sharing interfaces to people. The provider manages the lifecycle of network-sharing operations and coordinates between your app extension, the system, and connected accessories.

The provider delivers network updates through an async sequence that you can filter and process according to your app’s needs. Each event contains the current state of the shared networks, along with flags indicating when new networks become available or when your container app requests sharing. When networks become available for sharing or when your accessory needs additional networks, use the provider to present system UI that allows people to select and share networks. The interface can integrate with your accessory’s scan results to show signal strength and compatibility information.

> ❗ **Important**: Your `WiFiNetworkSharing` app extension can only use the methods in this class. The extension needs both the [`com.apple.developer.wifi-infrastructure`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.wifi-infrastructure) entitlement with the `WiFiNetworkSharing` capability declared and the [`com.apple.developer.accessory-transport-extension`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.accessory-transport-extension) entitlement.

## Topics

### Getting accessory data
- [let accessory: ASAccessory](winetworksharingprovider/accessory.md)
  The accessory that receives the shared networks.
### Getting network updates
- [func networkEvents(matching: Predicate<WINetworkSharingProvider.Network>?) -> some Sendable & AsyncSequence<WINetworkSharingProvider.NetworkEvent, any Error>
](winetworksharingprovider/networkevents(matching:).md)
  Returns an async sequence of network events, containing current shared networks and future updates.
- [WINetworkSharingProvider.NetworkEvent](winetworksharingprovider/networkevent.md)
  An event that occurred, indicating an update to the available shared networks.
- [WINetworkSharingProvider.Network](winetworksharingprovider/network.md)
  A Wi-Fi network to share with a connected accessory.
### Displaying network selection
- [func presentAskToShareUI(scanProvider: ((ASAccessory, WINetworkSharingProvider.AccessoryScanRequest) async -> WINetworkSharingProvider.AccessoryScanResponse?)?) async throws -> WINetworkSharingAskToShareState](winetworksharingprovider/presentasktoshareui(scanprovider:).md)
  Presents system UI asking people to share available networks with an accessory.
- [WINetworkSharingProvider.AccessoryScanRequest](winetworksharingprovider/accessoryscanrequest.md)
  A request for the accessory to scan for available Wi-Fi networks.
- [WINetworkSharingProvider.AccessoryScanResponse](winetworksharingprovider/accessoryscanresponse.md)
  A scan response from the accessory containing Wi-Fi scan results, if any.
- [WINetworkSharingProvider.AccessoryScanResult](winetworksharingprovider/accessoryscanresult.md)
  An access point that the accessory was able to discover in its Wi-Fi scans.
### Initializers
- [init(for: ASAccessory) async throws](winetworksharingprovider/init(for:).md)
  Creates a provider for the specified accessory.

## See Also

- [class WINetworkSharingController](winetworksharingcontroller.md)
  A controller that enables your container app to control network-sharing functions with connected accessories.
- [enum WINetworkSharingAskToShareState](winetworksharingasktosharestate.md)
  The authorization state for sharing the current Wi-Fi network with an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider)*