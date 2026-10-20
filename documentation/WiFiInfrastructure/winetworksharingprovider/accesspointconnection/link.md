# WINetworkSharingProvider.AccessPointConnection.Link

**Framework**: Wi-Fi Infrastructure  
**Kind**: struct  
**Role**: Structure

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
- [WINetworkSharingProvider.AccessPointConnection.Link.ID](./link/id-swift.struct.md)
  An opaque identifier for a given link.
### Instance Properties
- [let bssidHash: WIMACAddress.Hash](./link/bssidhash.md)
  A hash of the Access Point’s BSSID, which can be used to find this access point link in the environment.
- [let channel: WIChannel](./link/channel.md)
  A channel on which the Access Point is operating.
- [var description: String](./link/description.md)
  A string description of the link, for debugging purposes.
- [var id: WINetworkSharingProvider.AccessPointConnection.Link.ID](./link/id-swift.property.md)
  A stable per-link ID that can be used to uniquely identify this link. ID will be stable for the lifetime of a given App launch.

## Relationships

### Conforms To
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Identifiable](../../../Swift/identifiable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/accesspointconnection/link)*