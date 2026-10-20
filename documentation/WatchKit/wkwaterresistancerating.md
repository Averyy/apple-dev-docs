# WKWaterResistanceRating

**Framework**: WatchKit  
**Kind**: enum  
**Role**: Enumeration

Values indicating the water-resistance rating.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
enum WKWaterResistanceRating
```

```c
enum WKWaterResistanceRating : NSInteger;
```

## Topics

### Enumeration Cases
- [WKWaterResistanceRating.ipx7](./wkwaterresistancerating/ipx7.md)
  A water-resistance rating of IPX7.
- [WKWaterResistanceRating.wr50](./wkwaterresistancerating/wr50.md)
  A water-resistance rating of 50 meters.
- [WKWaterResistanceRating.wr100](./wkwaterresistancerating/wr100.md)
### Initializers
- [init?(rawValue: Int)](./wkwaterresistancerating/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing Water Resistance and Lock
- [var waterResistanceRating: WKWaterResistanceRating](./wkinterfacedevice/waterresistancerating.md)
  The Apple Watch water-resistance rating.
- [var isWaterLockEnabled: Bool](./wkinterfacedevice/iswaterlockenabled.md)
  A Boolean value that indicates whether the water lock is enabled.
- [func enableWaterLock()](./wkinterfacedevice/enablewaterlock%28%29.md)
  Disables the Apple Watch touch screen to prevent accidental taps while submerged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkwaterresistancerating)*