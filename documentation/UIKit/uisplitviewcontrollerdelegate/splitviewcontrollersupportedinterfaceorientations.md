# splitViewControllerSupportedInterfaceOrientations(_:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate to specify the interface orientations that the split view controller supports.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func splitViewControllerSupportedInterfaceOrientations(_ splitViewController: UISplitViewController) -> UIInterfaceOrientationMask
```

#### Return Value

The orientations that you want the specified split view controller to support. The value you return can be one or more of the [`UIInterfaceOrientationMask`](uiinterfaceorientationmask.md) constants.

#### Discussion

The split view controller calls this method to obtain the orientations that it supports. You can use this method to alter the set of orientations typically supported by a split view controller. If you don’t implement this method, the split view controller supports all orientations on iPad and all but the [`allButUpsideDown`](uiinterfaceorientationmask/allbutupsidedown.md) orientation on iPhone devices.

## Parameters

- `splitViewController`: The split view controller.

## See Also

- [var supportedInterfaceOrientations: UIInterfaceOrientationMask](uiviewcontroller/supportedinterfaceorientations.md)
  The interface orientations that the view controller supports.
- [func splitViewControllerPreferredInterfaceOrientationForPresentation(UISplitViewController) -> UIInterfaceOrientation](uisplitviewcontrollerdelegate/splitviewcontrollerpreferredinterfaceorientationforpresentation(_:).md)
  Asks the delegate for the orientation to use when presenting the split view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollersupportedinterfaceorientations(_:))*