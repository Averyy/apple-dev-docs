# tabBarControllerPreferredInterfaceOrientationForPresentation(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Called to allow the delegate to provide the preferred orientation for presentation of the tab bar controller.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func tabBarControllerPreferredInterfaceOrientationForPresentation(_ tabBarController: UITabBarController) -> UIInterfaceOrientation
```

```objc
- (UIInterfaceOrientation) tabBarControllerPreferredInterfaceOrientationForPresentation:(UITabBarController *) tabBarController;
```

## Return Value

The preferred orientation for presenting the tab bar controller.

## Parameters

- `tabBarController`: The tab bar controller that is asking the delegate object for the preferred presentation orientation.

## See Also

### Related Documentation
- [var preferredInterfaceOrientationForPresentation: UIInterfaceOrientation](../uiviewcontroller/preferredinterfaceorientationforpresentation.md)
  The interface orientation to use when presenting the view controller.
### Overriding view rotation settings
- [func tabBarControllerSupportedInterfaceOrientations(UITabBarController) -> UIInterfaceOrientationMask](./tabbarcontrollersupportedinterfaceorientations%28_%29.md)
  Called to allow the delegate to provide the complete set of supported interface orientations for the tab bar controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontrollerpreferredinterfaceorientationforpresentation(_:))*