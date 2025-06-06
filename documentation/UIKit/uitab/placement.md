# UITab.Placement

**Framework**: UIKit  
**Kind**: enum

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

## Topics

### Placement values
- [UITab.Placement.automatic](uitab/placement/automatic.md)
  The system adds only top-level items to the tab bar, but people can add, remove, or move this item.
- [UITab.Placement.default](uitab/placement/default.md)
  The item appears in the tab bar, but people can move or remove it.
- [UITab.Placement.fixed](uitab/placement/fixed.md)
  The item appears in the tab bar’s leading edge, and people can’t move or remove it.
- [UITab.Placement.movable](uitab/placement/movable.md)
  The item appears in the tab bar, people can move it but can’t remove it.
- [UITab.Placement.optional](uitab/placement/optional.md)
  The item doesn’t appear in the tab bar, but people can add it and move it.
- [UITab.Placement.pinned](uitab/placement/pinned.md)
  The item appears as a pinned tab, on the trailing edge of the tab bar.
- [UITab.Placement.sidebarOnly](uitab/placement/sidebaronly.md)
  The item only appears in the sidebar.
### Initializers
- [init?(rawValue: Int)](uitab/placement/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var isHidden: Bool](uitab/ishidden.md)
  A Boolean value that indicates whether an item is hidden in a sidebar.
- [var isHiddenByDefault: Bool](uitab/ishiddenbydefault.md)
  A Boolean value that indicates whether an item is hidden by default.
- [var allowsHiding: Bool](uitab/allowshiding.md)
  A Boolean value that indicates whether people can hide a tab in a sidebar.
- [var preferredPlacement: UITab.Placement](uitab/preferredplacement.md)
  The preferred placement for a tab when displayed in contexts that allow different placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitab/placement)*