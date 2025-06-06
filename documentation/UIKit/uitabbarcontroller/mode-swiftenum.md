# UITabBarController.Mode

**Framework**: UIKit  
**Kind**: enum

A tab bar’s display mode.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
enum Mode
```

## Topics

### Setting modes
- [UITabBarController.Mode.automatic](uitabbarcontroller/mode-swift.enum/automatic.md)
  The system sets the display mode based on the tab’s content.
- [UITabBarController.Mode.tabBar](uitabbarcontroller/mode-swift.enum/tabbar.md)
  The system displays the content only as a tab bar.
- [UITabBarController.Mode.tabSidebar](uitabbarcontroller/mode-swift.enum/tabsidebar.md)
  The system displays the content as either a tab bar or a sidebar, depending on the context.
### Initializers
- [init?(rawValue: Int)](uitabbarcontroller/mode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var mode: UITabBarController.Mode](uitabbarcontroller/mode-swift.property.md)
  The display mode for a tab bar.
- [var sidebar: UITabBarController.Sidebar](uitabbarcontroller/sidebar-swift.property.md)
  A tab bar’s corresponding sidebar.
- [UITabBarController.Sidebar](uitabbarcontroller/sidebar-swift.class.md)
  An object for managing and configuring the sidebar.
- [class UITabSidebarItem](uitabsidebaritem.md)
- [UITabSidebarItem.Request](uitabsidebaritem/request.md)
- [UITabBarController.Sidebar.Animating](uitabbarcontroller/sidebar-swift.class/animating.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/mode-swift.enum)*