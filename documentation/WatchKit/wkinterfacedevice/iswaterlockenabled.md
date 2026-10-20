# isWaterLockEnabled

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the water lock is enabled.

**Availability**:
- watchOS 6.1+

## Declaration

```swift
var isWaterLockEnabled: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isWaterLockEnabled) BOOL waterLockEnabled;
```

## See Also

### Accessing Water Resistance and Lock
- [var waterResistanceRating: WKWaterResistanceRating](./waterresistancerating.md)
  The Apple Watch water-resistance rating.
- [enum WKWaterResistanceRating](../wkwaterresistancerating.md)
  Values indicating the water-resistance rating.
- [func enableWaterLock()](./enablewaterlock%28%29.md)
  Disables the Apple Watch touch screen to prevent accidental taps while submerged.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/iswaterlockenabled)*