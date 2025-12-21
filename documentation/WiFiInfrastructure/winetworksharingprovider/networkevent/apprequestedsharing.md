# appRequestedSharing

**Framework**: Wi-Fi Infrastructure  
**Kind**: property

A Boolean value that indicates whether the container app requested network sharing.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
let appRequestedSharing: Bool
```

#### Discussion

The system sets this flag when your container app calls [`askToShare()`](winetworksharingcontroller/asktoshare().md).

## See Also

- [let newShareableNetworkAvailable: Bool](winetworksharingprovider/networkevent/newshareablenetworkavailable.md)
  A Boolean value that indicates whether the system detected available networks your app extension may request from people.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/networkevent/apprequestedsharing)*