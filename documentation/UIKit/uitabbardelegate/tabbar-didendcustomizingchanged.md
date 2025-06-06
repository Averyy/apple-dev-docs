# tabBar(_:didEndCustomizing:changed:)

**Framework**: UIKit  
**Kind**: method

Sent to the delegate after the customizing modal view is dismissed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func tabBar(_ tabBar: UITabBar, didEndCustomizing items: [UITabBarItem], changed: Bool)
```

## Parameters

- `tabBar`: The tab bar that is being customized.
- `items`: The items on the customizing modal view.
- `changed`:   if the visible set of items on the tab bar changed; otherwise,  .

## See Also

- [func tabBar(UITabBar, willBeginCustomizing: [UITabBarItem])](uitabbardelegate/tabbar(_:willbegincustomizing:).md)
  Sent to the delegate before the customizing modal view is displayed.
- [func tabBar(UITabBar, didBeginCustomizing: [UITabBarItem])](uitabbardelegate/tabbar(_:didbegincustomizing:).md)
  Sent to the delegate after the customizing modal view is displayed.
- [func tabBar(UITabBar, willEndCustomizing: [UITabBarItem], changed: Bool)](uitabbardelegate/tabbar(_:willendcustomizing:changed:).md)
  Sent to the delegate before the customizing modal view is dismissed.
- [func tabBar(UITabBar, didSelect: UITabBarItem)](uitabbardelegate/tabbar(_:didselect:).md)
  Sent to the delegate when the user selects a tab bar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbardelegate/tabbar(_:didendcustomizing:changed:))*