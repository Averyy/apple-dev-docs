# WINetworkSharingProvider.NetworkEvent

**Framework**: Wi-Fi Infrastructure  
**Kind**: struct  
**Role**: Structure

An event that occurred, indicating an update to the available shared networks.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
struct NetworkEvent
```

## Overview

A `NetworkEvent` provides a snapshot of the current shared network’s state, along with flags indicating system events that might require action from your app extension. Each event contains the complete list of networks currently shared with your accessory.

The event includes Boolean flags that indicate specific conditions:

- New networks available for sharing that people can approve.
- Requests from your container app to present sharing UI.
- Updates to the networks list itself.

Use the sequence number and update counter to track changes and avoid processing duplicate events. The timestamp provides context, but don’t use it for precise change detection due to potential clock variations.

## Topics

### Identifying an event
- [WINetworkSharingProvider.NetworkEvent.ID](./networkevent/id-swift.typealias.md)
  The type of value that uniquely identifies this event.
- [var id: WINetworkSharingProvider.NetworkEvent.ID](./networkevent/id-swift.property.md)
  A stable identifier that uniquely identifies this event.
### Getting network data
- [let networks: [WINetworkSharingProvider.Network]](./networkevent/networks.md)
  The latest network data, containing a list of all networks shared to the device.
- [let networksUpdateCounter: UInt64](./networkevent/networksupdatecounter.md)
  A counter that increments whenever the network data changes.
### Getting event signals
- [let newShareableNetworkAvailable: Bool](./networkevent/newshareablenetworkavailable.md)
  A Boolean value that indicates whether the system detected available networks your app extension may request from people.
- [let appRequestedSharing: Bool](./networkevent/apprequestedsharing.md)
  A Boolean value that indicates whether the container app requested network sharing.
### Getting the event time
- [let timestamp: Date](./networkevent/timestamp.md)
  The date when this event occurred.
### Getting the event description
- [var description: String](./networkevent/description.md)
  A string description of the event, for debugging purposes.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Identifiable](../../Swift/identifiable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting network updates
- [func networkEvents(matching: Predicate<WINetworkSharingProvider.Network>?) -> some Sendable & AsyncSequence<WINetworkSharingProvider.NetworkEvent, any Error>
](./networkevents%28matching%29.md)
  Returns an async sequence of network events, containing current shared networks and future updates.
- [WINetworkSharingProvider.Network](./network.md)
  A Wi-Fi network to share with a connected accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/networkevent)*