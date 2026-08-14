# WINetworkSharingProvider.AccessPointConnection.Link

**Framework**: Wi-Fi Infrastructure  
**Kind**: struct

A data link to a Wi-Fi Access Point.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
struct Link
```

#### Overview

WiFi 7 (and later) clients and Access Points may have multiple concurrent data links between them.

## Topics

### Structures
- [WINetworkSharingProvider.AccessPointConnection.Link.ID](winetworksharingprovider/accesspointconnection/link/id-swift.struct.md)
  An opaque identifier for a given link.
### Instance Properties
- [let bssidHash: WIMACAddress.Hash](winetworksharingprovider/accesspointconnection/link/bssidhash.md)
  A hash of the Access Point’s BSSID, which can be used to find this access point link in the environment.
- [let channel: WIChannel](winetworksharingprovider/accesspointconnection/link/channel.md)
  A channel on which the Access Point is operating.
- [var description: String](winetworksharingprovider/accesspointconnection/link/description.md)
  A string description of the link, for debugging purposes.
- [var id: WINetworkSharingProvider.AccessPointConnection.Link.ID](winetworksharingprovider/accesspointconnection/link/id-swift.property.md)
  A stable per-link ID that can be used to uniquely identify this link. ID will be stable for the lifetime of a given App launch.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/accesspointconnection/link)*