# isAutorotating

**Framework**: WatchKit  
**Kind**: property

A Boolean value that determines whether the interface automatically rotates when the user flips their wrist.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
@MainActor
var isAutorotating: Bool { get set }
```

#### Discussion

Defaults to [`false`](https://developer.apple.com/documentation/Swift/false).

Normally, when a user rotates their wrist–for example, to show a watchOS app to another person–the watch is likely to interpret this motion as dropping the wrist and may put the app to sleep. When autorotation is enabled, watchOS instead keeps the interface awake and rotates the content so that it is oriented properly for the viewer.

Do not enable autorotation indefinitely. Instead, enable it selectively on a specific interface controller that the user is likely to share. For example, in the interface controller’s [`willActivate()`](wkinterfacecontroller/willactivate().md) method, set this property to [`true`](https://developer.apple.com/documentation/Swift/true). In the [`didDeactivate()`](wkinterfacecontroller/diddeactivate().md) method, set it back to [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func deviceOrientationDidChange()](wkextensiondelegate/deviceorientationdidchange.md)
  Tells the delegate that the device’s orientation has changed.
- [var isAutorotated: Bool](wkextension/isautorotated.md)
  A Boolean value that indicates whether the system has automatically rotated the user interface so that it is properly oriented for another viewer.
- [var globalTintColor: UIColor](wkextension/globaltintcolor.md)
  The watchOS app’s global tint color.
- [func enableWaterLock()](wkextension/enablewaterlock.md)
  Disables the Apple Watch touch screen to prevent accidental taps while the watch is underwater.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/isautorotating)*