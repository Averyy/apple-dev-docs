# UITab.Placement

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

A tab’s placement when displayed in contexts that allow different placement.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
enum Placement
```

```c
enum UITabPlacement : NSInteger;
```

## Topics

### Placement values
- [UITab.Placement.automatic](./placement/automatic.md)
  The system adds only top-level items to the tab bar, but people can add, remove, or move this item.
- [UITab.Placement.default](./placement/default.md)
  The item appears in the tab bar, but people can move or remove it.
- [UITab.Placement.fixed](./placement/fixed.md)
  The item appears in the tab bar’s leading edge, and people can’t move or remove it.
- [UITab.Placement.movable](./placement/movable.md)
  The item appears in the tab bar, people can move it but can’t remove it.
- [UITab.Placement.optional](./placement/optional.md)
  The item doesn’t appear in the tab bar, but people can add it and move it.
- [UITab.Placement.pinned](./placement/pinned.md)
  The item appears as a pinned tab, on the trailing edge of the tab bar.
- [UITab.Placement.sidebarOnly](./placement/sidebaronly.md)
  The item only appears in the sidebar.
### Initializers
- [init?(rawValue: Int)](./placement/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing customization
- [var isHidden: Bool](./ishidden.md)
  A Boolean value that indicates whether an item is hidden in a sidebar.
- [var isHiddenByDefault: Bool](./ishiddenbydefault.md)
  A Boolean value that indicates whether an item is hidden by default.
- [var allowsHiding: Bool](./allowshiding.md)
  A Boolean value that indicates whether people can hide a tab in a sidebar.
- [var preferredPlacement: UITab.Placement](./preferredplacement.md)
  The preferred placement for a tab when displayed in contexts that allow different placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitab/placement)*