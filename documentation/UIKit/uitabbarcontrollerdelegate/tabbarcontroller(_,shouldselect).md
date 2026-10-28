# tabBarController(_:shouldSelect:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether the specified view controller should be made active.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func tabBarController(_ tabBarController: UITabBarController, shouldSelect viewController: UIViewController) -> Bool
```

```objc
- (BOOL) tabBarController:(UITabBarController *) tabBarController shouldSelectViewController:(UIViewController *) viewController;
```

## Return Value

[`true`](../../Swift/true.md) if the view controller’s tab should be selected or [`false`](../../Swift/false.md) if the current tab should remain active.

## Discussion

The tab bar controller calls this method in response to the user tapping a tab bar item. You can use this method to dynamically decide whether a given tab should be made the active tab.

## Parameters

- `tabBarController`: The tab bar controller containing `viewController`.
- `viewController`: The view controller belonging to the tab that was tapped by the user.

## See Also

### Managing tab bar selections
- [func tabBarController(UITabBarController, didSelect: UIViewController)](./tabbarcontroller%28_,didselect%29.md)
  Tells the delegate that the user selected an item in the tab bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:shouldselect:))*