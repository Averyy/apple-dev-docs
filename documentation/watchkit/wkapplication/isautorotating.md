# isAutorotating

**Framework**: WatchKit  
**Kind**: property

A Boolean value that determines whether the interface automatically rotates when the user flips their wrist.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
var isAutorotating: Bool { get set }
```

#### Discussion

This property defaults to [`false`](https://developer.apple.com/documentation/swift/false).

Normally, when a user rotates their wrist–for example, to show a watchOS app to another person–the watch is likely to interpret this motion as dropping the wrist and may put the app to sleep. When you enable autorotation, watchOS instead keeps the interface awake and rotates the content, orienting it properly for the viewer.

Don’t enable autorotation indefinitely. Instead, enable it selectively on a specific interface controller that the user is likely to share. For example, in the interface controller’s [`willActivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate()) method, set this property to [`true`](https://developer.apple.com/documentation/swift/true). In the [`didDeactivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/diddeactivate()) method, set it back to [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var isAutorotated: Bool](isautorotated.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isautorotated))
  A Boolean value that indicates whether the system has automatically rotated the user interface so that it is properly oriented for another viewer.
- [func deviceOrientationDidChange()](deviceorientationdidchange().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/deviceorientationdidchange()))
  Tells the delegate that the device’s orientation has changed.
- [var isAutorotated: Bool](isautorotated.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/isautorotated))
  A Boolean value that indicates whether the system has automatically rotated the user interface, orienting it properly for another viewer.
- [var globalTintColor: UIColor](globaltintcolor.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/globaltintcolor))
  The watchOS app’s global tint color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication/isautorotating)*