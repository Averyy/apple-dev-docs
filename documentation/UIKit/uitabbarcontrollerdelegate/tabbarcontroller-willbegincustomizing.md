# tabBarController(_:willBeginCustomizing:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the tab bar customization sheet is about to be displayed.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func tabBarController(_ tabBarController: UITabBarController, willBeginCustomizing viewControllers: [UIViewController])
```

## Parameters

- `tabBarController`: The tab bar controller that is being customized.
- `viewControllers`: The view controllers to be displayed in the customization sheet. This list typically contains all custom view controllers you added but does not include some standard controllers, such as the one that manages the More tab.

## See Also

- [func tabBarController(UITabBarController, willEndCustomizing: [UIViewController], changed: Bool)](uitabbarcontrollerdelegate/tabbarcontroller(_:willendcustomizing:changed:).md)
  Tells the delegate that the tab bar customization sheet is about to be dismissed.
- [func tabBarController(UITabBarController, didEndCustomizing: [UIViewController], changed: Bool)](uitabbarcontrollerdelegate/tabbarcontroller(_:didendcustomizing:changed:).md)
  Tells the delegate that the tab bar customization sheet was dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:willbegincustomizing:))*