# isAutorotating

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the interface automatically rotates when the user flips their wrist.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
var isAutorotating: Bool { get set }
```

```objc
@property (nonatomic, getter=isAutorotating) BOOL autorotating;
```

## Discussion

This property defaults to [`false`](../../Swift/false.md).

Normally, when a user rotates their wrist–for example, to show a watchOS app to another person–the watch is likely to interpret this motion as dropping the wrist and may put the app to sleep. When you enable autorotation, watchOS instead keeps the interface awake and rotates the content, orienting it properly for the viewer.

Don’t enable autorotation indefinitely. Instead, enable it selectively on a specific interface controller that the user is likely to share. For example, in the interface controller’s [`willActivate()`](../wkinterfacecontroller/willactivate%28%29.md) method, set this property to [`true`](../../Swift/true.md). In the [`didDeactivate()`](../wkinterfacecontroller/diddeactivate%28%29.md) method, set it back to [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [var isAutorotated: Bool](../wkextension/isautorotated.md)
  A Boolean value that indicates whether the system has automatically rotated the user interface so that it is properly oriented for another viewer.
- [func deviceOrientationDidChange()](../wkextensiondelegate/deviceorientationdidchange%28%29.md)
  Tells the delegate that the device’s orientation has changed.
### Managing the user interface
- [var isAutorotated: Bool](./isautorotated.md)
  A Boolean value that indicates whether the system has automatically rotated the user interface, orienting it properly for another viewer.
- [var globalTintColor: UIColor](./globaltintcolor.md)
  The watchOS app’s global tint color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication/isautorotating)*