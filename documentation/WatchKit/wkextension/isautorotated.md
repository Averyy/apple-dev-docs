# isAutorotated

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the system has automatically rotated the user interface so that it is properly oriented for another viewer.

**Availability**:
- watchOS 4.2+ - Deprecated in 9.2

## Declaration

```swift
var isAutorotated: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isAutorotated) BOOL autorotated;
```

## Discussion

Normally, when a user rotates their wrist–for example, to show a watchOS app to another person–the watch is likely to interpret this motion as dropping the wrist and may put the app to sleep. When autorotation is enabled, watchOS instead keeps the interface awake and rotates the content so that it is oriented properly for the viewer.

For more information on enabling autorotation, see [`isAutorotating`](./isautorotating.md).

## See Also

### Related Documentation
- [func deviceOrientationDidChange()](../wkextensiondelegate/deviceorientationdidchange%28%29.md)
  Tells the delegate that the device’s orientation has changed.
### Managing the user interface
- [var isAutorotating: Bool](./isautorotating.md)
  A Boolean value that determines whether the interface automatically rotates when the user flips their wrist.
- [var globalTintColor: UIColor](./globaltintcolor.md)
  The watchOS app’s global tint color.
- [func enableWaterLock()](./enablewaterlock%28%29.md)
  Disables the Apple Watch touch screen to prevent accidental taps while the watch is underwater.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/isautorotated)*