# UISplitViewControllerDelegate

**Framework**: UIKit  
**Kind**: protocol

The methods adopted by the object you use to manage changes to a split view interface.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UISplitViewControllerDelegate
```

#### Overview

Use the methods of this protocol to respond to changes in the current display mode and to the current interface orientation. When the split view interface collapses and expands, or when a new view controller is added to the interface, you can also use these methods to configure the child view controllers.

The methods of this protocol are all optional. If you don’t implement any of the methods, the split view controller provides default behavior to handle the collapsing and expanding transitions.

For more information, see [`UISplitViewController`](uisplitviewcontroller.md).

##### Column Style Split Views

In a column-style split view interface, you use these delegate methods to customize interface transition behavior:

- [`splitViewController(_:topColumnForCollapsingToProposedTopColumn:)`](uisplitviewcontrollerdelegate/splitviewcontroller(_:topcolumnforcollapsingtoproposedtopcolumn:).md)
- [`splitViewController(_:willHide:)`](uisplitviewcontrollerdelegate/splitviewcontroller(_:willhide:).md)
- [`splitViewController(_:didHide:)`](uisplitviewcontrollerdelegate/splitviewcontroller(_:didhide:).md)
- [`splitViewControllerDidCollapse(_:)`](uisplitviewcontrollerdelegate/splitviewcontrollerdidcollapse(_:).md)
- [`splitViewController(_:displayModeForExpandingToProposedDisplayMode:)`](uisplitviewcontrollerdelegate/splitviewcontroller(_:displaymodeforexpandingtoproposeddisplaymode:).md)
- [`splitViewController(_:willShow:)`](uisplitviewcontrollerdelegate/splitviewcontroller(_:willshow:).md)
- [`splitViewController(_:didShow:)`](uisplitviewcontrollerdelegate/splitviewcontroller(_:didshow:).md)
- [`splitViewControllerDidExpand(_:)`](uisplitviewcontrollerdelegate/splitviewcontrollerdidexpand(_:).md)

##### Classic Split Views

In a classic split view interface, you use these delegate methods to customize interface transition behavior:

- [`primaryViewController(forCollapsing:)`](uisplitviewcontrollerdelegate/primaryviewcontroller(forcollapsing:).md)
- [`splitViewController(_:collapseSecondary:onto:)`](uisplitviewcontrollerdelegate/splitviewcontroller(_:collapsesecondary:onto:).md)
- [`primaryViewController(forExpanding:)`](uisplitviewcontrollerdelegate/primaryviewcontroller(forexpanding:).md)
- [`splitViewController(_:separateSecondaryFrom:)`](uisplitviewcontrollerdelegate/splitviewcontroller(_:separatesecondaryfrom:).md)
- [`splitViewController(_:show:sender:)`](uisplitviewcontrollerdelegate/splitviewcontroller(_:show:sender:).md)
- [`splitViewController(_:showDetail:sender:)`](uisplitviewcontrollerdelegate/splitviewcontroller(_:showdetail:sender:).md)

At the end of a collapse transition, the split view controller typically shows only the content from its primary view controller. You can change this behavior by implementing the [`primaryViewController(forCollapsing:)`](uisplitviewcontrollerdelegate/primaryviewcontroller(forcollapsing:).md) method in your split view controller delegate. You might use that method to specify the secondary view controller or an entirely different view controller—perhaps one better suited for display in a horizontally compact environment.

If you want to perform any additional adjustments of the view controllers and view hierarchy, you can also implement the [`splitViewController(_:collapseSecondary:onto:)`](uisplitviewcontrollerdelegate/splitviewcontroller(_:collapsesecondary:onto:).md) method in your delegate.

The expansion process reverses the collapsing process by asking the delegate to designate which view controller becomes the primary view controller and to give the delegate a chance to perform the transition itself. If you implement the delegate methods for collapsing your split view interface, you should also implement the [`primaryViewController(forExpanding:)`](uisplitviewcontrollerdelegate/primaryviewcontroller(forexpanding:).md) and [`splitViewController(_:separateSecondaryFrom:)`](uisplitviewcontrollerdelegate/splitviewcontroller(_:separatesecondaryfrom:).md) methods for expanding that interface.

## Topics

### Specifying the interface orientations
- [func splitViewControllerPreferredInterfaceOrientationForPresentation(UISplitViewController) -> UIInterfaceOrientation](uisplitviewcontrollerdelegate/splitviewcontrollerpreferredinterfaceorientationforpresentation(_:).md)
  Asks the delegate for the orientation to use when presenting the split view controller.
- [func splitViewControllerSupportedInterfaceOrientations(UISplitViewController) -> UIInterfaceOrientationMask](uisplitviewcontrollerdelegate/splitviewcontrollersupportedinterfaceorientations(_:).md)
  Asks the delegate to specify the interface orientations that the split view controller supports.
### Responding to display mode changes
- [func splitViewController(UISplitViewController, willChangeTo: UISplitViewController.DisplayMode)](uisplitviewcontrollerdelegate/splitviewcontroller(_:willchangeto:).md)
  Tells the delegate that the display mode for the split view controller is about to change.
- [func targetDisplayModeForAction(in: UISplitViewController) -> UISplitViewController.DisplayMode](uisplitviewcontrollerdelegate/targetdisplaymodeforaction(in:).md)
  Asks the delegate to provide the display mode to apply when a split view controller action occurs.
### Collapsing the interface
- [func splitViewController(UISplitViewController, topColumnForCollapsingToProposedTopColumn: UISplitViewController.Column) -> UISplitViewController.Column](uisplitviewcontrollerdelegate/splitviewcontroller(_:topcolumnforcollapsingtoproposedtopcolumn:).md)
  Asks the delegate to provide the column to display after the split view interface collapses.
- [func splitViewController(UISplitViewController, willHide: UISplitViewController.Column)](uisplitviewcontrollerdelegate/splitviewcontroller(_:willhide:).md)
  Tells the delegate that the specified column is about to be hidden.
- [func splitViewController(UISplitViewController, didHide: UISplitViewController.Column)](uisplitviewcontrollerdelegate/splitviewcontroller(_:didhide:).md)
  Tells the delegate that the system completed hiding the specified column.
- [func splitViewControllerDidCollapse(UISplitViewController)](uisplitviewcontrollerdelegate/splitviewcontrollerdidcollapse(_:).md)
  Tells the delegate that the split view controller interface has collapsed.
### Expanding the interface
- [func splitViewController(UISplitViewController, displayModeForExpandingToProposedDisplayMode: UISplitViewController.DisplayMode) -> UISplitViewController.DisplayMode](uisplitviewcontrollerdelegate/splitviewcontroller(_:displaymodeforexpandingtoproposeddisplaymode:).md)
  Asks the delegate to provide the display mode to use after the split view interface expands.
- [func splitViewController(UISplitViewController, willShow: UISplitViewController.Column)](uisplitviewcontrollerdelegate/splitviewcontroller(_:willshow:).md)
  Tells the delegate that the specified column is about to be shown.
- [func splitViewController(UISplitViewController, didShow: UISplitViewController.Column)](uisplitviewcontrollerdelegate/splitviewcontroller(_:didshow:).md)
  Tells the delegate that the system completed showing the specified column.
- [func splitViewControllerDidExpand(UISplitViewController)](uisplitviewcontrollerdelegate/splitviewcontrollerdidexpand(_:).md)
  Tells the delegate that the split view controller interface has expanded.
### Handling the presentation gesture
- [func splitViewControllerInteractivePresentationGestureWillBegin(UISplitViewController)](uisplitviewcontrollerdelegate/splitviewcontrollerinteractivepresentationgesturewillbegin(_:).md)
  Tells the delegate that the interactive presentation gesture is about to begin.
- [func splitViewControllerInteractivePresentationGestureDidEnd(UISplitViewController)](uisplitviewcontrollerdelegate/splitviewcontrollerinteractivepresentationgesturedidend(_:).md)
  Tells the delegate when the interactive presentation gesture ends.
### Collapsing and expanding classic split views
- [func primaryViewController(forCollapsing: UISplitViewController) -> UIViewController?](uisplitviewcontrollerdelegate/primaryviewcontroller(forcollapsing:).md)
  Asks the delegate to provide the single view controller to display after the split view interface collapses.
- [func splitViewController(UISplitViewController, collapseSecondary: UIViewController, onto: UIViewController) -> Bool](uisplitviewcontrollerdelegate/splitviewcontroller(_:collapsesecondary:onto:).md)
  Asks the delegate to adjust the primary view controller and to incorporate the secondary view controller into the collapsed interface.
- [func primaryViewController(forExpanding: UISplitViewController) -> UIViewController?](uisplitviewcontrollerdelegate/primaryviewcontroller(forexpanding:).md)
  Asks the delegate to provide the view controller to display in the primary position when the split view interface expands.
- [func splitViewController(UISplitViewController, separateSecondaryFrom: UIViewController) -> UIViewController?](uisplitviewcontrollerdelegate/splitviewcontroller(_:separatesecondaryfrom:).md)
  Asks the delegate to provide the new secondary view controller for the split view interface.
### Overriding the presentation behavior
- [func splitViewController(UISplitViewController, show: UIViewController, sender: Any?) -> Bool](uisplitviewcontrollerdelegate/splitviewcontroller(_:show:sender:).md)
  Asks the delegate if it will do the work of displaying a view controller in the primary position of the split view interface.
- [func splitViewController(UISplitViewController, showDetail: UIViewController, sender: Any?) -> Bool](uisplitviewcontrollerdelegate/splitviewcontroller(_:showdetail:sender:).md)
  Asks the delegate if it will do the work of displaying a view controller in the secondary position of the split view interface.
### Deprecated methods
- [func splitViewController(UISplitViewController, shouldHide: UIViewController, in: UIInterfaceOrientation) -> Bool](uisplitviewcontrollerdelegate/splitviewcontroller(_:shouldhide:in:).md)
  Asks the delegate whether the first view controller should be hidden for the specified orientation.
- [func splitViewController(UISplitViewController, willHide: UIViewController, with: UIBarButtonItem, for: UIPopoverController)](uisplitviewcontrollerdelegate/splitviewcontroller(_:willhide:with:for:).md)
  Tells the delegate that the specified view controller is about to be hidden.
- [func splitViewController(UISplitViewController, willShow: UIViewController, invalidating: UIBarButtonItem)](uisplitviewcontrollerdelegate/splitviewcontroller(_:willshow:invalidating:).md)
  Tells the delegate that the specified view controller is about to be shown again.
- [func splitViewController(UISplitViewController, popoverController: UIPopoverController, willPresent: UIViewController)](uisplitviewcontrollerdelegate/splitviewcontroller(_:popovercontroller:willpresent:).md)
  Tells the delegate that the hidden view controller is about to be displayed in a popover.

## See Also

- [var delegate: (any UISplitViewControllerDelegate)?](uisplitviewcontroller/delegate.md)
  The delegate you use to manage changes to a split view interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate)*