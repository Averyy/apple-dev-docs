# UITabBarController.Mode

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UITabBarControllerMode : NSInteger;
```

## Topics

### Setting modes
- [UITabBarController.Mode.automatic](./mode-swift.enum/automatic.md)
  The system sets the display mode based on the tab’s content.
- [UITabBarController.Mode.tabBar](./mode-swift.enum/tabbar.md)
  The system displays the content only as a tab bar.
- [UITabBarController.Mode.tabSidebar](./mode-swift.enum/tabsidebar.md)
  The system displays the content as either a tab bar or a sidebar, depending on the context.
### Initializers
- [init?(rawValue: Int)](./mode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting the sidebar
- [var mode: UITabBarController.Mode](./mode-swift.property.md)
  The display mode for a tab bar.
- [var sidebar: UITabBarController.Sidebar](./sidebar-swift.property.md)
  A tab bar’s corresponding sidebar.
- [UITabBarController.Sidebar](./sidebar-swift.class.md)
  An object for managing and configuring the sidebar.
- [class UITabSidebarItem](../uitabsidebaritem.md)
- [UITabSidebarItem.Request](../uitabsidebaritem/request.md)
- [UITabBarController.Sidebar.Animating](./sidebar-swift.class/animating.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/mode-swift.enum)*