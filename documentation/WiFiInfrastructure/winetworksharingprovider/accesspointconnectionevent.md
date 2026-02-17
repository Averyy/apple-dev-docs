# WINetworkSharingProvider.AccessPointConnectionEvent

**Framework**: Wi-Fi Infrastructure  
**Kind**: struct

An event that occurred, indicating an update to the available shared access points.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
struct AccessPointConnectionEvent
```

#### Overview

An `AccessPointConnectionEvent` provides a snapshot of changes to the currently connected Access Point(s) that might require action from your app extension. Each event contains the complete list of access point(s) the host is currently connected to, and which may be shared with your accessory.

Use the sequence number and update counter to track changes and avoid processing duplicate events. The timestamp provides context but shouldn’t be used for precise change detection due to potential clock variations.

## Topics

### Instance Properties
- [let accessPointConnections: [WINetworkSharingProvider.AccessPointConnection]](winetworksharingprovider/accesspointconnectionevent/accesspointconnections.md)
  A list of access points to which the host connects for networks someone authorized to share to the device.
- [let accessPointConnectionsUpdateCounter: UInt64](winetworksharingprovider/accesspointconnectionevent/accesspointconnectionsupdatecounter.md)
  A counter that increments whenever the access point data changes.
- [var description: String](winetworksharingprovider/accesspointconnectionevent/description.md)
  A string description of the event for debugging purposes.
- [var id: WINetworkSharingProvider.AccessPointConnectionEvent.ID](winetworksharingprovider/accesspointconnectionevent/id-swift.property.md)
  A stable identifier that uniquely identifies this event.
- [let timestamp: Date](winetworksharingprovider/accesspointconnectionevent/timestamp.md)
  The date when this event occurred.
### Type Aliases
- [WINetworkSharingProvider.AccessPointConnectionEvent.ID](winetworksharingprovider/accesspointconnectionevent/id-swift.typealias.md)
  The type of value that uniquely identifies this event.

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

- [WINetworkSharingProvider.AccessPointConnection](winetworksharingprovider/accesspointconnection.md)
  A Wi-Fi access point the host is currently connected to, which may be shared with a connected accessory.
- [func accessPointConnectionEvents(matching: Predicate<WINetworkSharingProvider.AccessPointConnection>?) -> some Sendable & AsyncSequence<WINetworkSharingProvider.AccessPointConnectionEvent, any Error>
](winetworksharingprovider/accesspointconnectionevents(matching:).md)
  Returns an async sequence of access point events containing the currently connected access point(s) and future updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/accesspointconnectionevent)*