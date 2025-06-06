# isAutorotated

**Framework**: Watchkit  
**Kind**: property

A Boolean value that indicates whether the system has automatically rotated the user interface, orienting it properly for another viewer.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
var isAutorotated: Bool { get }
```

#### Discussion

Normally, when a user rotates their wrist–for example, to show a watchOS app to another person–the watch is likely to interpret this motion as dropping the wrist and may put the app to sleep. When you enable autorotation, watchOS instead keeps the interface awake and rotates the content, orienting it properly for the viewer.

For more information on enabling autorotation, see [`isAutorotating`](wkextension/isautorotating.md).

## See Also

- [var isAutorotating: Bool](wkextension/isautorotating.md)
  A Boolean value that determines whether the interface automatically rotates when the user flips their wrist.
- [func deviceOrientationDidChange()](wkextensiondelegate/deviceorientationdidchange.md)
  Tells the delegate that the device’s orientation has changed.
- [var isAutorotating: Bool](wkapplication/isautorotating.md)
  A Boolean value that determines whether the interface automatically rotates when the user flips their wrist.
- [var globalTintColor: UIColor](wkapplication/globaltintcolor.md)
  The watchOS app’s global tint color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication/isautorotated)*