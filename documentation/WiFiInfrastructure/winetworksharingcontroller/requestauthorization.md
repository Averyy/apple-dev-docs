# requestAuthorization()

**Framework**: Wi-Fi Infrastructure  
**Kind**: method

Requests network-sharing authorization for the specified accessory at initial setup.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
func requestAuthorization() async throws -> WINetworkSharingController.AuthorizationState
```

#### Return Value

An [`WINetworkSharingController.AuthorizationState`](winetworksharingcontroller/authorizationstate.md) value indicating the authorization level the person selected.

#### Discussion

Call this method to request that the system ask the person to authorize sharing of Wi-Fi networks to the specified accessory. The person or the system may decline the request.

The person can select from the following sharing modes:

- : The system automatically sends new networks to the accessory when the device joins them while the accessory is connected.
- : When the device joins a new network, the system notifies your extension through the Wi-Fi Infrastructure framework. Your extension can then check [`newShareableNetworkAvailable`](winetworksharingprovider/networkevent/newshareablenetworkavailable.md) and call [`presentAskToShareUI(scanProvider:)`](winetworksharingprovider/presentasktoshareui(scanprovider:).md) to present UI asking the person to share that network.
- : The person declines to share Wi-Fi networks with this accessory.

In the “Automatically Share” and “Ask Every Time” sharing modes, the accessory may request to share a nearby network that’s known to the person. Accessories can use this to prompt a person to share a different network if they have trouble connecting to a previously shared network.

> **Note**: - `accessoryTransportNotSecured` if the accessory is not using a secure Bluetooth transport.
- `accessoryNotConnected` if the accessory isn’t connected when your container app calls this method.
- `WINetworkSharingError` if other faults occur.

## See Also

- [WINetworkSharingController.AuthorizationState](winetworksharingcontroller/authorizationstate.md)
  An enumeration that represents the authorization state for sharing Wi-Fi networks with a given accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingcontroller/requestauthorization())*