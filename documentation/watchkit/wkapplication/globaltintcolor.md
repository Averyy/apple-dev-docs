# globalTintColor

**Framework**: Watchkit  
**Kind**: property

The watchOS app’s global tint color.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
var globalTintColor: UIColor { get }
```

#### Discussion

This property provides access to the global tint color so that you can match the color elsewhere in your user interface. You specify the global tint color in the app’s storyboard, or in the asset catalog. If you don’t set a global tint color, this property returns the system default tint color.

For more information, see [`Setting the app’s accent color`](https://developer.apple.com/documentation/watchOS-Apps/setting-the-app-s-accent-color).

## See Also

- [var isAutorotating: Bool](wkapplication/isautorotating.md)
  A Boolean value that determines whether the interface automatically rotates when the user flips their wrist.
- [var isAutorotated: Bool](wkapplication/isautorotated.md)
  A Boolean value that indicates whether the system has automatically rotated the user interface, orienting it properly for another viewer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplication/globaltintcolor)*