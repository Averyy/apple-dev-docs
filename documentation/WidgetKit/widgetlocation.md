# WidgetLocation

**Framework**: WidgetKit  
**Kind**: struct

Values that indicate different widget locations.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- watchOS 26.0+

## Declaration

```swift
struct WidgetLocation
```

## Mentions

- [Preparing widgets for additional platforms, contexts, and appearances](preparing-widgets-for-additional-contexts-and-appearances.md)

## Topics

### Specifying a location style
- [static let carPlay: WidgetLocation](widgetlocation/carplay.md)
  The CarPlay location for a widget.
- [static let iPhoneWidgetsOnMac: WidgetLocation](widgetlocation/iphonewidgetsonmac.md)
  The widget originates from another device and appears on the Mac.
- [static let homeScreen: WidgetLocation](widgetlocation/homescreen.md)
  The widget appears on the Home Screen or in Today View.
- [static let lockScreen: WidgetLocation](widgetlocation/lockscreen.md)
  The widget appears on the Lock Screen.
- [static let smartStack: WidgetLocation](widgetlocation/smartstack.md)
- [static let standBy: WidgetLocation](widgetlocation/standby.md)
  The widget appears in StandBy.
- [static let watchFace: WidgetLocation](widgetlocation/watchface.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [struct AccessoryWidgetBackground](accessorywidgetbackground.md)
  An adaptive background view that provides a standard appearance based on the the widget’s environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetlocation)*