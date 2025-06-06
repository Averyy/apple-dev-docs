# tabBarControllerSupportedInterfaceOrientations(_:)

**Framework**: UIKit  
**Kind**: method

Called to allow the delegate to provide the complete set of supported interface orientations for the tab bar controller.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func tabBarControllerSupportedInterfaceOrientations(_ tabBarController: UITabBarController) -> UIInterfaceOrientationMask
```

#### Return Value

One of the [`UIInterfaceOrientationMask`](uiinterfaceorientationmask.md) constants that represents the set of interface orientations supported by the tab bar controller.

## Parameters

- `tabBarController`: The tab bar controller that is asking the delegate object for the supported interface orientations.

## See Also

- [var supportedInterfaceOrientations: UIInterfaceOrientationMask](uiviewcontroller/supportedinterfaceorientations.md)
  The interface orientations that the view controller supports.
- [func tabBarControllerPreferredInterfaceOrientationForPresentation(UITabBarController) -> UIInterfaceOrientation](uitabbarcontrollerdelegate/tabbarcontrollerpreferredinterfaceorientationforpresentation(_:).md)
  Called to allow the delegate to provide the preferred orientation for presentation of the tab bar controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontrollersupportedinterfaceorientations(_:))*