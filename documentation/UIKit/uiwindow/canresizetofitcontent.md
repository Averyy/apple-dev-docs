# canResizeToFitContent

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window’s constraint-based content determines its size.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var canResizeToFitContent: Bool { get set }
```

```objc
@property (nonatomic, setter=setCanResizeToFitContent:) BOOL canResizeToFitContent;
```

#### Discussion

The default value of this property is [`false`](../../Swift/false.md), which causes the window to maintain a fixed size. Setting this property to [`true`](../../Swift/true.md) allows the system to perform constraints-based window sizing, which updates the window’s size to match the space needed by its content. Window-size changes occur only when the app runs on macOS.

## See Also

### Configuring the window
- [var rootViewController: UIViewController?](./rootviewcontroller.md)
  The root view controller for the window.
- [var windowLevel: UIWindow.Level](./windowlevel.md)
  The position of the window in the z-axis.
- [UIWindow.Level](./level.md)
  The positioning of windows relative to each other.
- [var screen: UIScreen](./screen.md)
  The screen to display the window on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindow/canresizetofitcontent)*