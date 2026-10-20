# viewController(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the view controller associated with the specified column of the split view interface.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func viewController(for column: UISplitViewController.Column) -> UIViewController?
```

```objc
- (UIViewController *) viewControllerForColumn:(UISplitViewControllerColumn) column;
```

#### Return Value

The corresponding child view controller object.

#### Discussion

This method doesn’t apply to classic split view controllers with a [`style`](./style-swift.property.md) of [`UISplitViewController.Style.unspecified`](./style-swift.enum/unspecified.md). For a classic split view controller, instead use the [`viewControllers`](./viewcontrollers.md) property to get the view controllers in the split view interface.

## Parameters

- `column`: The corresponding column of the split view interface. See [`UISplitViewController.Column`](./column.md) for values.

## See Also

### Managing the child view controllers
- [UISplitViewController.Column](./column.md)
  Constants that describe the columns within the split view interface.
- [func setViewController(UIViewController?, for: UISplitViewController.Column)](./setviewcontroller%28_,for%29.md)
  Presents the provided view controller in the specified column of the split view interface.
- [var viewControllers: [UIViewController]](./viewcontrollers.md)
  The array of view controllers the split view controller manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontroller/viewcontroller(for:))*