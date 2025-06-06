# viewController(for:)

**Framework**: UIKit  
**Kind**: method

Returns the view controller associated with the specified column of the split view interface.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func viewController(for column: UISplitViewController.Column) -> UIViewController?
```

#### Return Value

The corresponding child view controller object.

#### Discussion

This method doesn’t apply to classic split view controllers with a [`style`](uisplitviewcontroller/style-swift.property.md) of [`UISplitViewController.Style.unspecified`](uisplitviewcontroller/style-swift.enum/unspecified.md). For a classic split view controller, instead use the [`viewControllers`](uisplitviewcontroller/viewcontrollers.md) property to get the view controllers in the split view interface.

## Parameters

- `column`: The corresponding column of the split view interface. See   for values.

## See Also

- [UISplitViewController.Column](uisplitviewcontroller/column.md)
  Constants that describe the columns within the split view interface.
- [func setViewController(UIViewController?, for: UISplitViewController.Column)](uisplitviewcontroller/setviewcontroller(_:for:).md)
  Presents the provided view controller in the specified column of the split view interface.
- [var viewControllers: [UIViewController]](uisplitviewcontroller/viewcontrollers.md)
  The array of view controllers the split view controller manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/viewcontroller(for:))*