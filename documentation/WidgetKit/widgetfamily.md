# WidgetFamily

**Framework**: WidgetKit  
**Kind**: enum

Values that define the widget’s size and shape.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- visionOS 26.0+
- watchOS 9.0+

## Declaration

```swift
@preconcurrency
enum WidgetFamily
```

#### Overview

Widgets can support one or more sizes, giving users the flexibility to configure their widgets however they like. Each widget size provides a different amount of space for detail, so consider which sizes work best for the type of information the widget displays. For more information about designing widgets, see [`Widgets`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/widgets/overview/introduction/) or [`Complications`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/watchos/overview/complications/).

> **Note**: The sizes of widgets may vary across devices. Your widget content should be flexible and avoid using fixed values.

You specify the sizes your widget supports using the [`supportedFamilies(_:)`](https://developer.apple.com/documentation/SwiftUI/WidgetConfiguration/supportedFamilies(_:)) property modifier when defining your widget’s configuration.

```swift
struct GameStatusWidget: Widget {
    var body: some WidgetConfiguration {
        StaticConfiguration(
            kind: "com.mygame.game-status",
            provider: GameStatusProvider(),
            placeholder: GameStatusPlaceholderView()
        ) { entry in
            GameStatusView(entry.gameStatus)
        }
        .configurationDisplayName("Game Status")
        .description("Shows an overview of your game status")
        .supportedFamilies([.systemSmall, .systemMedium, .systemLarge])
    }
}
```

When WidgetKit needs to load a widget’s timeline, it calls the [`TimelineProvider`](timelineprovider.md) class’s [`getTimeline(in:completion:)`](timelineprovider/gettimeline(in:completion:).md) method. The system passes a [`TimelineProviderContext`](timelineprovidercontext.md) instance to the method’s `context` parameter. Use the context’s [`family`](timelineprovidercontext/family.md) property to determine the widget’s size and shape. For example, the [`WidgetFamily.systemSmall`](widgetfamily/systemsmall.md) family represents a small, square widget on the Home Screen or Today View in iOS or iPadOS, while, in watchOS the[`WidgetFamily.accessoryCorner`](widgetfamily/accessorycorner.md) family appears as a widget-based complication in the corner of a watch face.

Use the [`WidgetFamily`](widgetfamily.md) value to return the appropriate content given the widget’s size. For example, a [`WidgetFamily.systemSmall`](widgetfamily/systemsmall.md) widget may focus on showing only the most critical data, such as a single image or a simple gauge, while a [`WidgetFamily.systemLarge`](widgetfamily/systemlarge.md) widget can contain additional details, more-complex graphs, and even small blocks of text.

## Topics

### Accessing system families
- [WidgetFamily.systemSmall](widgetfamily/systemsmall.md)
  A small widget.
- [WidgetFamily.systemMedium](widgetfamily/systemmedium.md)
  A medium-sized widget.
- [WidgetFamily.systemLarge](widgetfamily/systemlarge.md)
  A large widget.
- [WidgetFamily.systemExtraLarge](widgetfamily/systemextralarge.md)
  An extra-large widget.
- [WidgetFamily.systemExtraLargePortrait](widgetfamily/systemextralargeportrait.md)
  An extra-large widget that uses a portrait orientation.
### Accessing accessory families
- [WidgetFamily.accessoryCircular](widgetfamily/accessorycircular.md)
  A circular widget.
- [WidgetFamily.accessoryCorner](widgetfamily/accessorycorner.md)
  A widget-based complication in the corner of a watch face in watchOS.
- [WidgetFamily.accessoryRectangular](widgetfamily/accessoryrectangular.md)
  A rectangular widget.
- [WidgetFamily.accessoryInline](widgetfamily/accessoryinline.md)
  A flat widget that contains a single row of text and an optional image.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Creating a widget extension](creating-a-widget-extension.md)
  Display your app’s content in a convenient, informative widget on various devices.
- [Developing a WidgetKit strategy](developing-a-widgetkit-strategy.md)
  Explore features, tasks, related frameworks, and constraints as you make a plan to implement widgets, controls, watch complications, and Live Activities.
- [Emoji Rangers: Supporting Live Activities, interactivity, and animations](emoji-rangers-supporting-live-activities-interactivity-and-animations.md)
  Offer Live Activities, controls, animate data updates, and add interactivity to widgets.
- [Preparing widgets for additional platforms, contexts, and appearances](preparing-widgets-for-additional-contexts-and-appearances.md)
  Create widgets that support additional platforms and adapt to their context.
- [protocol Widget](../SwiftUI/Widget.md)
  The configuration and content of a widget to display on the Home screen or in Notification Center.
- [struct StaticConfiguration](staticconfiguration.md)
  An object describing the content of a widget that has no user-configurable options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetfamily)*