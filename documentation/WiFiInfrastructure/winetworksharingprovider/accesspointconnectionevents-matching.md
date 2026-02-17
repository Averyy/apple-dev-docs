# accessPointConnectionEvents(matching:)

**Framework**: Wi-Fi Infrastructure  
**Kind**: method

Returns an async sequence of access point events containing the currently connected access point(s) and future updates.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
func accessPointConnectionEvents(matching predicate: Predicate<WINetworkSharingProvider.AccessPointConnection>? = nil) -> some Sendable & AsyncSequence<WINetworkSharingProvider.AccessPointConnectionEvent, any Error>
```

#### Return Value

An AsyncSequence that delivers [`WINetworkSharingProvider.AccessPointConnectionEvent`](winetworksharingprovider/accesspointconnectionevent.md) instances whenever your app extension needs to update its access point information.

#### Discussion

Updates will be sent when the host joins or roams to a new Access Point, or when it disconnects from an access point.

## Parameters

- `predicate`: An optional predicate for filtering the access point list. The default is  , meaning   you receive all access point information.

## See Also

- [WINetworkSharingProvider.AccessPointConnection](winetworksharingprovider/accesspointconnection.md)
  A Wi-Fi access point the host is currently connected to, which may be shared with a connected accessory.
- [WINetworkSharingProvider.AccessPointConnectionEvent](winetworksharingprovider/accesspointconnectionevent.md)
  An event that occurred, indicating an update to the available shared access points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/accesspointconnectionevents(matching:))*