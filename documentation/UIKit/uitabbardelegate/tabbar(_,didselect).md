# tabBar(_:didSelect:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sent to the delegate when the user selects a tab bar item.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func tabBar(_ tabBar: UITabBar, didSelect item: UITabBarItem)
```

```objc
- (void) tabBar:(UITabBar *) tabBar didSelectItem:(UITabBarItem *) item;
```

## Parameters

- `tabBar`: The tab bar that is being customized.
- `item`: The tab bar item that was selected.

## See Also

### Customizing tab bars
- [func tabBar(UITabBar, willBeginCustomizing: [UITabBarItem])](./tabbar%28_,willbegincustomizing%29.md)
  Sent to the delegate before the customizing modal view is displayed.
- [func tabBar(UITabBar, didBeginCustomizing: [UITabBarItem])](./tabbar%28_,didbegincustomizing%29.md)
  Sent to the delegate after the customizing modal view is displayed.
- [func tabBar(UITabBar, willEndCustomizing: [UITabBarItem], changed: Bool)](./tabbar%28_,willendcustomizing,changed%29.md)
  Sent to the delegate before the customizing modal view is dismissed.
- [func tabBar(UITabBar, didEndCustomizing: [UITabBarItem], changed: Bool)](./tabbar%28_,didendcustomizing,changed%29.md)
  Sent to the delegate after the customizing modal view is dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbardelegate/tabbar(_:didselect:))*