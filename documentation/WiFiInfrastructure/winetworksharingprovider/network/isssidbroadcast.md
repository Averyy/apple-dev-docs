# isSSIDBroadcast

**Framework**: Wi-Fi Infrastructure  
**Kind**: property

A Boolean value indicating whether the access point broadcasts the SSID.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
let isSSIDBroadcast: Bool
```

#### Discussion

Networks that don’t broadcast their SSID need directed scanning with the specific SSID information to be discoverable by your accessory.

> ⚠️ **Warning**: Active Wi-Fi scanning reduces privacy for people using your accessory because probe requests are visible to all nearby Wi-Fi devices. These scans can reveal your accessory’s location, and scanning for specific SSIDs exposes networks your accessory used previously, indicating past locations. Implement MAC address randomization in probe request frames and minimize active scans when possible.

> **Note**: - [`Privacy features when connecting to wireless networks`](https://developer.apple.comhttps://support.apple.com/guide/security/privacy-features-connecting-wireless-networks-secb9cb3140c/web)
- [`Recommended settings for Wi-Fi routers and access points`](https://developer.apple.comhttps://support.apple.com/en-us/102766)

## See Also

- [let ssid: WISSID](winetworksharingprovider/network/ssid.md)
  The Service Set Identifier (SSID) of the network, also known as the network name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/network/isssidbroadcast)*