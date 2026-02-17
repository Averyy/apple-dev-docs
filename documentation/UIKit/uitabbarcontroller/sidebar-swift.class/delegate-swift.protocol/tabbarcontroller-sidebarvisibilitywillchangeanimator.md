# tabBarController(_:sidebarVisibilityWillChange:animator:)

**Framework**: UIKit  
**Kind**: method

Notifies the delegate when the visibility of the sidebar is about to change when `sidebar.isHidden` changes. Add animations to the animator to run alongside the visibility update. Alongside animations and completions will run immediately if the sidebar visibility is changed without animation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
optional func tabBarController(_ tabBarController: UITabBarController, sidebarVisibilityWillChange sidebar: UITabBarController.Sidebar, animator: any UITabBarController.Sidebar.Animating)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebarvisibilitywillchange:animator:))*