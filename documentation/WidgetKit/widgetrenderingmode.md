# WidgetRenderingMode

**Framework**: WidgetKit  
**Kind**: struct

Constants that indicate the rendering mode for a widget.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- visionOS 26.0+ (Beta)
- watchOS 9.0+

## Declaration

```swift
struct WidgetRenderingMode
```

## Mentions

- [Migrating ClockKit complications to WidgetKit](converting-a-clockkit-app.md)

#### Overview

The system can modify the appearance of accessory family widgets. For example, it renders widgets on the Lock Screen on iPhone using the [`vibrant`](widgetrenderingmode/vibrant.md) mode, while it renders widget-based complications in watchOS using either the [`fullColor`](widgetrenderingmode/fullcolor.md) or [`accented`](widgetrenderingmode/accented.md) modes, depending on the watch face and the user’s settings.

You can read the rendering mode from the environment values using the `.widgetRenderingMode` key.

```swift
@Environment(\.widgetRenderingMode) var widgetRenderingMode
```

You can then customize your widget’s design based on the rendering mode.

## Topics

### Rendering modes
- [static let fullColor: WidgetRenderingMode](widgetrenderingmode/fullcolor.md)
  The system renders the widget in full color.
- [static let accented: WidgetRenderingMode](widgetrenderingmode/accented.md)
  The system divides the widget’s view hierarchy into an accent group and a default group, applying a different color to each group.
- [static let vibrant: WidgetRenderingMode](widgetrenderingmode/vibrant.md)
  The system desaturates the widget, making a monochrome version that it uses to create an adaptive, vibrant effect.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [Preparing widgets for additional platforms, contexts, and appearances](preparing-widgets-for-additional-contexts-and-appearances.md)
  Create widgets that support additional platforms and adapt to their context.
- [Displaying the right widget background](displaying-the-right-widget-background.md)
  Group your widget’s background views and mark them as removable to ensure your widget appears correctly for each context and platform.
- [Optimizing your widget for accented rendering mode and Liquid Glass](optimizing-your-widget-for-accented-rendering-mode-and-liquid-glass.md)
  Make your widget feel at home on Apple platforms and Liquid Glass by using accented rendering mode.
- [Adding StandBy and CarPlay support to your widget](adding-standby-and-carplay-support-to-your-widget.md)
  Ensure that your small system family widget works well in StandBy and CarPlay.
- [Creating views for widgets, Live Activities, and watch complications](creating-views-for-widgets-live-activities-and-watch-complications.md)
  Implement glanceable views with WidgetKit and SwiftUI.
- [SwiftUI views for widgets](swiftui-views.md)
  Present your app’s content in widgets with SwiftUI views.
- [Introducing SwiftUI](https://developer.apple.com/tutorials/SwiftUI)
  SwiftUI is a modern way to declare user interfaces for any Apple platform. Create beautiful, dynamic apps faster than ever before.
- [struct WidgetAccentedRenderingMode](widgetaccentedrenderingmode.md)
  Constants that indicate the rendering mode for an `Image` in when displayed in a widget in [`accented`](widgetrenderingmode/accented.md) mode.
- [struct AccessoryWidgetBackground](accessorywidgetbackground.md)
  An adaptive background view that provides a standard appearance based on the the widget’s environment.
- [struct WidgetLocation](widgetlocation.md)
  Values that indicate different widget locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/widgetkit/widgetrenderingmode)*