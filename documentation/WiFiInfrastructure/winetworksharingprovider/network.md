# WINetworkSharingProvider.Network

**Framework**: Wi-Fi Infrastructure  
**Kind**: struct

A Wi-Fi network to share with a connected accessory.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
struct Network
```

## Topics

### Identifying a network
- [var id: WINetworkSharingProvider.Network.ID](winetworksharingprovider/network/id-swift.property.md)
  A stable identifier that uniquely identifies this network.
- [WINetworkSharingProvider.Network.ID](winetworksharingprovider/network/id-swift.struct.md)
  An opaque identifier for a given network.
### Getting the network SSID
- [let ssid: WISSID](winetworksharingprovider/network/ssid.md)
  The Service Set Identifier (SSID) of the network, also known as the network name.
- [let isSSIDBroadcast: Bool](winetworksharingprovider/network/isssidbroadcast.md)
  A Boolean value indicating whether the access point broadcasts the SSID.
### Getting the network credentials
- [let securityPolicy: Set<WINetworkSharingProvider.Network.SecurityPolicy>](winetworksharingprovider/network/securitypolicy-swift.property.md)
  The set of security types allowed for connecting to this network.
- [WINetworkSharingProvider.Network.SecurityPolicy](winetworksharingprovider/network/securitypolicy-swift.enum.md)
  The security policies allowed for connecting to a Wi-Fi network.
- [let credentials: WINetworkSharingProvider.Network.Credentials](winetworksharingprovider/network/credentials-swift.property.md)
  The credentials the accessory needs to connect to this network.
- [WINetworkSharingProvider.Network.Credentials](winetworksharingprovider/network/credentials-swift.enum.md)
  Credentials for authenticating to a Wi-Fi network.
- [let captivePortalLogin: WINetworkSharingProvider.Network.CaptivePortalLogin?](winetworksharingprovider/network/captiveportallogin-swift.property.md)
  The captive portal login information for the network.
- [WINetworkSharingProvider.Network.CaptivePortalLogin](winetworksharingprovider/network/captiveportallogin-swift.struct.md)
  Captive portal login information for a Wi-Fi network.
### Getting the date
- [let lastModified: Date](winetworksharingprovider/network/lastmodified.md)
  The date when this network was last modified.
- [let firstShared: Date](winetworksharingprovider/network/firstshared.md)
  The date when this network was first shared to the accessory.
### Getting a network description
- [var description: String](winetworksharingprovider/network/description.md)
  A string description of the network, for debugging purposes.

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
- [WINetworkSharingProvider.NetworkEvent](winetworksharingprovider/networkevent.md)
  An event that occurred, indicating an update to the available shared networks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/network)*