# AccessoryWidgetBackground

**Framework**: Widgetkit  
**Kind**: struct

An adaptive background view that provides a standard appearance based on the the widget’s environment.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency struct AccessoryWidgetBackground
```

## Mentions

- [Preparing widgets for additional platforms, contexts, and appearances](preparing-widgets-for-additional-contexts-and-appearances.md)
- [Migrating ClockKit complications to WidgetKit](converting-a-clockkit-app.md)

#### Overview

Use this view to provide a standardized background for your accessory widgets. Place the view in a [`ZStack`](https://developer.apple.com/documentation/SwiftUI/ZStack) behind your widget’s content.

```Swift
ZStack {
    AccessoryWidgetBackground()
    VStack {
        Text("MON")
            .font(.caption)
            .widgetAccented()
        Text("6")
            .font(.title)
    }
}
```

The system only displays this view inside a [`WidgetFamily.accessoryCircular`](widgetfamily/accessorycircular.md), [`WidgetFamily.accessoryCorner`](widgetfamily/accessorycorner.md), or [`WidgetFamily.accessoryRectangular`](widgetfamily/accessoryrectangular.md) widget. In any other context, the system displays an empty view instead.

## Topics

### Creating accessory widget backgrounds
- [init()](accessorywidgetbackground/init.md)
  Creates an instance of an accessory widget background.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [View](../SwiftUI/View.md)

## See Also

- [Creating views for widgets, Live Activities, and watch complications](creating-views-for-widgets-live-activities-and-watch-complications.md)
  Implement glanceable views with WidgetKit and SwiftUI.
- [Preparing widgets for additional platforms, contexts, and appearances](preparing-widgets-for-additional-contexts-and-appearances.md)
  Create widgets that support additional platforms and adapt to their context.
- [SwiftUI views for widgets](swiftui-views.md)
  Present your app’s content in widgets with SwiftUI views.
- [Introducing SwiftUI](https://developer.apple.com/tutorials/SwiftUI)
  SwiftUI is a modern way to declare user interfaces for any Apple platform. Create beautiful, dynamic apps faster than ever before.
- [struct WidgetLocation](widgetlocation.md)
  Values that indicate different widget locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/accessorywidgetbackground)*