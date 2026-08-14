# WINetworkSharingProvider.AccessPointConnection

**Framework**: Wi-Fi Infrastructure  
**Kind**: struct

A Wi-Fi access point the host is currently connected to, which may be shared with a connected accessory.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
struct AccessPointConnection
```

## Topics

### Structures
- [WINetworkSharingProvider.AccessPointConnection.ID](winetworksharingprovider/accesspointconnection/id-swift.struct.md)
  An opaque identifier for a given access point.
- [WINetworkSharingProvider.AccessPointConnection.Link](winetworksharingprovider/accesspointconnection/link.md)
  A data link to a Wi-Fi Access Point.
### Instance Properties
- [var description: String](winetworksharingprovider/accesspointconnection/description.md)
  A string description of the access point, for debugging purposes.
- [var id: WINetworkSharingProvider.AccessPointConnection.ID](winetworksharingprovider/accesspointconnection/id-swift.property.md)
  A stable per-access point ID that can be used to uniquely identify this access point. ID will be stable for the lifetime of a given App launch.
- [let links: [WINetworkSharingProvider.AccessPointConnection.Link]](winetworksharingprovider/accesspointconnection/links.md)
  The set of active data links with the Access Point.
- [let ssid: WISSID](winetworksharingprovider/accesspointconnection/ssid.md)
  The access point’s Service Set Identifier (SSID), also known as the network name.

## Relationships

### Conforms To
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Identifiable](../swift/identifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [WINetworkSharingProvider.AccessPointConnectionEvent](winetworksharingprovider/accesspointconnectionevent.md)
  An event that indicates an update to the available shared access points.
- [func accessPointConnectionEvents(matching: Predicate<WINetworkSharingProvider.AccessPointConnection>?) -> some Sendable & AsyncSequence<WINetworkSharingProvider.AccessPointConnectionEvent, any Error>
](winetworksharingprovider/accesspointconnectionevents(matching:).md)
  Returns an async sequence of access point events containing the currently connected access point(s) and future updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/accesspointconnection)*