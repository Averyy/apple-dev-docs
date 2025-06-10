# ActivityPreviewViewKind.DynamicIslandPreviewViewState

**Framework**: WidgetKit  
**Kind**: enum

Values that represent the different presentations of a Live Activity in the Dynamic Island for use in Xcode previews.

**Availability**:
- iOS 16.2+
- iPadOS 16.2+

## Declaration

```swift
@preconcurrency
enum DynamicIslandPreviewViewState
```

## Topics

### Dynamic Island presentations
- [ActivityPreviewViewKind.DynamicIslandPreviewViewState.compact](activitypreviewviewkind/dynamicislandpreviewviewstate/compact.md)
  The presentation of a Live Activity in the Dynamic Island that shows both the [`compactLeading`](dynamicislandmode/compactleading.md) and [`compactTrailing`](dynamicislandmode/compacttrailing.md) views combined.
- [ActivityPreviewViewKind.DynamicIslandPreviewViewState.minimal](activitypreviewviewkind/dynamicislandpreviewviewstate/minimal.md)
  The minimal presentation of a Live Activity in the Dynamic Island.
- [ActivityPreviewViewKind.DynamicIslandPreviewViewState.expanded](activitypreviewviewkind/dynamicislandpreviewviewstate/expanded.md)
  The expanded presentation of a Live Activity in the Dynamic Island.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [ActivityPreviewViewKind.content](activitypreviewviewkind/content.md)
  The Live Activity presentation that appears on the Lock Screen and as a banner on devices that don’t support the Dynamic Island.
- [case dynamicIsland(ActivityPreviewViewKind.DynamicIslandPreviewViewState)](activitypreviewviewkind/dynamicisland(_:).md)
  The Live Activity presentation that appears in the Dynamic Island.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/activitypreviewviewkind/dynamicislandpreviewviewstate)*