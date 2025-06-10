# ActivityPreviewViewKind

**Framework**: WidgetKit  
**Kind**: enum

Values that represent Live Activity presentations for use in Xcode previews.

**Availability**:
- iOS 16.2+
- iPadOS 16.2+

## Declaration

```swift
@preconcurrency
enum ActivityPreviewViewKind
```

## Topics

### Live Activity preview types
- [ActivityPreviewViewKind.content](activitypreviewviewkind/content.md)
  The Live Activity presentation that appears on the Lock Screen and as a banner on devices that don’t support the Dynamic Island.
- [case dynamicIsland(ActivityPreviewViewKind.DynamicIslandPreviewViewState)](activitypreviewviewkind/dynamicisland(_:).md)
  The Live Activity presentation that appears in the Dynamic Island.
- [ActivityPreviewViewKind.DynamicIslandPreviewViewState](activitypreviewviewkind/dynamicislandpreviewviewstate.md)
  Values that represent the different presentations of a Live Activity in the Dynamic Island for use in Xcode previews.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ActivityConfiguration](activityconfiguration.md)
  An object that describes the content of a Live Activity.
- [struct DynamicIsland](dynamicisland.md)
  The layout and configuration for a Live Activity that appears in the Dynamic Island.
- [let NSUserActivityTypeLiveActivity: String](nsuseractivitytypeliveactivity.md)
  A string that the system passes to the app on launch from a Live Activity that doesn’t provide a URL.
- [enum ActivityFamily](activityfamily.md)
  A family that defines the Live Activity’s size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/activitypreviewviewkind)*