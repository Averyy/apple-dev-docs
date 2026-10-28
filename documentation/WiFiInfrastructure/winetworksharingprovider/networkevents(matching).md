# networkEvents(matching:)

**Framework**: Wi-Fi Infrastructure  
**Kind**: method  
**Role**: Instance Method

Returns an async sequence of network events, containing current shared networks and future updates.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
func networkEvents(matching predicate: Predicate<WINetworkSharingProvider.Network>? = nil) -> some Sendable & AsyncSequence<WINetworkSharingProvider.NetworkEvent, any Error>
```

## Return Value

An async sequence that delivers [`WINetworkSharingProvider.NetworkEvent`](./networkevent.md) instances whenever your app extension needs to update its network information or present UI.

## Discussion

Use this method to monitor changes to the shared networks list and respond to system events, like new network availability or sharing requests from your container app.

## Parameters

- `predicate`: An optional predicate for filtering the shared networks list. The default is `nil`, meaning you receive all networks.

## See Also

### Getting network updates
- [WINetworkSharingProvider.NetworkEvent](./networkevent.md)
  An event that occurred, indicating an update to the available shared networks.
- [WINetworkSharingProvider.Network](./network.md)
  A Wi-Fi network to share with a connected accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/networkevents(matching:))*