# tabBarController(_:willEndCustomizing:changed:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the tab bar customization sheet is about to be dismissed.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func tabBarController(_ tabBarController: UITabBarController, willEndCustomizing viewControllers: [UIViewController], changed: Bool)
```

```objc
- (void) tabBarController:(UITabBarController *) tabBarController willEndCustomizingViewControllers:(NSArray<__kindof UIViewController *> *) viewControllers changed:(BOOL) changed;
```

#### Discussion

This method is called in response to the user tapping the Done button on the sheet but before the sheet is dismissed.

## Parameters

- `tabBarController`: The tab bar controller that is being customized.
- `viewControllers`: The view controllers of the tab bar controller. The arrangement of the controllers in the array represents the new display order within the tab bar.
- `changed`: A Boolean value indicating whether items changed on the tab bar. [`true`](../../Swift/true.md) if items changed or [`false`](../../Swift/false.md) if they did not.

## See Also

### Managing tab bar customizations
- [func tabBarController(UITabBarController, willBeginCustomizing: [UIViewController])](./tabbarcontroller%28_,willbegincustomizing%29.md)
  Tells the delegate that the tab bar customization sheet is about to be displayed.
- [func tabBarController(UITabBarController, didEndCustomizing: [UIViewController], changed: Bool)](./tabbarcontroller%28_,didendcustomizing,changed%29.md)
  Tells the delegate that the tab bar customization sheet was dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:willendcustomizing:changed:))*