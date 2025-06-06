# windows

**Framework**: UIKit  
**Kind**: property

The windows associated with the scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var windows: [UIWindow] { get }
```

#### Discussion

Use this property to retrieve the windows associated with the scene. To remove the window from the current scene, or move it to a different scene, change the value of the window’s [`windowScene`](uiwindow/windowscene.md) property.

## See Also

- [var keyWindow: UIWindow?](uiwindowscene/keywindow.md)
  The key window associated with the scene.
- [var screen: UIScreen](uiwindowscene/screen.md)
  The screen that displays the contents of the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/windows)*