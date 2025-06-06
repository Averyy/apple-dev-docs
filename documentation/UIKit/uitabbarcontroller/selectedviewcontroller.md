# selectedViewController

**Framework**: Uikit  
**Kind**: property

The view controller associated with the currently selected tab item.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
unowned(unsafe) var selectedViewController: UIViewController? { get set }
```

#### Discussion

This view controller is the one whose custom view is currently displayed by the tab bar interface. The specified view controller must be in the [`viewControllers`](uitabbarcontroller/viewcontrollers.md) array. Assigning a new view controller to this property changes the currently displayed view and also selects an appropriate tab in the tab bar. Changing the view controller also updates the [`selectedIndex`](uitabbarcontroller/selectedindex.md) property accordingly. The default value of this property is `nil`.

In iOS 3.0 and later, you can use this property to select any of the view controllers in the [`viewControllers`](uitabbarcontroller/viewcontrollers.md) property. This includes view controllers that are managed by the More navigation controller and whose tab bar items are not visible in the tab bar. You can also use it to select the More navigation controller itself, which is available from the [`moreNavigationController`](uitabbarcontroller/morenavigationcontroller.md) property. Prior to iOS 3.0, you could select only the More navigation controller and the subset of view controllers whose tab bar item was visible. Attempting to set this property to a view controller whose tab bar item was not visible had no effect.

> **Note**:  The More interface is not available in tvOS.

## See Also

- [var selectedIndex: Int](uitabbarcontroller/selectedindex.md)
  The index of the view controller associated with the currently selected tab item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/selectedviewcontroller)*