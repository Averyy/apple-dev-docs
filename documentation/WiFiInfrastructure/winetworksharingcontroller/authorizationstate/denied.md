# WINetworkSharingController.AuthorizationState.denied

**Framework**: Wi-Fi Infrastructure  
**Kind**: case  
**Role**: Case

The person has chosen not to share Wi-Fi networks with the accessory.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
case denied
```

## See Also

### Checking authorization state
- [WINetworkSharingController.AuthorizationState.undetermined](./undetermined.md)
  The person has not yet made a choice about sharing Wi-Fi networks with the accessory.
- [WINetworkSharingController.AuthorizationState.askToShare](./asktoshare.md)
  The person has granted authorization to share Wi-Fi networks with the accessory, but you must request approval for each network individually.
- [WINetworkSharingController.AuthorizationState.automatic](./automatic.md)
  The person has granted authorization to share Wi-Fi networks with the accessory automatically, without requiring approval for each network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingcontroller/authorizationstate/denied)*