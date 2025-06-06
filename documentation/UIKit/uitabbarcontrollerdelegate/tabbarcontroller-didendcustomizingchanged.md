# tabBarController(_:didEndCustomizing:changed:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the tab bar customization sheet was dismissed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func tabBarController(_ tabBarController: UITabBarController, didEndCustomizing viewControllers: [UIViewController], changed: Bool)
```

#### Discussion

You can use this method to respond to changes to the order of tabs in the tab bar.

## Parameters

- `tabBarController`: The tab bar controller that is being customized.
- `viewControllers`: The view controllers of the tab bar controller. The arrangement of the controllers in the array represents the new display order within the tab bar.
- `changed`: A Boolean value indicating whether items changed on the tab bar.   if items changed or   if they did not.

## See Also

- [func tabBarController(UITabBarController, willBeginCustomizing: [UIViewController])](uitabbarcontrollerdelegate/tabbarcontroller(_:willbegincustomizing:).md)
  Tells the delegate that the tab bar customization sheet is about to be displayed.
- [func tabBarController(UITabBarController, willEndCustomizing: [UIViewController], changed: Bool)](uitabbarcontrollerdelegate/tabbarcontroller(_:willendcustomizing:changed:).md)
  Tells the delegate that the tab bar customization sheet is about to be dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:didendcustomizing:changed:))*