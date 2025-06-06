# tabBarController(_:willEndCustomizing:changed:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the tab bar customization sheet is about to be dismissed.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func tabBarController(_ tabBarController: UITabBarController, willEndCustomizing viewControllers: [UIViewController], changed: Bool)
```

#### Discussion

This method is called in response to the user tapping the Done button on the sheet but before the sheet is dismissed.

## Parameters

- `tabBarController`: The tab bar controller that is being customized.
- `viewControllers`: The view controllers of the tab bar controller. The arrangement of the controllers in the array represents the new display order within the tab bar.
- `changed`: A Boolean value indicating whether items changed on the tab bar.   if items changed or   if they did not.

## See Also

- [func tabBarController(UITabBarController, willBeginCustomizing: [UIViewController])](uitabbarcontrollerdelegate/tabbarcontroller(_:willbegincustomizing:).md)
  Tells the delegate that the tab bar customization sheet is about to be displayed.
- [func tabBarController(UITabBarController, didEndCustomizing: [UIViewController], changed: Bool)](uitabbarcontrollerdelegate/tabbarcontroller(_:didendcustomizing:changed:).md)
  Tells the delegate that the tab bar customization sheet was dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:willendcustomizing:changed:))*