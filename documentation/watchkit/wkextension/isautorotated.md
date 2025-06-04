# isAutorotated

**Framework**: Watchkit  
**Kind**: property

A Boolean value that indicates whether the system has automatically rotated the user interface so that it is properly oriented for another viewer.

**Availability**:
- watchOS 4.2+

## Declaration

```swift
@MainActor var isAutorotated: Bool { get }
```

## Overview

Normally, when a user rotates their wrist–for example, to show a watchOS app to another person–the watch is likely to interpret this motion as dropping the wrist and may put the app to sleep. When autorotation is enabled, watchOS instead keeps the interface awake and rotates the content so that it is oriented properly for the viewer.

For more information on enabling autorotation, see [`isAutorotating`](https://developer.apple.com/documentation/watchkit/wkextension/isautorotating).

## See Also

- [func deviceOrientationDidChange()](deviceorientationdidchange().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/deviceorientationdidchange()))
- [var isAutorotating: Bool](isautorotating.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/isautorotating))
- [var globalTintColor: UIColor](globaltintcolor.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/globaltintcolor))
- [func enableWaterLock()](enablewaterlock().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension/enablewaterlock()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/isautorotated)*