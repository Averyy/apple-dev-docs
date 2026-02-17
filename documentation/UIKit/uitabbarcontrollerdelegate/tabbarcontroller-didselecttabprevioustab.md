# tabBarController(_:didSelectTab:previousTab:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the user selected the specified @c selectedTab in the tab bar controller.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
optional func tabBarController(_ tabBarController: UITabBarController, didSelectTab selectedTab: UITab, previousTab: UITab?)
```

#### Discussion

This specified @c selectedTab is either a root tab or any of their descendants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:didselecttab:previoustab:))*