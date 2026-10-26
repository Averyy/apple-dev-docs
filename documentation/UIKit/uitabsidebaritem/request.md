# UITabSidebarItem.Request

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
class Request
```

```objc
@interface UITabSidebarItemRequest : NSObject
```

## Topics

### Instance Properties
- [var content: UITabSidebarItem.Content](./request/content.md)
- [action](../uitabsidebaritemrequest/action.md)
  The action that the receiver represents. Only one of `tab` or `action` will be valid for an item.
- [tab](../uitabsidebaritemrequest/tab.md)
  The tab that the receiver represents. Only one of `tab` or `action` will be valid for an item.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)

## See Also

### Supporting the sidebar
- [var mode: UITabBarController.Mode](../uitabbarcontroller/mode-swift.property.md)
  The display mode for a tab bar.
- [UITabBarController.Mode](../uitabbarcontroller/mode-swift.enum.md)
  A tab bar’s display mode.
- [var sidebar: UITabBarController.Sidebar](../uitabbarcontroller/sidebar-swift.property.md)
  A tab bar’s corresponding sidebar.
- [UITabBarController.Sidebar](../uitabbarcontroller/sidebar-swift.class.md)
  An object for managing and configuring the sidebar.
- [class UITabSidebarItem](../uitabsidebaritem.md)
- [UITabBarController.Sidebar.Animating](../uitabbarcontroller/sidebar-swift.class/animating.md)
- [UITabSidebarScrollTarget](../uitabsidebarscrolltarget.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabsidebaritem/request)*