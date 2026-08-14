# WINetworkSharingAskToShareState

**Framework**: Wi-Fi Infrastructure  
**Kind**: enum

The authorization state for sharing the current Wi-Fi network with an accessory.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
enum WINetworkSharingAskToShareState
```

#### Overview

Use this type to track whether the person allowed the accessory to join the Wi-Fi network that the device is currently using.

## Topics

### Checking authorization state
- [WINetworkSharingAskToShareState.undetermined](winetworksharingasktosharestate/undetermined.md)
  The person hasn’t decided whether to share the network with the accessory.
- [WINetworkSharingAskToShareState.denied](winetworksharingasktosharestate/denied.md)
  The person chose not to share the network with the accessory.
- [WINetworkSharingAskToShareState.approved](winetworksharingasktosharestate/approved.md)
  The person allowed the accessory to use the network.

## Relationships

### Conforms To
- [CaseIterable](../swift/caseiterable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class WINetworkSharingController](winetworksharingcontroller.md)
  A controller that enables your container app to control network-sharing functions with connected accessories.
- [class WINetworkSharingProvider](winetworksharingprovider.md)
  A provider that delivers updated Wi-Fi network information to your app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingasktosharestate)*