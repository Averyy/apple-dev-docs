# WINetworkSharingProvider.AccessPointConnectionEvent

**Framework**: Wi-Fi Infrastructure  
**Kind**: struct  
**Role**: Structure

An event that indicates an update to the available shared access points.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
struct AccessPointConnectionEvent
```

#### Discussion

An `AccessPointConnectionEvent` provides a snapshot of changes to one or more of the currently connected access points that might require action from your app extension. Each event contains the complete list of access points to which the host is currently connected; your app may share this list with your accessory.

Use the sequence number and update counter to track changes and avoid processing duplicate events. The timestamp provides context but it is recommended you don’t use it for precise change detection due to potential clock variations.

## Topics

### Instance Properties
- [let accessPointConnections: [WINetworkSharingProvider.AccessPointConnection]](./accesspointconnectionevent/accesspointconnections.md)
  A list of access points to which the host connects for networks someone authorized to share to the device.
- [let accessPointConnectionsUpdateCounter: UInt64](./accesspointconnectionevent/accesspointconnectionsupdatecounter.md)
  A counter that increments whenever the access point data changes.
- [var description: String](./accesspointconnectionevent/description.md)
  A string description of the event for debugging purposes.
- [var id: WINetworkSharingProvider.AccessPointConnectionEvent.ID](./accesspointconnectionevent/id-swift.property.md)
  A stable identifier that uniquely identifies this event.
- [let timestamp: Date](./accesspointconnectionevent/timestamp.md)
  The date when this event occurred.
### Type Aliases
- [WINetworkSharingProvider.AccessPointConnectionEvent.ID](./accesspointconnectionevent/id-swift.typealias.md)
  The type of value that uniquely identifies this event.

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

### Getting information about access point connections
- [WINetworkSharingProvider.AccessPointConnection](./accesspointconnection.md)
  A Wi-Fi access point the host is currently connected to, which may be shared with a connected accessory.
- [func accessPointConnectionEvents(matching: Predicate<WINetworkSharingProvider.AccessPointConnection>?) -> some Sendable & AsyncSequence<WINetworkSharingProvider.AccessPointConnectionEvent, any Error>
](./accesspointconnectionevents%28matching%29.md)
  Returns an async sequence of access point events containing the currently connected access point(s) and future updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/accesspointconnectionevent)*