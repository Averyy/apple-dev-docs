# ActivityConfiguration

**Framework**: WidgetKit  
**Kind**: struct

An object that describes the content of a Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
@MainActor
@preconcurrency struct ActivityConfiguration<Attributes> where Attributes : ActivityAttributes
```

## Mentions

- [Creating a widget extension](creating-a-widget-extension.md)

#### Overview

To learn more about offering Live Activities for your app, see [`ActivityKit`](https://developer.apple.com/documentation/ActivityKit).

## Topics

### Creating a Live Activity configuration
- [struct ActivityViewContext](activityviewcontext.md)
  A structure that describes the view context for creating the views of a Live Activity.
- [init<Content>(for: Attributes.Type, content: (ActivityViewContext<Attributes>) -> Content, dynamicIsland: (ActivityViewContext<Attributes>) -> DynamicIsland)](activityconfiguration/init(for:content:dynamicisland:).md)
  Creates a configuration object for a Live Activity.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [WidgetConfiguration](../SwiftUI/WidgetConfiguration.md)

## See Also

- [struct DynamicIsland](dynamicisland.md)
  The layout and configuration for a Live Activity that appears in the Dynamic Island.
- [let NSUserActivityTypeLiveActivity: String](nsuseractivitytypeliveactivity.md)
  A string that the system passes to the app on launch from a Live Activity that doesn’t provide a URL.
- [enum ActivityPreviewViewKind](activitypreviewviewkind.md)
  Values that represent Live Activity presentations for use in Xcode previews.
- [enum ActivityFamily](activityfamily.md)
  A family that defines the Live Activity’s size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/activityconfiguration)*