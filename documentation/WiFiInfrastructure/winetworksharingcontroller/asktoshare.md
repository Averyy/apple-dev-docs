# askToShare()

**Framework**: Wi-Fi Infrastructure  
**Kind**: method

Signals your app extension to run and process the request to share a network.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
func askToShare() async throws -> WINetworkSharingAskToShareState
```

#### Discussion

Call this method to prompt your app extension to ask the person to share new networks. Your app extension can request network sharing in several ways:

- The system indicates when a new network is available that a person can share with your accessory, if the person approves. Your app extension can check with your accessory to confirm whether it needs another network, and if so, call the API to present the request.
- Your accessory communicates with your app extension directly and asks it to present a sharing request. This is useful if your accessory has problems connecting to a network.
- Your container app calls this API to signal your app extension to ask the person for a network. This is useful if your app has a button the person can press to add a network to the accessory.

If the person authorizes the system to “Automatically Share” networks to your accessory, the system shares networks to your accessory without any prompting.

> ❗ **Important**: Your container app needs to run in the foreground to submit a new sharing request to your app extension using this API.

– Returns: The [`WINetworkSharingAskToShareState`](winetworksharingasktosharestate.md), indicating a response from the person.

> **Note**: A [`WINetworkSharingError`](winetworksharingerror.md) for various conditions: - [`WINetworkSharingError.appNotInForeground`](winetworksharingerror/appnotinforeground.md): The container app can’t submit a new sharing request because it’s not in the foreground.
- [`WINetworkSharingError.timeout`](winetworksharingerror/timeout.md): Your app extension didn’t call the [`presentAskToShareUI(scanProvider:)`](winetworksharingprovider/presentasktoshareui(scanprovider:).md) API in response to this call.
- [`WINetworkSharingError.accessoryNotAuthorized`](winetworksharingerror/accessorynotauthorized.md): The person hasn’t authorized to share network data to the accessory.
- [`WINetworkSharingError.accessoryNotConnected`](winetworksharingerror/accessorynotconnected.md): The accessory isn’t connected when your container app calls this method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingcontroller/asktoshare())*