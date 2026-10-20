# tabBar(_:willBeginCustomizing:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate before the customizing modal view is displayed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func tabBar(_ tabBar: UITabBar, willBeginCustomizing items: [UITabBarItem])
```

```objc
- (void) tabBar:(UITabBar *) tabBar willBeginCustomizingItems:(NSArray<UITabBarItem *> *) items;
```

#### Discussion

Use the [`beginCustomizingItems(_:)`](../uitabbar/begincustomizingitems%28_%29.md) method of [`UITabBar`](../uitabbar.md) to display the customizing modal view and begin the customizing mode.

## Parameters

- `tabBar`: The tab bar that is being customized.
- `items`: The items on the customizing modal view.

## See Also

### Customizing tab bars
- [func tabBar(UITabBar, didBeginCustomizing: [UITabBarItem])](./tabbar%28_,didbegincustomizing%29.md)
  Sent to the delegate after the customizing modal view is displayed.
- [func tabBar(UITabBar, willEndCustomizing: [UITabBarItem], changed: Bool)](./tabbar%28_,willendcustomizing,changed%29.md)
  Sent to the delegate before the customizing modal view is dismissed.
- [func tabBar(UITabBar, didEndCustomizing: [UITabBarItem], changed: Bool)](./tabbar%28_,didendcustomizing,changed%29.md)
  Sent to the delegate after the customizing modal view is dismissed.
- [func tabBar(UITabBar, didSelect: UITabBarItem)](./tabbar%28_,didselect%29.md)
  Sent to the delegate when the user selects a tab bar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbardelegate/tabbar(_:willbegincustomizing:))*