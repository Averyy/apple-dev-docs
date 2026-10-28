# firstShared

**Framework**: Wi-Fi Infrastructure  
**Kind**: property  
**Role**: Instance Property

The date when this network was first shared to the accessory.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+

## Declaration

```swift
let firstShared: Date
```

## Discussion

Use this property for informational purposes or broad filtering policies. Avoid deriving subsets of changed networks based on specific timestamps due to potential wall time fluctuations.

## See Also

### Getting the date
- [let lastModified: Date](./lastmodified.md)
  The date when this network was last modified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiinfrastructure/winetworksharingprovider/network/firstshared)*