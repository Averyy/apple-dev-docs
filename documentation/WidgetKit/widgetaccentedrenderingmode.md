# WidgetAccentedRenderingMode

**Framework**: WidgetKit  
**Kind**: struct

Constants that indicate the rendering mode for an `Image` in when displayed in a widget in [`accented`](widgetrenderingmode/accented.md) mode.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 26.0+
- watchOS 11.0+

## Declaration

```swift
struct WidgetAccentedRenderingMode
```

## Mentions

- [Optimizing your widget for accented rendering mode and Liquid Glass](optimizing-your-widget-for-accented-rendering-mode-and-liquid-glass.md)

## Topics

### Type Properties
- [static let accented: WidgetAccentedRenderingMode](widgetaccentedrenderingmode/accented.md)
  Specifies that the `Image` should be included as part of the accented widget group.
- [static let accentedDesaturated: WidgetAccentedRenderingMode](widgetaccentedrenderingmode/accenteddesaturated.md)
  Maps the luminance of the `Image` in to the alpha channel, replacing color channels with the color applied to the accent group.
- [static let desaturated: WidgetAccentedRenderingMode](widgetaccentedrenderingmode/desaturated.md)
  Maps the luminance of the `Image` in to the alpha channel, replacing color channels with the color applied to the default group.
- [static let fullColor: WidgetAccentedRenderingMode](widgetaccentedrenderingmode/fullcolor.md)
  Specifies that the `Image` should be rendered at full color with no other color modifications. Only applies to iOS.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

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
- [struct AccessoryWidgetBackground](accessorywidgetbackground.md)
  An adaptive background view that provides a standard appearance based on the the widget’s environment.
- [struct WidgetLocation](widgetlocation.md)
  Values that indicate different widget locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetaccentedrenderingmode)*