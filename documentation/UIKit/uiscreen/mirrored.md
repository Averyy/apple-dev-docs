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
var mirrored: UIScreen? { get }
```

#### Discussion

When a screen supports mirroring and mirroring is active, this property contains the screen object associated with the device’s main screen. This represents the screen the attached display mirrors from. The value of this property is `nil` when mirroring is disabled, not supported, or no screen is connected to the device.

To disable mirroring and present unique content on the external display, register a scene accessory with [`registerSceneAccessory(_:)`](uiviewcontroller/registersceneaccessory(_:).md). For more information, see [`Presenting content on a connected display`](presenting-content-on-a-connected-display.md).

## See Also

- [class var main: UIScreen](uiscreen/main.md)
  Returns the screen object representing the device’s screen.
- [var isCaptured: Bool](uiscreen/iscaptured.md)
  A Boolean value that indicates whether the system is actively cloning the screen to another destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/mirrored)*