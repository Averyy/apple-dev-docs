# networks

**Framework**: Wi-Fi Infrastructure  
**Kind**: property

The latest network data, containing a list of all networks shared to the device.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
let networks: [WINetworkSharingProvider.Network]
```

#### Discussion

The list will be filtered to networks matching the provided predicate, with a predicate was provided when getting the `WINetworkSharingProvider/networkListUpdates(matching:)` sequence.

## See Also

- [let networksUpdateCounter: UInt64](winetworksharingprovider/networkevent/networksupdatecounter.md)
  A counter that increments whenever the network data changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/networkevent/networks)*