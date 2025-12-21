# lastModified

**Framework**: Wi-Fi Infrastructure  
**Kind**: property

The date when this network was last modified.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
let lastModified: Date
```

#### Discussion

Use this property for informational purposes or broad filtering policies. Avoid deriving subsets of changed networks based on specific timestamps due to potential wall time fluctuations.

## See Also

- [let firstShared: Date](winetworksharingprovider/network/firstshared.md)
  The date when this network was first shared to the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/network/lastmodified)*