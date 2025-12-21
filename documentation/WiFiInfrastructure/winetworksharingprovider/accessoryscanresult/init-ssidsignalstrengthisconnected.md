# init(ssid:signalStrength:isConnected:)

**Framework**: Wi-Fi Infrastructure  
**Kind**: init

Creates an accessory scan result.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
init(ssid: WISSID?, signalStrength: Double, isConnected: Bool)
```

## Parameters

- `ssid`: The SSID of the discovered network.
- `signalStrength`: The signal strength value, between   and  .
- `isConnected`: A Boolean that indicates whether the accessory is connected to this network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/accessoryscanresult/init(ssid:signalstrength:isconnected:))*