# splitViewController(_:separateSecondaryFrom:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate to provide the new secondary view controller for the split view interface.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func splitViewController(_ splitViewController: UISplitViewController, separateSecondaryFrom primaryViewController: UIViewController) -> UIViewController?
```

```objc
- (UIViewController *) splitViewController:(UISplitViewController *) splitViewController separateSecondaryViewControllerFromPrimaryViewController:(UIViewController *) primaryViewController;
```

#### Return Value

The view controller to use as the secondary view controller in the expanded split view interface, or `nil` to let the split view controller choose an appropriate secondary view controller for you.

#### Discussion

This delegate method only applies to classic split view interfaces. For more information, see [Split view styles](../uisplitviewcontroller.md#Split-view-styles).

Use this method to designate the secondary view controller for your split view interface and to perform any additional cleanup that might be needed. After this method returns, the split view controller installs the newly designated primary and secondary view controllers in its [`viewControllers`](../uisplitviewcontroller/viewcontrollers.md) array.

When an interface collapses, some view controllers merge the contents of the primary and secondary view controllers. This method is your opportunity to undo those changes and return your split view interface to its original state.

When you return `nil` from this method, the split view controller calls the primary view controller’s [`separateSecondaryViewController(for:)`](../uiviewcontroller/separatesecondaryviewcontroller%28for%29.md) method, giving it a chance to designate an appropriate secondary view controller. Most view controllers do nothing by default but the [`UINavigationController`](../uinavigationcontroller.md) class responds by popping and returning the view controller from the top of its navigation stack.

## Parameters

- `splitViewController`: The split view controller whose interface is expanding.
- `primaryViewController`: The primary view controller in the expanded split view interface. If you implement the [`primaryViewController(forExpanding:)`](./primaryviewcontroller%28forexpanding%29.md) method in your delegate, this object is the one that method returns.

## See Also

### Collapsing and expanding classic split views
- [func primaryViewController(forCollapsing: UISplitViewController) -> UIViewController?](./primaryviewcontroller%28forcollapsing%29.md)
  Asks the delegate to provide the single view controller to display after the split view interface collapses.
- [func splitViewController(UISplitViewController, collapseSecondary: UIViewController, onto: UIViewController) -> Bool](./splitviewcontroller%28_,collapsesecondary,onto%29.md)
  Asks the delegate to adjust the primary view controller and to incorporate the secondary view controller into the collapsed interface.
- [func primaryViewController(forExpanding: UISplitViewController) -> UIViewController?](./primaryviewcontroller%28forexpanding%29.md)
  Asks the delegate to provide the view controller to display in the primary position when the split view interface expands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontroller(_:separatesecondaryfrom:))*