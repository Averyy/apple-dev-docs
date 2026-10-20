# isFullScreen

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window scene is full screen or windowed.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 16.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var isFullScreen: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isFullScreen) BOOL fullScreen;
```

#### Discussion

The system only supports this property in Mac Catalyst apps.

## See Also

### Determining window behaviors
- [var windowingBehaviors: UISceneWindowingBehaviors?](./windowingbehaviors.md)
  An object that specifies the behaviors of the window.
- [class UISceneWindowingBehaviors](../uiscenewindowingbehaviors.md)
  An object with properties that determine the behavior of a window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/isfullscreen)*