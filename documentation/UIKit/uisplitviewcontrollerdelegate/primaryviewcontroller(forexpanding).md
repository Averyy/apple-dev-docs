# primaryViewController(forExpanding:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate to provide the view controller to display in the primary position when the split view interface expands.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func primaryViewController(forExpanding splitViewController: UISplitViewController) -> UIViewController?
```

```objc
- (UIViewController *) primaryViewControllerForExpandingSplitViewController:(UISplitViewController *) splitViewController;
```

#### Return Value

The view controller to use as the primary view controller, or `nil` to specify the current primary view controller.

#### Discussion

This delegate method only applies to classic split view interfaces. For more information, see [Split view styles](../uisplitviewcontroller.md#Split-view-styles).

When the split view controller transitions from a horizontally compact to a horizontally regular size class, it calls this method and asks you for the view controller to display in the primary position when that transition is complete. The view controller you return becomes the primary view controller of the split view interface. If you do not implement this method, or if your implementation returns `nil`, the split view controller chooses its current primary view controller as the one to use.

If you specified a specific view controller in your [`primaryViewController(forCollapsing:)`](./primaryviewcontroller%28forcollapsing%29.md) method, use this method to restore the original primary view controller for your split view interface. You can also implement the [`splitViewController(_:separateSecondaryFrom:)`](./splitviewcontroller%28_,separatesecondaryfrom%29.md) method to disentangle your view controllers from one another as needed.

## Parameters

- `splitViewController`: The split view controller whose interface is expanding.

## See Also

### Collapsing and expanding classic split views
- [func primaryViewController(forCollapsing: UISplitViewController) -> UIViewController?](./primaryviewcontroller%28forcollapsing%29.md)
  Asks the delegate to provide the single view controller to display after the split view interface collapses.
- [func splitViewController(UISplitViewController, collapseSecondary: UIViewController, onto: UIViewController) -> Bool](./splitviewcontroller%28_,collapsesecondary,onto%29.md)
  Asks the delegate to adjust the primary view controller and to incorporate the secondary view controller into the collapsed interface.
- [func splitViewController(UISplitViewController, separateSecondaryFrom: UIViewController) -> UIViewController?](./splitviewcontroller%28_,separatesecondaryfrom%29.md)
  Asks the delegate to provide the new secondary view controller for the split view interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/primaryviewcontroller(forexpanding:))*