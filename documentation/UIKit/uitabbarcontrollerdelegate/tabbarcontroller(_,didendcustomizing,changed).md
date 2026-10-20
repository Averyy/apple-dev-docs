# tabBarController(_:didEndCustomizing:changed:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the tab bar customization sheet was dismissed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func tabBarController(_ tabBarController: UITabBarController, didEndCustomizing viewControllers: [UIViewController], changed: Bool)
```

```objc
- (void) tabBarController:(UITabBarController *) tabBarController didEndCustomizingViewControllers:(NSArray<__kindof UIViewController *> *) viewControllers changed:(BOOL) changed;
```

#### Discussion

You can use this method to respond to changes to the order of tabs in the tab bar.

## Parameters

- `tabBarController`: The tab bar controller that is being customized.
- `viewControllers`: The view controllers of the tab bar controller. The arrangement of the controllers in the array represents the new display order within the tab bar.
- `changed`: A Boolean value indicating whether items changed on the tab bar. [`true`](../../Swift/true.md) if items changed or [`false`](../../Swift/false.md) if they did not.

## See Also

### Managing tab bar customizations
- [func tabBarController(UITabBarController, willBeginCustomizing: [UIViewController])](./tabbarcontroller%28_,willbegincustomizing%29.md)
  Tells the delegate that the tab bar customization sheet is about to be displayed.
- [func tabBarController(UITabBarController, willEndCustomizing: [UIViewController], changed: Bool)](./tabbarcontroller%28_,willendcustomizing,changed%29.md)
  Tells the delegate that the tab bar customization sheet is about to be dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:didendcustomizing:changed:))*