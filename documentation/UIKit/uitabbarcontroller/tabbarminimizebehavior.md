# tabBarMinimizeBehavior

**Framework**: UIKit  
**Kind**: property

Defines the minimize behavior for the tab bar, if it is supported.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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