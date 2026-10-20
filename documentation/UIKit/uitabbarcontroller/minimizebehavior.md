# UITabBarController.MinimizeBehavior

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UITabBarMinimizeBehavior : NSInteger;
```

## Topics

### Enumeration Cases
- [UITabBarController.MinimizeBehavior.automatic](./minimizebehavior/automatic.md)
  Resolves to the system default minimize behavior.
- [UITabBarController.MinimizeBehavior.never](./minimizebehavior/never.md)
  The tab bar does not minimize.
- [UITabBarController.MinimizeBehavior.onScrollDown](./minimizebehavior/onscrolldown.md)
  The tab bar minimizes when scrolling down, and expands when scrolling back up.
- [UITabBarController.MinimizeBehavior.onScrollUp](./minimizebehavior/onscrollup.md)
  The tab bar minimizes when scrolling up, and expands when scrolling back down. Recommended if the scroll view content is aligned to the bottom.
### Initializers
- [init?(rawValue: Int)](./minimizebehavior/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Customizing the tab bar behavior
- [var delegate: (any UITabBarControllerDelegate)?](./delegate.md)
  The tab bar controller’s delegate object.
- [protocol UITabBarControllerDelegate](../uitabbarcontrollerdelegate.md)
  A set of methods you implement to customize the behavior of a tab bar.
- [var tabBarMinimizeBehavior: UITabBarController.MinimizeBehavior](./tabbarminimizebehavior.md)
  Defines the minimize behavior for the tab bar, if it is supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/minimizebehavior)*