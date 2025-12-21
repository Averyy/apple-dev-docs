# UITabBarController.MinimizeBehavior

**Framework**: UIKit  
**Kind**: enum

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum MinimizeBehavior
```

## Topics

### Enumeration Cases
- [UITabBarController.MinimizeBehavior.automatic](uitabbarcontroller/minimizebehavior/automatic.md)
  Resolves to the system default minimize behavior.
- [UITabBarController.MinimizeBehavior.never](uitabbarcontroller/minimizebehavior/never.md)
  The tab bar does not minimize.
- [UITabBarController.MinimizeBehavior.onScrollDown](uitabbarcontroller/minimizebehavior/onscrolldown.md)
  The tab bar minimizes when scrolling down, and expands when scrolling back up.
- [UITabBarController.MinimizeBehavior.onScrollUp](uitabbarcontroller/minimizebehavior/onscrollup.md)
  The tab bar minimizes when scrolling up, and expands when scrolling back down. Recommended if the scroll view content is aligned to the bottom.
### Initializers
- [init?(rawValue: Int)](uitabbarcontroller/minimizebehavior/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var delegate: (any UITabBarControllerDelegate)?](uitabbarcontroller/delegate.md)
  The tab bar controller’s delegate object.
- [protocol UITabBarControllerDelegate](uitabbarcontrollerdelegate.md)
  A set of methods you implement to customize the behavior of a tab bar.
- [var tabBarMinimizeBehavior: UITabBarController.MinimizeBehavior](uitabbarcontroller/tabbarminimizebehavior.md)
  Defines the minimize behavior for the tab bar, if it is supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/minimizebehavior)*