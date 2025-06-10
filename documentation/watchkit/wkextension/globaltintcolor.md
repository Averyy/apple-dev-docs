# globalTintColor

**Framework**: WatchKit  
**Kind**: property

The watchOS app’s global tint color.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
@MainActor
var globalTintColor: UIColor { get }
```

#### Discussion

This property provides access to the global tint color so that you can match the color elsewhere in your user interface. You specify the global tint color in the app’s storyboard, or in the asset catalog. If you don’t set a global tint color, this property returns the system default tint color.

For more information, see [`Setting the app’s accent color`](https://developer.apple.com/documentation/watchOS-Apps/setting-the-app-s-accent-color).

## See Also

- [var isAutorotating: Bool](wkextension/isautorotating.md)
  A Boolean value that determines whether the interface automatically rotates when the user flips their wrist.
- [var isAutorotated: Bool](wkextension/isautorotated.md)
  A Boolean value that indicates whether the system has automatically rotated the user interface so that it is properly oriented for another viewer.
- [func enableWaterLock()](wkextension/enablewaterlock.md)
  Disables the Apple Watch touch screen to prevent accidental taps while the watch is underwater.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkextension/globaltintcolor)*