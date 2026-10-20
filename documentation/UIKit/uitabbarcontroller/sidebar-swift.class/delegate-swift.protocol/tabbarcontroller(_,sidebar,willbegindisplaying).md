# tabBarController(_:sidebar:willBeginDisplaying:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate when the sidebar is about to display the row representing the specified `tab`

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
optional func tabBarController(_ tabBarController: UITabBarController, sidebar: UITabBarController.Sidebar, willBeginDisplaying tab: UITab)
```

```objc
- (void) tabBarController:(UITabBarController *) tabBarController sidebar:(UITabBarControllerSidebar *) sidebar willBeginDisplayingTab:(UITab *) tab;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/delegate-swift.protocol/tabbarcontroller(_:sidebar:willbegindisplaying:))*