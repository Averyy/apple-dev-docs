# UISplitViewController.Column

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the columns within the split view interface.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum Column
```

```c
enum UISplitViewControllerColumn : NSInteger;
```

## Topics

### Constants
- [UISplitViewController.Column.primary](./column/primary.md)
  The column for the primary view controller.
- [UISplitViewController.Column.supplementary](./column/supplementary.md)
  The column for the supplementary view controller.
- [UISplitViewController.Column.secondary](./column/secondary.md)
  The column for the secondary, or detail, view controller.
- [UISplitViewController.Column.compact](./column/compact.md)
  The column for the view controller that’s shown when the split view controller is collapsed.
- [UISplitViewController.Column.inspector](./column/inspector.md)
  The column for the inspector, or trailing, view controller.
### Initializers
- [init?(rawValue: Int)](./column/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing the child view controllers
- [func setViewController(UIViewController?, for: UISplitViewController.Column)](./setviewcontroller%28_,for%29.md)
  Presents the provided view controller in the specified column of the split view interface.
- [func viewController(for: UISplitViewController.Column) -> UIViewController?](./viewcontroller%28for%29.md)
  Returns the view controller associated with the specified column of the split view interface.
- [var viewControllers: [UIViewController]](./viewcontrollers.md)
  The array of view controllers the split view controller manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/column)*