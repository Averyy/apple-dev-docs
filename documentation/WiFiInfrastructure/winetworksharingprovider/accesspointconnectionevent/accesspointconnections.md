# accessPointConnections

**Framework**: Wi-Fi Infrastructure  
**Kind**: property

A list of access points to which the host connects for networks someone authorized to share to the device.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
let accessPointConnections: [WINetworkSharingProvider.AccessPointConnection]
```

#### Discussion

The Wi-Fi Infrastructure framework filters this list to access points matching the predicate you provide when getting the [`accessPointConnectionEvents(matching:)`](winetworksharingprovider/accesspointconnectionevents(matching:).md) sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/accesspointconnectionevent/accesspointconnections)*