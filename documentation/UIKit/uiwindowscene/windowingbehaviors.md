# windowingBehaviors

**Framework**: UIKit  
**Kind**: property

An object that specifies the behaviors of the window.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var windowingBehaviors: UISceneWindowingBehaviors? { get }
```

#### Discussion

For Mac apps built with Mac Catalyst, use this property to specify whether the scene’s window displays minimize and close buttons. This property is `nil` on unsupported platforms.

## See Also

- [var isFullScreen: Bool](uiwindowscene/isfullscreen.md)
  A Boolean value that indicates whether the window scene is full screen or windowed.
- [class UISceneWindowingBehaviors](uiscenewindowingbehaviors.md)
  An object with properties that determine the behavior of a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/windowingbehaviors)*