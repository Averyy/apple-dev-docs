# tabBarController(_:tab:acceptItemsFrom:)

**Framework**: UIKit  
**Kind**: method

Notifies the delegate to perform a drop into the specified @c tab from the specified session.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
optional func tabBarController(_ tabBarController: UITabBarController, tab: UITab, acceptItemsFrom session: any UIDropSession)
```

## Mentions

- [Elevating your iPad app with a tab bar and sidebar](elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md)

#### Discussion

This is only called if the operation returned from `tabBarController:tab:operationForAcceptingItemsFromDropSession` is valid for a drop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:tab:acceptitemsfrom:))*