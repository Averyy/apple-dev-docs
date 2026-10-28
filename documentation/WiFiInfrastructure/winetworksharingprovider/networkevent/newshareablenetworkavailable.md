# newShareableNetworkAvailable

**Framework**: Wi-Fi Infrastructure  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the system detected available networks your app extension may request from people.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
let newShareableNetworkAvailable: Bool
```

## Discussion

Your app extension can use [`presentAskToShareUI(scanProvider:)`](../presentasktoshareui%28scanprovider%29.md) to request that people share the network with your accessory when your accessory needs it. This flag clears when people share the available networks to your accessory or when the networks are no longer available.

> ❗ **Important**: When people choose to automatically share networks to your accessory, the system automatically provides the network in the [`networks`](./networks.md) property without setting this flag, because your app extension doesn’t need to take action.

## See Also

### Getting event signals
- [let appRequestedSharing: Bool](./apprequestedsharing.md)
  A Boolean value that indicates whether the container app requested network sharing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/networkevent/newshareablenetworkavailable)*