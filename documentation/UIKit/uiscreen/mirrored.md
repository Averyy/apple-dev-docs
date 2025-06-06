# mirrored

**Framework**: UIKit  
**Kind**: property

The screen an external display mirrors from.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
var mirrored: UIScreen? { get }
```

#### Discussion

When a screen supports mirroring and mirroring is active, this property contains the screen object associated with the device’s main screen. This represents the screen the attached display mirrors from. The value of this property is `nil` when mirroring is disabled, not supported, or no screen is connected to the device.

To disable mirroring and use the external display for presenting unique content, create a window and associate it with a [`windowExternalDisplayNonInteractive`](uiscenesession/role-swift.struct/windowexternaldisplaynoninteractive.md) scene.

## See Also

- [class var main: UIScreen](uiscreen/main.md)
  Returns the screen object representing the device’s screen.
- [var isCaptured: Bool](uiscreen/iscaptured.md)
  A Boolean value that indicates whether the system is actively cloning the screen to another destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/mirrored)*