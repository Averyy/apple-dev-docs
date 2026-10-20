# tabBar(_:willEndCustomizing:changed:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate before the customizing modal view is dismissed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func tabBar(_ tabBar: UITabBar, willEndCustomizing items: [UITabBarItem], changed: Bool)
```

```objc
- (void) tabBar:(UITabBar *) tabBar willEndCustomizingItems:(NSArray<UITabBarItem *> *) items changed:(BOOL) changed;
```

## Parameters

- `tabBar`: The tab bar that is being customized.
- `items`: The items on the customizing modal view.
- `changed`: [`true`](../../Swift/true.md) if the visible set of items on the tab bar changed; otherwise, [`false`](../../Swift/false.md).

## See Also

### Customizing tab bars
- [func tabBar(UITabBar, willBeginCustomizing: [UITabBarItem])](./tabbar%28_,willbegincustomizing%29.md)
  Sent to the delegate before the customizing modal view is displayed.
- [func tabBar(UITabBar, didBeginCustomizing: [UITabBarItem])](./tabbar%28_,didbegincustomizing%29.md)
  Sent to the delegate after the customizing modal view is displayed.
- [func tabBar(UITabBar, didEndCustomizing: [UITabBarItem], changed: Bool)](./tabbar%28_,didendcustomizing,changed%29.md)
  Sent to the delegate after the customizing modal view is dismissed.
- [func tabBar(UITabBar, didSelect: UITabBarItem)](./tabbar%28_,didselect%29.md)
  Sent to the delegate when the user selects a tab bar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbardelegate/tabbar(_:willendcustomizing:changed:))*