# UISplitViewController.Column

**Framework**: UIKit  
**Kind**: enum

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

## Topics

### Constants
- [UISplitViewController.Column.primary](uisplitviewcontroller/column/primary.md)
  The column for the primary view controller.
- [UISplitViewController.Column.supplementary](uisplitviewcontroller/column/supplementary.md)
  The column for the supplementary view controller.
- [UISplitViewController.Column.secondary](uisplitviewcontroller/column/secondary.md)
  The column for the secondary, or detail, view controller.
- [UISplitViewController.Column.compact](uisplitviewcontroller/column/compact.md)
  The column for the view controller that’s shown when the split view controller is collapsed.
### Initializers
- [init?(rawValue: Int)](uisplitviewcontroller/column/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func setViewController(UIViewController?, for: UISplitViewController.Column)](uisplitviewcontroller/setviewcontroller(_:for:).md)
  Presents the provided view controller in the specified column of the split view interface.
- [func viewController(for: UISplitViewController.Column) -> UIViewController?](uisplitviewcontroller/viewcontroller(for:).md)
  Returns the view controller associated with the specified column of the split view interface.
- [var viewControllers: [UIViewController]](uisplitviewcontroller/viewcontrollers.md)
  The array of view controllers the split view controller manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/column)*