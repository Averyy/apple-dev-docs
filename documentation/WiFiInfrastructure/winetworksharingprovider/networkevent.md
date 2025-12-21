# WINetworkSharingProvider.NetworkEvent

**Framework**: Wi-Fi Infrastructure  
**Kind**: struct

An event that occurred, indicating an update to the available shared networks.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
struct NetworkEvent
```

#### Overview

A `NetworkEvent` provides a snapshot of the current shared network’s state, along with flags indicating system events that might require action from your app extension. Each event contains the complete list of networks currently shared with your accessory.

The event includes Boolean flags that indicate specific conditions:

- New networks available for sharing that people can approve.
- Requests from your container app to present sharing UI.
- Updates to the networks list itself.

Use the sequence number and update counter to track changes and avoid processing duplicate events. The timestamp provides context, but don’t use it for precise change detection due to potential clock variations.

## Topics

### Identifying an event
- [WINetworkSharingProvider.NetworkEvent.ID](winetworksharingprovider/networkevent/id-swift.typealias.md)
  The type of value that uniquely identifies this event.
- [var id: WINetworkSharingProvider.NetworkEvent.ID](winetworksharingprovider/networkevent/id-swift.property.md)
  A stable identifier that uniquely identifies this event.
### Getting network data
- [let networks: [WINetworkSharingProvider.Network]](winetworksharingprovider/networkevent/networks.md)
  The latest network data, containing a list of all networks shared to the device.
- [let networksUpdateCounter: UInt64](winetworksharingprovider/networkevent/networksupdatecounter.md)
  A counter that increments whenever the network data changes.
### Getting event signals
- [let newShareableNetworkAvailable: Bool](winetworksharingprovider/networkevent/newshareablenetworkavailable.md)
  A Boolean value that indicates whether the system detected available networks your app extension may request from people.
- [let appRequestedSharing: Bool](winetworksharingprovider/networkevent/apprequestedsharing.md)
  A Boolean value that indicates whether the container app requested network sharing.
### Getting the event time
- [let timestamp: Date](winetworksharingprovider/networkevent/timestamp.md)
  The date when this event occurred.
### Getting the event description
- [var description: String](winetworksharingprovider/networkevent/description.md)
  A string description of the event, for debugging purposes.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func networkEvents(matching: Predicate<WINetworkSharingProvider.Network>?) -> some Sendable & AsyncSequence<WINetworkSharingProvider.NetworkEvent, any Error>
](winetworksharingprovider/networkevents(matching:).md)
  Returns an async sequence of network events, containing current shared networks and future updates.
- [WINetworkSharingProvider.Network](winetworksharingprovider/network.md)
  A Wi-Fi network to share with a connected accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/networkevent)*