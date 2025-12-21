# tabBarMinimizeBehavior

**Framework**: UIKit  
**Kind**: property

Defines the minimize behavior for the tab bar, if it is supported.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
var tabBarMinimizeBehavior: UITabBarController.MinimizeBehavior { get set }
```

#### Discussion

The default value for this property is `UITabBarMinimizeBehaviorAutomatic`.

## See Also

- [var delegate: (any UITabBarControllerDelegate)?](uitabbarcontroller/delegate.md)
  The tab bar controller’s delegate object.
- [protocol UITabBarControllerDelegate](uitabbarcontrollerdelegate.md)
  A set of methods you implement to customize the behavior of a tab bar.
- [UITabBarController.MinimizeBehavior](uitabbarcontroller/minimizebehavior.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/tabbarminimizebehavior)*