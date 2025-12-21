# WINetworkSharingController.AuthorizationState

**Framework**: Wi-Fi Infrastructure  
**Kind**: enum

An enumeration that represents the authorization state for sharing Wi-Fi networks with a given accessory.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
enum AuthorizationState
```

#### Overview

Use `AuthorizationState` to determine the current permission level for Wi-Fi network sharing between the person’s device and a connected accessory. This enum helps you understand whether the person has granted, denied, or not yet decided on Wi-Fi sharing permissions.

Check the authorization state before attempting to share Wi-Fi credentials with an accessory. Handle each state appropriately in your app’s user interface to provide clear feedback about the current sharing permissions.

## Topics

### Checking authorization state
- [WINetworkSharingController.AuthorizationState.undetermined](winetworksharingcontroller/authorizationstate/undetermined.md)
  The person has not yet made a choice about sharing Wi-Fi networks with the accessory.
- [WINetworkSharingController.AuthorizationState.denied](winetworksharingcontroller/authorizationstate/denied.md)
  The person has chosen not to share Wi-Fi networks with the accessory.
- [WINetworkSharingController.AuthorizationState.askToShare](winetworksharingcontroller/authorizationstate/asktoshare.md)
  The person has granted authorization to share Wi-Fi networks with the accessory, but you must request approval for each network individually.
- [WINetworkSharingController.AuthorizationState.automatic](winetworksharingcontroller/authorizationstate/automatic.md)
  The person has granted authorization to share Wi-Fi networks with the accessory automatically, without requiring approval for each network.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func requestAuthorization() async throws -> WINetworkSharingController.AuthorizationState](winetworksharingcontroller/requestauthorization.md)
  Requests network-sharing authorization for the specified accessory at initial setup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingcontroller/authorizationstate)*