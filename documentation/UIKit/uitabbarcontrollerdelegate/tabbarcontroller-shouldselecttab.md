# tabBarController(_:shouldSelectTab:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether the specified tab should be made active.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
optional func tabBarController(_ tabBarController: UITabBarController, shouldSelectTab tab: UITab) -> Bool
```

#### Discussion

Return @c YES if the specified @c tab can be selected by the user. Otherwise, return @c NO


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontrollerdelegate/tabbarcontroller(_:shouldselecttab:))*