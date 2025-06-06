# UITabBarController.Mode.tabSidebar

**Framework**: UIKit  
**Kind**: case

The system displays the content as either a tab bar or a sidebar, depending on the context.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
case tabSidebar
```

## Mentions

- [Elevating your iPad app with a tab bar and sidebar](elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md)

#### Discussion

Different platforms handle the mode differently:

- On iPad, the system displays the content as either a tab bar or a sidebar, depending on the context.
- On Mac Catalyst, the system displays a sidebar.
- On iPhone and Apple TV, the system displays the platform’s regular tab bar.
- In visionOS, the system displays the platform’s regular tabs, but a [`UITabGroup`](uitabgroup.md) can display a sidebar when it displays the group’s view controller.

For more information, see [`Elevating your iPad app with a tab bar and sidebar`](elevating-your-ipad-app-with-a-tab-bar-and-sidebar.md).

## See Also

- [UITabBarController.Mode.automatic](uitabbarcontroller/mode-swift.enum/automatic.md)
  The system sets the display mode based on the tab’s content.
- [UITabBarController.Mode.tabBar](uitabbarcontroller/mode-swift.enum/tabbar.md)
  The system displays the content only as a tab bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/mode-swift.enum/tabsidebar)*