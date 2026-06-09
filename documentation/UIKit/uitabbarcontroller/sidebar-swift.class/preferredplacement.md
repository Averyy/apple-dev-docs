# preferredPlacement

**Framework**: UIKit  
**Kind**: property

The preferred placement for the tab bar controller when the sidebar and tab bar are mutually exclusive, and only one placement can be displayed.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var preferredPlacement: UITabBarController.Sidebar.Placement { get set }
```

#### Discussion

When set to `UITabBarControllerSidebarPlacementAutomatic`, the system resolves to the platform default. On iOS, this resolves to showing the tab bar by default. This property has no effect on platforms where multiple placements are supported, like on iPadOS, where the sidebar can be minimized into the top tab bar.

Default is `UITabBarControllerSidebarPlacementAutomatic`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/preferredplacement)*