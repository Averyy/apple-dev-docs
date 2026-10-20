# UITabGroup.SidebarAppearance

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The appearance of a section in a sidebar.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
enum SidebarAppearance
```

```c
enum UITabGroupSidebarAppearance : NSUInteger;
```

## Topics

### Enumeration Cases
- [UITabGroup.SidebarAppearance.automatic](./sidebarappearance-swift.enum/automatic.md)
  The default appearance showing the group and its children appropriately depending on the group level it is in.
- [UITabGroup.SidebarAppearance.inline](./sidebarappearance-swift.enum/inline.md)
  Displays only the children alongside the group’s siblings.
- [UITabGroup.SidebarAppearance.rootSection](./sidebarappearance-swift.enum/rootsection.md)
  Displays the group and its children as a top-level group of the sidebar.
### Initializers
- [init?(rawValue: UInt)](./sidebarappearance-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring a tab group
- [var sidebarAppearance: UITabGroup.SidebarAppearance](./sidebarappearance-swift.property.md)
  The appearance of a tab group’s section in a sidebar.
- [var managingNavigationController: UINavigationController?](./managingnavigationcontroller.md)
  The controller that manages navigation for items in a sidebar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabgroup/sidebarappearance-swift.enum)*