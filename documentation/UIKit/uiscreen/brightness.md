# brightness

**Framework**: UIKit  
**Kind**: property

The brightness level of the screen.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var brightness: CGFloat { get set }
```

#### Discussion

This property is only supported on the main screen. The value of this property is a number between `0.0` and `1.0`, inclusive, where `0.0` is the minimum brightness and `1.0` is the maximum brightness.

Brightness changes remain in effect until the person locks their device, even if the person closes your app before then. The next time the person unlocks the device, the system restores the brightness setting to the original value in Settings or Control Center.

In visionOS, setting this property has no effect.

## See Also

- [var wantsSoftwareDimming: Bool](uiscreen/wantssoftwaredimming.md)
  A Boolean value that indicates whether the screen may be dimmed lower than the hardware is normally capable of by emulating it in software.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/brightness)*