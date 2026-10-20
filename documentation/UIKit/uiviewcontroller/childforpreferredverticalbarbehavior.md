# childForPreferredVerticalBarBehavior

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Which child view controller, if any, should control the vertical bar behavior.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
var childForPreferredVerticalBarBehavior: UIViewController? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIViewController * childViewControllerForPreferredVerticalBarBehavior;
```

#### Discussion

Return a child to defer the configuration to it, or `nil` to use the configuration provided by this view controller. The system container view controllers forward to their active content by default — `UINavigationController` to its top view controller, `UITabBarController` to its selected view controller — so a content view controller’s preference flows up to the window of the app or the nearest presentation.

## See Also

### Configuring bars on the vertical axis
- [var preferredVerticalBarBehavior: UIVerticalBarBehavior](./preferredverticalbarbehavior.md)
  The vertical bar behavior that this view controller prefers.
- [enum UIVerticalBarBehavior](../uiverticalbarbehavior.md)
  A behavior that determines whether the vertical bar is used.
- [func setNeedsUpdateOfVerticalBarConfiguration()](./setneedsupdateofverticalbarconfiguration%28%29.md)
  Signals to the system that the preferred vertical bar configuration, such as its behavior, has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiviewcontroller/childforpreferredverticalbarbehavior)*