# globalTintColor

**Framework**: Watchkit  
**Kind**: property

The watchOS app’s global tint color.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor var globalTintColor: UIColor { get }
```

## Overview

This property provides access to the global tint color so that you can match the color elsewhere in your user interface. You specify the global tint color in the app’s storyboard, or in the asset catalog. If you don’t set a global tint color, this property returns the system default tint color.

For more information, see [`Setting the app’s accent color`](https://developer.apple.com/documentation/watchOS-Apps/setting-the-app-s-accent-color).

## See Also

- [var isAutorotating: Bool](isautorotating.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/isautorotating))
- [var isAutorotated: Bool](isautorotated.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication/isautorotated))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication/globaltintcolor)*