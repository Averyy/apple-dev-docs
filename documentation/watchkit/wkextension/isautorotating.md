# isAutorotating

**Framework**: Watchkit  
**Kind**: property

A Boolean value that determines whether the interface automatically rotates when the user flips their wrist.

**Availability**:
- watchOS 4.0+

## Declaration

```swift
@MainActor var isAutorotating: Bool { get set }
```

## Overview

Defaults to [`false`](https://developer.apple.com/documentation/swift/false).

Normally, when a user rotates their wrist–for example, to show a watchOS app to another person–the watch is likely to interpret this motion as dropping the wrist and may put the app to sleep. When autorotation is enabled, watchOS instead keeps the interface awake and rotates the content so that it is oriented properly for the viewer.

Do not enable autorotation indefinitely. Instead, enable it selectively on a specific interface controller that the user is likely to share. For example, in the interface controller’s [`willActivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate()) method, set this property to [`true`](https://developer.apple.com/documentation/swift/true). In the [`didDeactivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/diddeactivate()) method, set it back to [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func deviceOrientationDidChange()](deviceorientationdidchange().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/deviceorientationdidchange()))
- [var isAutorotated: Bool](isautorotated.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isautorotated))
- [var globalTintColor: UIColor](globaltintcolor.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/globaltintcolor))
- [func enableWaterLock()](enablewaterlock().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/enablewaterlock()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/isautorotating)*