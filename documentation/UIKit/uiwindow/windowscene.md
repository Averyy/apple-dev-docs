# windowScene

**Framework**: UIKit  
**Kind**: property

The scene containing the window.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var windowScene: UIWindowScene? { get set }
```

#### Discussion

Changing the value of this property moves the window to the newly specified scene. Setting the property to `nil` removes the window from its current scene.

## See Also

- [var avDisplayManager: AVDisplayManager](uiwindow/avdisplaymanager.md)
  The display manager that handles requests for screen resolution, refresh rate, and HDR mode information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow/windowscene)*