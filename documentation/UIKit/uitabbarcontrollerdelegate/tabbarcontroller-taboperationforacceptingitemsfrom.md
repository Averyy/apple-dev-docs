# tabBarController(_:tab:operationForAcceptingItemsFrom:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for a drop operation to determine if drag items can be dropped into the specified @c tab

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
optional func tabBarController(_ tabBarController: UITabBarController, tab: UITab, operationForAcceptingItemsFrom session: any UIDropSession) -> UIDropOperation
```

## Mentions

- [Elevating your iPad app with a tab bar and sidebar](elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md)

#### Discussion

If the operation is either a `.move` or `.copy`, then the drop will proceed and `tabBarController:tab:acceptItemsFromDropSession:` is called. By default, the drop will be treated as a cancel operation if this is not implemented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:tab:operationforacceptingitemsfrom:))*