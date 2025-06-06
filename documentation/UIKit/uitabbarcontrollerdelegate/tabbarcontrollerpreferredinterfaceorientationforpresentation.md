# tabBarControllerPreferredInterfaceOrientationForPresentation(_:)

**Framework**: UIKit  
**Kind**: method

Called to allow the delegate to provide the preferred orientation for presentation of the tab bar controller.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func tabBarControllerPreferredInterfaceOrientationForPresentation(_ tabBarController: UITabBarController) -> UIInterfaceOrientation
```

#### Return Value

The preferred orientation for presenting the tab bar controller.

## Parameters

- `tabBarController`: The tab bar controller that is asking the delegate object for the preferred presentation orientation.

## See Also

- [var preferredInterfaceOrientationForPresentation: UIInterfaceOrientation](uiviewcontroller/preferredinterfaceorientationforpresentation.md)
  The interface orientation to use when presenting the view controller.
- [func tabBarControllerSupportedInterfaceOrientations(UITabBarController) -> UIInterfaceOrientationMask](uitabbarcontrollerdelegate/tabbarcontrollersupportedinterfaceorientations(_:).md)
  Called to allow the delegate to provide the complete set of supported interface orientations for the tab bar controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontrollerpreferredinterfaceorientationforpresentation(_:))*