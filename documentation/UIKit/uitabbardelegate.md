# UITabBarDelegate

**Framework**: UIKit  
**Kind**: protocol

The [`UITabBarDelegate`](uitabbardelegate.md) protocol defines optional methods for a delegate of a [`UITabBar`](uitabbar.md) object. The [`UITabBar`](uitabbar.md) class provides the ability for the user to reorder, remove, and add items to the tab bar; this process is referred to as customizing the tab bar. The tab bar delegate receives messages when customizing occurs.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UITabBarDelegate : NSObjectProtocol
```

#### Overview

Send [`beginCustomizingItems(_:)`](uitabbar/begincustomizingitems(_:).md) to a [`UITabBar`](uitabbar.md) object to begin customizing. Implement the methods in Customizing tab bars to intervene while a user is customizing a tab bar. The customizing modal view is dismissed when the user taps the Done button on the modal view.

## Topics

### Customizing tab bars
- [func tabBar(UITabBar, willBeginCustomizing: [UITabBarItem])](uitabbardelegate/tabbar(_:willbegincustomizing:).md)
  Sent to the delegate before the customizing modal view is displayed.
- [func tabBar(UITabBar, didBeginCustomizing: [UITabBarItem])](uitabbardelegate/tabbar(_:didbegincustomizing:).md)
  Sent to the delegate after the customizing modal view is displayed.
- [func tabBar(UITabBar, willEndCustomizing: [UITabBarItem], changed: Bool)](uitabbardelegate/tabbar(_:willendcustomizing:changed:).md)
  Sent to the delegate before the customizing modal view is dismissed.
- [func tabBar(UITabBar, didEndCustomizing: [UITabBarItem], changed: Bool)](uitabbardelegate/tabbar(_:didendcustomizing:changed:).md)
  Sent to the delegate after the customizing modal view is dismissed.
- [func tabBar(UITabBar, didSelect: UITabBarItem)](uitabbardelegate/tabbar(_:didselect:).md)
  Sent to the delegate when the user selects a tab bar item.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [UITabBarController](uitabbarcontroller.md)

## See Also

- [var delegate: (any UITabBarDelegate)?](uitabbar/delegate.md)
  The tab bar’s delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbardelegate)*