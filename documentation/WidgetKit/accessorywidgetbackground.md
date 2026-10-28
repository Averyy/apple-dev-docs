# AccessoryWidgetBackground

**Framework**: WidgetKit  
**Kind**: struct  
**Role**: Structure

An adaptive background view that provides a standard appearance based on the the widget’s environment.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 26.0+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency struct AccessoryWidgetBackground
```

## Mentions

- [Migrating ClockKit complications to WidgetKit](./converting-a-clockkit-app.md)
- [Displaying the right widget background](./displaying-the-right-widget-background.md)

## Overview

Use this view to provide a standardized background for your accessory widgets. Place the view in a [`ZStack`](../SwiftUI/zstack.md) behind your widget’s content.

```swift
ZStack {
    AccessoryWidgetBackground()
    VStack {
        Text("MON")
            .font(.caption)
            .widgetAccentable()
        Text("6")
            .font(.title)
    }
}
```

The system only displays this view inside a [`WidgetFamily.accessoryCircular`](./widgetfamily/accessorycircular.md), [`WidgetFamily.accessoryCorner`](./widgetfamily/accessorycorner.md), or [`WidgetFamily.accessoryRectangular`](./widgetfamily/accessoryrectangular.md) widget. In any other context, the system displays an empty view instead.

## Topics

### Creating accessory widget backgrounds
- [init()](./accessorywidgetbackground/init%28%29.md)
  Creates an instance of an accessory widget background.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [View](../SwiftUI/view.md)

## See Also

### Layout and presentation
- [Supporting additional widget sizes](./supporting-additional-widget-sizes.md)
  Offer widgets in additional contexts by adding support for various widget sizes.
- [Displaying the right widget background](./displaying-the-right-widget-background.md)
  Group your widget’s background views and mark them as removable to ensure your widget appears correctly for each context and platform.
- [Optimizing your widget for accented rendering mode and Liquid Glass](./optimizing-your-widget-for-accented-rendering-mode-and-liquid-glass.md)
  Make your widget feel at home on Apple platforms and Liquid Glass by using accented rendering mode.
- [Adding StandBy and CarPlay support to your widget](./adding-standby-and-carplay-support-to-your-widget.md)
  Ensure that your small system family widget works well in StandBy and CarPlay.
- [struct WidgetRenderingMode](./widgetrenderingmode.md)
  Constants that indicate the rendering mode for a widget.
- [struct WidgetAccentedRenderingMode](./widgetaccentedrenderingmode.md)
  Constants that indicate the rendering mode for an `Image` in when displayed in a widget in [`accented`](./widgetrenderingmode/accented.md) mode.
- [struct WidgetLocation](./widgetlocation.md)
  Values that indicate different widget locations.
- [func widgetAccentable(Bool) -> some View
](../SwiftUI/view/widgetaccentable%28_%29.md)
  Adds the view and all of its subviews to the accented group.
- [func widgetAccentedRenderingMode(WidgetAccentedRenderingMode?) -> some View
](../SwiftUI/image/widgetaccentedrenderingmode%28_%29.md)
  Specifies the how to render an `Image` when using the `WidgetKit/WidgetRenderingMode/accented` mode.
- [var widgetRenderingMode: WidgetRenderingMode](../SwiftUI/environmentvalues/widgetrenderingmode.md)
  The widget’s rendering mode, based on where the system is displaying it.
- [var widgetContentMargins: EdgeInsets](../SwiftUI/environmentvalues/widgetcontentmargins.md)
  A property that identifies the content margins of a widget.
- [static let widget: ContainerBackgroundPlacement](../SwiftUI/containerbackgroundplacement/widget.md)
  The container background placement for a widget.
- [var showsWidgetContainerBackground: Bool](../SwiftUI/environmentvalues/showswidgetcontainerbackground.md)
  An environment variable that indicates whether the background of a widget appears.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/accessorywidgetbackground)*