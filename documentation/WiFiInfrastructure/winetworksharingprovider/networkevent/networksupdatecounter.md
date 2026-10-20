# networksUpdateCounter

**Framework**: Wi-Fi Infrastructure  
**Kind**: property  
**Role**: Instance Property

A counter that increments whenever the network data changes.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
let networksUpdateCounter: UInt64
```

#### Discussion

The counter increments by `1`.

## See Also

### Getting network data
- [let networks: [WINetworkSharingProvider.Network]](./networks.md)
  The latest network data, containing a list of all networks shared to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/networkevent/networksupdatecounter)*