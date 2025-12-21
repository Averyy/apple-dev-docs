# presentAskToShareUI(scanProvider:)

**Framework**: Wi-Fi Infrastructure  
**Kind**: method

Presents system UI asking people to share available networks with an accessory.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
func presentAskToShareUI(scanProvider: ((ASAccessory, WINetworkSharingProvider.AccessoryScanRequest) async -> WINetworkSharingProvider.AccessoryScanResponse?)? = nil) async throws -> WINetworkSharingAskToShareState
```

#### Return Value

The [`WINetworkSharingAskToShareState`](winetworksharingasktosharestate.md), indicating a response from the person.

#### Discussion

Call this method when your accessory needs additional networks or when the system indicates new shareable networks are available. The system checks for nearby known networks and prompts people to select networks to share with your accessory.

Your app extension can present sharing UI in these scenarios:

- : The system sets `newShareableNetworkAvailable` to `true` when networks become available for sharing. Your extension can verify with your accessory whether it needs additional networks before calling this method. Your container app doesn’t need to be in the foreground for this scenario.
- : Your accessory can communicate directly with your extension to request network sharing, such as when connection problems occur. Your container app needs to be in the foreground before calling this method.
- : Your container app can call [`askToShare()`](winetworksharingcontroller/asktoshare().md) to set the [`appRequestedSharing`](winetworksharingprovider/networkevent/apprequestedsharing.md) flag, indicating it wants your extension to present sharing UI. Your container app needs to be in the foreground before calling this method.

> ❗ **Important**: When people choose to “Automatically Share” networks, the system adds new networks to future [`networks`](winetworksharingprovider/networkevent/networks.md) without needing additional calls to this method or further approval.

> **Note**: [`WINetworkSharingError`](winetworksharingerror.md) for various conditions: - [`WINetworkSharingError.timeout`](winetworksharingerror/timeout.md): The person didn’t respond to the request.
- [`WINetworkSharingError.noAvailableNetworks`](winetworksharingerror/noavailablenetworks.md): No shareable networks were available nearby.
- [`WINetworkSharingError.appNotInForeground`](winetworksharingerror/appnotinforeground.md): Called when [`newShareableNetworkAvailable`](winetworksharingprovider/networkevent/newshareablenetworkavailable.md) is false and the container app isn’t in the foreground.
- [`WINetworkSharingError.accessoryNotAuthorized`](winetworksharingerror/accessorynotauthorized.md): The person hasn’t authorized network data sharing to the accessory.
- [`WINetworkSharingError.accessoryNotConnected`](winetworksharingerror/accessorynotconnected.md): The accessory isn’t connected when making this request.

## Parameters

- `scanProvider`: The optional closure the system calls periodically to get updated scan results   from the accessory. Returns networks your accessory discovers to help people select compatible,   high-performance networks. Defaults to   when your accessory provides no scan information.   The closure receives:

## See Also

- [WINetworkSharingProvider.AccessoryScanRequest](winetworksharingprovider/accessoryscanrequest.md)
  A request for the accessory to scan for available Wi-Fi networks.
- [WINetworkSharingProvider.AccessoryScanResponse](winetworksharingprovider/accessoryscanresponse.md)
  A scan response from the accessory containing Wi-Fi scan results, if any.
- [WINetworkSharingProvider.AccessoryScanResult](winetworksharingprovider/accessoryscanresult.md)
  An access point that the accessory was able to discover in its Wi-Fi scans.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/presentasktoshareui(scanprovider:))*