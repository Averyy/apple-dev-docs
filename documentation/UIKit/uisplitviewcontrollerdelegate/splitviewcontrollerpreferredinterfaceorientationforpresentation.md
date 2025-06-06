# splitViewControllerPreferredInterfaceOrientationForPresentation(_:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for the orientation to use when presenting the split view controller.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func splitViewControllerPreferredInterfaceOrientationForPresentation(_ splitViewController: UISplitViewController) -> UIInterfaceOrientation
```

#### Return Value

The orientation to use when first displaying the split view controller.

#### Discussion

UIKit calls this method to determine which orientation your app prefers when presenting the specified split view controller. You can use this method to specify the orientation that you think is best when first displaying the split view controller. The orientation you specify can be different from the current device orientation. After presentation, the system may rotate the split view controller as appropriate to one of its other supported interface orientations.

If you do not implement this method, the system presents the view controller using the current orientation of the status bar.

## Parameters

- `splitViewController`: The split view controller that is about to be presented onscreen.

## See Also

- [var preferredInterfaceOrientationForPresentation: UIInterfaceOrientation](uiviewcontroller/preferredinterfaceorientationforpresentation.md)
  The interface orientation to use when presenting the view controller.
- [func splitViewControllerSupportedInterfaceOrientations(UISplitViewController) -> UIInterfaceOrientationMask](uisplitviewcontrollerdelegate/splitviewcontrollersupportedinterfaceorientations(_:).md)
  Asks the delegate to specify the interface orientations that the split view controller supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollerpreferredinterfaceorientationforpresentation(_:))*