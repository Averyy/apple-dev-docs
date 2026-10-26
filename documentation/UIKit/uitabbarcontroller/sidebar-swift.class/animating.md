# UITabBarController.Sidebar.Animating

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
protocol Animating : NSObjectProtocol
```

```objc
@protocol UITabBarControllerSidebarAnimating <NSObject>
```

## Topics

### Instance Methods
- [func addAnimations(() -> Void)](./animating/addanimations%28_%29.md)
- [func addCompletion(() -> Void)](./animating/addcompletion%28_%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Supporting the sidebar
- [var mode: UITabBarController.Mode](../mode-swift.property.md)
  The display mode for a tab bar.
- [UITabBarController.Mode](../mode-swift.enum.md)
  A tab bar’s display mode.
- [var sidebar: UITabBarController.Sidebar](../sidebar-swift.property.md)
  A tab bar’s corresponding sidebar.
- [UITabBarController.Sidebar](../sidebar-swift.class.md)
  An object for managing and configuring the sidebar.
- [class UITabSidebarItem](../../uitabsidebaritem.md)
- [UITabSidebarItem.Request](../../uitabsidebaritem/request.md)
- [UITabSidebarScrollTarget](../../uitabsidebarscrolltarget.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/animating)*