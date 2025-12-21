# AccessoryWidgetBackground

**Framework**: WidgetKit  
**Kind**: struct

An adaptive background view that provides a standard appearance based on the the widget’s environment.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- visionOS 26.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency struct AccessoryWidgetBackground
```

## Mentions

- [Migrating ClockKit complications to WidgetKit](converting-a-clockkit-app.md)
- [Displaying the right widget background](displaying-the-right-widget-background.md)

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
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)

## See Also

- [Supporting additional widget sizes](supporting-additional-widget-sizes.md)
  Offer widgets in additional contexts by adding support for various widget sizes.
- [Displaying the right widget background](displaying-the-right-widget-background.md)
  Group your widget’s background views and mark them as removable to ensure your widget appears correctly for each context and platform.
- [Optimizing your widget for accented rendering mode and Liquid Glass](optimizing-your-widget-for-accented-rendering-mode-and-liquid-glass.md)
  Make your widget feel at home on Apple platforms and Liquid Glass by using accented rendering mode.
- [Adding StandBy and CarPlay support to your widget](adding-standby-and-carplay-support-to-your-widget.md)
  Ensure that your small system family widget works well in StandBy and CarPlay.
- [struct WidgetRenderingMode](widgetrenderingmode.md)
  Constants that indicate the rendering mode for a widget.
- [struct WidgetAccentedRenderingMode](widgetaccentedrenderingmode.md)
  Constants that indicate the rendering mode for an `Image` in when displayed in a widget in [`accented`](widgetrenderingmode/accented.md) mode.
- [struct WidgetLocation](widgetlocation.md)
  Values that indicate different widget locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/accessorywidgetbackground)*