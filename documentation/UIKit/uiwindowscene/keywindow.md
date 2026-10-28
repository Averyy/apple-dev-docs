# keyWindow

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The key window associated with the scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var keyWindow: UIWindow? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) UIWindow * keyWindow;
```

## Discussion

The key window receives keyboard and other non-touch-related events. Of a scene’s associated [`windows`](./windows.md), only one window at a time may be the key window.

## See Also

### Getting the active windows
- [var windows: [UIWindow]](./windows.md)
  The windows associated with the scene.
- [var screen: UIScreen](./screen.md)
  The screen that displays the contents of the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/keywindow)*