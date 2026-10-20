# tabBarController(_:willBeginCustomizing:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the tab bar customization sheet is about to be displayed.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func tabBarController(_ tabBarController: UITabBarController, willBeginCustomizing viewControllers: [UIViewController])
```

```objc
- (void) tabBarController:(UITabBarController *) tabBarController willBeginCustomizingViewControllers:(NSArray<__kindof UIViewController *> *) viewControllers;
```

## Parameters

- `tabBarController`: The tab bar controller that is being customized.
- `viewControllers`: The view controllers to be displayed in the customization sheet. This list typically contains all custom view controllers you added but does not include some standard controllers, such as the one that manages the More tab.

## See Also

### Managing tab bar customizations
- [func tabBarController(UITabBarController, willEndCustomizing: [UIViewController], changed: Bool)](./tabbarcontroller%28_,willendcustomizing,changed%29.md)
  Tells the delegate that the tab bar customization sheet is about to be dismissed.
- [func tabBarController(UITabBarController, didEndCustomizing: [UIViewController], changed: Bool)](./tabbarcontroller%28_,didendcustomizing,changed%29.md)
  Tells the delegate that the tab bar customization sheet was dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:willbegincustomizing:))*