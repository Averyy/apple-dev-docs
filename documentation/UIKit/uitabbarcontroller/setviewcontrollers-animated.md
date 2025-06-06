# setViewControllers(_:animated:)

**Framework**: UIKit  
**Kind**: method

Sets the root view controllers of the tab bar controller.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setViewControllers(_ viewControllers: [UIViewController]?, animated: Bool)
```

#### Discussion

When you assign a new set of view controllers at runtime, the tab bar controller removes all of the old view controllers before installing the new ones. When changing the view controllers, the tab bar controller remembers the view controller object that was previously selected and attempts to reselect it. If the selected view controller is no longer present, it attempts to select the view controller at the same index in the array as the previous selection. If that index is invalid, it selects the view controller at index 0.

This method also sets the value of the [`customizableViewControllers`](uitabbarcontroller/customizableviewcontrollers.md) property to the contents of the `viewControllers` parameter.

## Parameters

- `viewControllers`: The array of custom view controllers to display in the tab bar interface. The order of the view controllers in this array corresponds to the display order in the tab bar, with the controller at index 0 representing the left-most tab, the controller at index 1 the next tab to the right, and so on.
- `animated`: If  , the tab bar items for the view controllers are animated into position. If  , changes to the tab bar items are reflected immediately.

## See Also

- [var viewControllers: [UIViewController]?](uitabbarcontroller/viewcontrollers.md)
  An array of the root view controllers displayed by the tab bar interface.
- [var customizableViewControllers: [UIViewController]?](uitabbarcontroller/customizableviewcontrollers.md)
  The subset of view controllers managed by this tab bar controller that can be customized.
- [var moreNavigationController: UINavigationController](uitabbarcontroller/morenavigationcontroller.md)
  The view controller that manages the More navigation interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/setviewcontrollers(_:animated:))*