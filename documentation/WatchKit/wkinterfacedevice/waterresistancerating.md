# waterResistanceRating

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The Apple Watch water-resistance rating.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var waterResistanceRating: WKWaterResistanceRating { get }
```

```objc
@property (nonatomic, readonly) WKWaterResistanceRating waterResistanceRating;
```

#### Discussion

For a list of possible water resistance ratings, see [`WKWaterResistanceRating`](../wkwaterresistancerating.md).

## See Also

### Accessing Water Resistance and Lock
- [enum WKWaterResistanceRating](../wkwaterresistancerating.md)
  Values indicating the water-resistance rating.
- [var isWaterLockEnabled: Bool](./iswaterlockenabled.md)
  A Boolean value that indicates whether the water lock is enabled.
- [func enableWaterLock()](./enablewaterlock%28%29.md)
  Disables the Apple Watch touch screen to prevent accidental taps while submerged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/waterresistancerating)*